from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    preferred_username: str | None = None
    email: str | None = None


class UserRead(UserBase):
    class Config:
        from_attributes = True
