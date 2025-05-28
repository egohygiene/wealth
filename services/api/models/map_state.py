from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from services.api.constants import MAP_STATES_TABLE, USERS_TABLE

from .base import Base


class MapState(Base):
    __tablename__ = MAP_STATES_TABLE

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey(f"{USERS_TABLE}.id"), nullable=False)
    state = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user = relationship("User", back_populates="map_states")
