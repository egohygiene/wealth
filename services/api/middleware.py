from __future__ import annotations

import uuid
from typing import Callable, Awaitable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import structlog

log = structlog.get_logger(__name__)


class RequestContextMiddleware(BaseHTTPMiddleware):
    """Attach request context (id, path, user) to structlog."""

    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        """Bind request context vars, execute the call chain, and unbind."""
        request_id = str(uuid.uuid4())
        user = getattr(request.state, "user", None)
        structlog.contextvars.bind_contextvars(
            request_id=request_id,
            path=request.url.path,
            user_id=getattr(user, "sub", None) if user else None,
        )
        log.info("request.start", method=request.method, path=request.url.path)
        try:
            response = await call_next(request)
        finally:
            log.info("request.end", status_code=getattr(response, "status_code", 500))
            structlog.contextvars.unbind_contextvars("request_id", "path", "user_id")
        response.headers["X-Request-ID"] = request_id
        return response
