from fastapi import HTTPException, Request
from pydantic import BaseModel
from fastapi_keycloak import OIDCUser as KeycloakOIDCUser
import structlog

log = structlog.get_logger(__name__)

class OIDCUser(BaseModel):
    """Subset of common OpenID Connect claims."""

    sub: str
    preferred_username: str | None = None
    email: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    name: str | None = None


def get_user(request: Request) -> OIDCUser:
    """Extract the OIDC user from middleware claims."""
    user_claims = getattr(request.state, "user", None) or request.scope.get("user")
    if not isinstance(user_claims, dict):
        raise HTTPException(status_code=401, detail="User not authenticated")
    return OIDCUser.model_validate(user_claims)


def map_user(user: KeycloakOIDCUser) -> dict:
    """Map FastAPI-Keycloak user to a plain dictionary for request state."""
    oidc_user = OIDCUser(
        sub=user.sub,
        preferred_username=getattr(user, "preferred_username", None),
        email=getattr(user, "email", None),
        given_name=getattr(user, "given_name", None),
        family_name=getattr(user, "family_name", None),
        name=getattr(user, "name", None),
    )
    return oidc_user.model_dump()
