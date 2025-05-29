from fastapi import HTTPException, Request
from pydantic import BaseModel

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
