from typing import List, Optional, Dict
from pydantic import Field
from wealth.models.wealth import Wealth
from wealth.models.investment import Investment
from wealth.models.risk import RiskProfile

class Portfolio(Wealth):
    investments: List[Investment] = Field(default_factory=list, description="List of investments in this portfolio")
    risk_profile: Optional[RiskProfile] = Field(default=RiskProfile.BALANCED, description="Targeted risk strategy")
    strategy_label: Optional[str] = Field(default=None, description="Optional label for categorization or optimization strategy")
    notes: Optional[str] = None

    def total_value(self) -> float:
        """Return the combined current value of all investments."""
        return sum(inv.current_value for inv in self.investments)

    def allocation_breakdown(self) -> Dict[str, float]:
        """Return investment allocation percentages grouped by asset type."""
        total = self.total_value()
        breakdown = {}
        for inv in self.investments:
            asset = inv.asset_type.value
            breakdown[asset] = breakdown.get(asset, 0) + inv.current_value
        return {
            asset: round((value / total) * 100, 2) for asset, value in breakdown.items()
        } if total else {}

    def find_high_risk_assets(self) -> List[Investment]:
        """List investments flagged as high or speculative risk."""
        return [inv for inv in self.investments if inv.risk_level in ("high", "speculative")]

    def get_platforms(self) -> List[str]:
        """Return a unique list of investment platform names."""
        return list({inv.platform for inv in self.investments if inv.platform})
