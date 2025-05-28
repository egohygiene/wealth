from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from services.api.constants import USERS_TABLE

from .base import Base


class User(Base):
    __tablename__ = USERS_TABLE

    id = Column(String, primary_key=True)
    preferred_username = Column(String, nullable=True)
    email = Column(String, nullable=True)

    messages = relationship("Message", back_populates="user")
    map_states = relationship("MapState", back_populates="user")
