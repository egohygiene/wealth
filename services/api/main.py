from fastapi import FastAPI, Depends, Request
from pydantic import BaseModel
import asyncpg
from fastapi_keycloak import FastAPIKeycloak, OIDCUser
from authlib.integrations.starlette_client import OAuth

from .config import get_config

app = FastAPI(title="Wealth API")

config = get_config()

DATABASE_URL = (
    f"postgresql://{config.db_user}:{config.db_password}@"
    f"{config.db_host}:{config.db_port}/{config.db_name}"
)

db_pool: asyncpg.Pool | None = None

# Configure Keycloak connection. Adjust URLs and secrets for your environment.
keycloak = FastAPIKeycloak(
    server_url=config.keycloak_server_url,
    client_id=config.keycloak_client_id,
    client_secret=config.keycloak_client_secret,
    admin_client_secret=config.keycloak_admin_client_secret,
    realm=config.keycloak_realm,
    redirect_uri=config.keycloak_redirect_uri,
)

# Configure Google OAuth2
oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=config.google_client_id,
    client_secret=config.google_client_secret,
    client_kwargs={"scope": "openid email profile"},
)

# Initialise the connection on startup
@app.on_event("startup")
async def startup_event():
    await keycloak.load_config()
    global db_pool
    db_pool = await asyncpg.create_pool(DATABASE_URL)
    async with db_pool.acquire() as conn:
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS locations (
                id SERIAL PRIMARY KEY,
                name TEXT,
                geom geometry(Point, 4326)
            )
            """
        )
        await conn.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                user_id TEXT,
                content TEXT
            )
            """
        )

# Close database connections on shutdown
@app.on_event("shutdown")
async def shutdown_event():
    if db_pool:
        await db_pool.close()

# Expose authentication routes (login, callback, etc.)
app.include_router(keycloak.get_auth_router())

# Google authentication routes
@app.get("/login/google")
async def login_google(request: Request):
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


@app.get("/auth/google")
async def google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)
    return {
        "username": user.get("email"),
        "google_id": user.get("sub"),
    }

# Example protected endpoint
@app.get("/me")
def read_current_user(user: OIDCUser = Depends(keycloak.get_current_user())):
    return {
        "username": user.preferred_username,
        "email": user.email,
    }


class Location(BaseModel):
    name: str
    latitude: float
    longitude: float


class PostIn(BaseModel):
    content: str


class Post(PostIn):
    id: int
    user_id: str


@app.post("/locations")
async def create_location(location: Location):
    if not db_pool:
        raise RuntimeError("Database not initialized")
    async with db_pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO locations (name, geom) VALUES ($1, ST_SetSRID(ST_MakePoint($2, $3), 4326))",
            location.name,
            location.longitude,
            location.latitude,
        )
    return {"status": "ok"}


@app.get("/locations")
async def read_locations():
    if not db_pool:
        raise RuntimeError("Database not initialized")
    async with db_pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, name, ST_Y(geom) AS latitude, ST_X(geom) AS longitude FROM locations"
        )
        return [dict(row) for row in rows]


@app.post("/posts", response_model=Post)
async def create_post(
    post: PostIn, user: OIDCUser = Depends(keycloak.get_current_user())
):
    if not db_pool:
        raise RuntimeError("Database not initialized")
    async with db_pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO posts (user_id, content) VALUES ($1, $2) RETURNING id",
            user.sub,
            post.content,
        )
        return Post(id=row["id"], user_id=user.sub, content=post.content)


@app.get("/posts", response_model=list[Post])
async def read_posts(user: OIDCUser = Depends(keycloak.get_current_user())):
    if not db_pool:
        raise RuntimeError("Database not initialized")
    async with db_pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, user_id, content FROM posts WHERE user_id = $1",
            user.sub,
        )
        return [Post(id=row["id"], user_id=row["user_id"], content=row["content"]) for row in rows]

