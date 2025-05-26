from typing import Optional
from pydantic import Field

from wealth.models.wealth import Wealth
from wealth.models.asset import AssetType
from wealth.models.risk import Risk, RiskType

class Investment(Wealth):
    asset_type: AssetType = Field(..., description="The type of asset this investment represents")
    amount_invested: float = Field(0.0, description="The amount of money originally invested")
    current_value: float = Field(0.0, description="The current market value of the investment")
    platform: Optional[str] = Field(default=None, description="The brokerage or wallet provider (e.g. Fidelity, Coinbase)")
    risk_score: float = Field(0.0, ge=0.0, le=1.0, description="Numeric risk score (0-1)")
    risk_level: RiskType = Field(default=RiskType.MEDIUM, description="General risk category")
    risk: Optional[Risk] = Field(default=None, description="Optional detailed risk object")
    notes: Optional[str] = None
