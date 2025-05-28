from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    preferred_username = Column(String, nullable=True)
    email = Column(String, nullable=True)

    messages = relationship("Message", back_populates="user")
