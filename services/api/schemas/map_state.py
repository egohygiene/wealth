from datetime import datetime
from pydantic import BaseModel

from .user import UserRead


class MapStateCreate(BaseModel):
    state: dict


class MapStateRead(MapStateCreate):
    id: int
    user: UserRead
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
