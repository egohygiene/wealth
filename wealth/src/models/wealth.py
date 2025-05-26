from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Wealth(BaseModel):
    id: str
    user_id: str
    name: str
    category: str
    description: Optional[str] = None
    tags: List[str] = []
    notes_to_self: Optional[str] = None
    active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
