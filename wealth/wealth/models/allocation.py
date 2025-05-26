from enum import Enum, unique
from typing import Optional, List
from pydantic import Field
from wealth.models.wealth import Wealth
from wealth.models.risk import Risk, RiskType
from wealth.models.services import Service

@unique
class AllocationType(str, Enum):
    FIXED = "fixed"        # e.g., $100/month
    VARIABLE = "variable"  # e.g., 5% of income

class Allocation(Wealth):
    allocation_type: AllocationType = Field(..., description="Specifies whether the allocation is fixed or variable")
    budget_amount: Optional[float] = Field(default=None, description="Fixed dollar amount for the budgeted allocation")
    budget_percentage: Optional[float] = Field(default=None, description="Variable percentage of income for allocation")
    savings_bucket: Optional[str] = Field(default=None, description="Which account or goal this allocation is tied to")
    risk_score: float = Field(default=0.0, ge=0.0, le=1.0, description="Numeric score of perceived volatility or uncertainty")
    risk_level: RiskType = Field(default=RiskType.LOW, description="General risk classification for this allocation")
    risk: Optional[Risk] = Field(default=None, description="Optional structured Risk object")
    tags: List[str] = Field(default_factory=list)
    services: List[Service] = Field(default_factory=list, description="List of relevant services tied to this allocation")
    active: bool = Field(default=True, description="Is this allocation currently part of the active plan?")
