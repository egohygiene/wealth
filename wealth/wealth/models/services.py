from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from uuid import uuid4

class Service(BaseModel):
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    name: str = Field(..., description="Service name, e.g., 'Spotify', 'TurboTax'")
    url: Optional[HttpUrl] = Field(default=None, description="Website or login portal")
    logo_url: Optional[HttpUrl] = Field(default=None, description="Optional brand icon or favicon")
    provider: Optional[str] = Field(default=None, description="The company offering the service")
    notes: Optional[str] = Field(default=None, description="Optional description or setup instructions")
