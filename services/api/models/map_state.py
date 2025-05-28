from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import Base


class MapState(Base):
    __tablename__ = "map_states"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    state = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user = relationship("User", back_populates="map_states")
