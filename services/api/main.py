from fastapi import Depends, FastAPI, Request
from fastapi_keycloak import FastAPIKeycloak

from .auth import OIDCUser, get_user
from .dao import MapStateDAO, MessageDAO, UserDAO
from authlib.integrations.starlette_client import OAuth
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from .config import get_config
from .database import engine, get_session
from .migrations import run_migrations_async
from .schemas import (
    MapStateCreate,
    MapStateRead,
    MessageCreate,
    MessageRead,
)

app = FastAPI(title="Wealth API")

config = get_config()

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


@app.on_event("startup")
async def startup_event() -> None:
    await keycloak.load_config()
    await run_migrations_async()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await engine.dispose()


# Expose authentication routes (login, callback, etc.)
app.include_router(keycloak.get_auth_router())


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


@app.get("/me")
def read_current_user(user: OIDCUser = Depends(get_user)):
    """Return all available claims for the current user."""
    return user.model_dump()


@app.post("/messages", response_model=MessageRead)
async def create_message(
    message_in: MessageCreate,
    session: AsyncSession = Depends(get_session),
    user: OIDCUser = Depends(get_user),
):
    user_dao = UserDAO(session)
    db_user = await user_dao.get_or_create(
        user.sub, user.preferred_username, user.email
    )

    message_dao = MessageDAO(session)
    return await message_dao.create(db_user, message_in.message)


@app.get("/messages", response_model=list[MessageRead])
async def read_messages(
    session: AsyncSession = Depends(get_session),
    user: OIDCUser = Depends(get_user),
):
    dao = MessageDAO(session)
    return await dao.list_all()


@app.post("/message/generate", response_model=MessageRead)
async def generate_message(
    session: AsyncSession = Depends(get_session),
    user: OIDCUser = Depends(get_user),
):
    user_dao = UserDAO(session)
    db_user = await user_dao.get_or_create(
        user.sub, user.preferred_username, user.email
    )

    message_dao = MessageDAO(session)
    generated_text = f"Auto-generated at {datetime.now(timezone.utc).isoformat()}!"
    return await message_dao.create(db_user, generated_text)


@app.post("/map_states", response_model=MapStateRead)
async def create_map_state(
    map_state_in: MapStateCreate,
    session: AsyncSession = Depends(get_session),
    user: OIDCUser = Depends(get_user),
):
    user_dao = UserDAO(session)
    db_user = await user_dao.get_or_create(
        user.sub, user.preferred_username, user.email
    )

    dao = MapStateDAO(session)
    return await dao.create(db_user, map_state_in.state)


@app.get("/map_states", response_model=list[MapStateRead])
async def read_map_states(
    session: AsyncSession = Depends(get_session),
    user: OIDCUser = Depends(get_user),
):
    dao = MapStateDAO(session)
    return await dao.list_all()
