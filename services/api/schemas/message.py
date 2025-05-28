from datetime import datetime

from pydantic import BaseModel

from .user import UserRead


class MessageCreate(BaseModel):
    message: str = "Hello World"


class MessageRead(MessageCreate):
    id: int
    user: UserRead
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
