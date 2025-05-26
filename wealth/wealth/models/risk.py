from enum import Enum, unique
from typing import Optional
from uuid import uuid4
from datetime import datetime, timezone
from pydantic import BaseModel, Field

# 🧠 Risk Type — Object-Level Assessment
@unique
class RiskType(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    SPECULATIVE = "speculative"
    GUARANTEED = "guaranteed"

# 🧠 Risk Profile — User-Level Strategy
@unique
class RiskProfile(str, Enum):
    CONSERVATIVE = "conservative"
    MODERATE = "moderate"
    BALANCED = "balanced"
    AGGRESSIVE = "aggressive"
    SPECULATIVE = "speculative"

# 🎯 Risk Object — Links a score and category to any UUID in the system
class Risk(BaseModel):
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    name: str
    score: float = Field(..., ge=0.0, le=1.0, description="Numerical risk value from 0 (low) to 1 (high)")
    level: RiskType = Field(..., description="Categorical risk type (low, medium, high, etc.)")
    description: Optional[str] = None

    source_object_type: Optional[str] = Field(default=None, description="What object this risk applies to (e.g., 'investment', 'debt')")
    source_object_id: Optional[str] = Field(default=None, description="UUID of the associated object")

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
