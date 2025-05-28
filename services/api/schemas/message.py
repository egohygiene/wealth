from datetime import datetime

from pydantic import BaseModel


class MessageCreate(BaseModel):
    message: str = "Hello World"


class MessageRead(MessageCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
