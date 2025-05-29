from fastapi import Depends, HTTPException, Request
from pydantic import BaseModel
import structlog
from typing import Any, Dict

log = structlog.get_logger(__name__)

class OIDCUser(BaseModel):
    """Subset of common OpenID Connect claims."""

    sub: str
    preferred_username: str | None = None
    email: str | None = None
    given_name: str | None = None
    family_name: str | None = None
    name: str | None = None


def get_user(request: Request) -> Dict[str, Any]:
    """Return raw user info extracted from middleware claims."""
    user_claims = getattr(request.state, "user", None) or request.scope.get("user")
    if not isinstance(user_claims, dict):
        raise HTTPException(status_code=401, detail="User not authenticated")
    return user_claims


async def map_user(userinfo: Dict[str, Any] = Depends(get_user)) -> OIDCUser:
    """Convert raw user info to an ``OIDCUser`` instance."""
    if not isinstance(userinfo, dict):
        raise TypeError("userinfo must be a dictionary")
    return OIDCUser.model_validate(userinfo)
