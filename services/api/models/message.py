from sqlalchemy import Column, Integer, Text, DateTime, func, String, ForeignKey
from sqlalchemy.orm import relationship

from services.api.constants import MESSAGES_TABLE, USERS_TABLE

from .base import Base


class Message(Base):
    __tablename__ = MESSAGES_TABLE

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey(f"{USERS_TABLE}.id"), nullable=False)
    message = Column(Text, nullable=False, server_default="Hello World")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user = relationship("User", back_populates="messages")
