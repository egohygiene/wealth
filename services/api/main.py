from fastapi import FastAPI, Depends, Request
from fastapi_keycloak import FastAPIKeycloak, OIDCUser
from authlib.integrations.starlette_client import OAuth
import os

app = FastAPI(title="Wealth API")

# Configure Keycloak connection. Adjust URLs and secrets for your environment.
keycloak = FastAPIKeycloak(
    server_url="http://localhost:8080/auth/",
    client_id="wealth-api",
    client_secret="CHANGE_ME",
    admin_client_secret="CHANGE_ME",
    realm="wealth",
    redirect_uri="http://localhost:8000/callback",
)

# Configure Google OAuth2
oauth = OAuth()
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=os.getenv("GOOGLE_CLIENT_ID", "CHANGE_ME"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET", "CHANGE_ME"),
    client_kwargs={"scope": "openid email profile"},
)

# Initialise the connection on startup
@app.on_event("startup")
async def startup_event():
    await keycloak.load_config()

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
