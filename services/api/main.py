from fastapi import FastAPI, Depends
from fastapi_keycloak import FastAPIKeycloak, OIDCUser

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

# Initialise the connection on startup
@app.on_event("startup")
async def startup_event():
    await keycloak.load_config()

# Expose authentication routes (login, callback, etc.)
app.include_router(keycloak.get_auth_router())

# Example protected endpoint
@app.get("/me")
def read_current_user(user: OIDCUser = Depends(keycloak.get_current_user())):
    return {
        "username": user.preferred_username,
        "email": user.email,
    }
