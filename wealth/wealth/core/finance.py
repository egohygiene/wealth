from __future__ import annotations
from pathlib import Path

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Optional

from wealth.models import (
    Allocation, Expense, Income, Debt, Investment, LifecyclePhase,
    Portfolio, RiskProfile, Service
)

class FinanceSummary(BaseModel):
    net_worth: float
    investment_count: int
    debt_count: int
    allocation_count: int

    def to_dict(self):
        return self.model_dump()

    def to_json(self, indent: Optional[int] = 4):
        return self.model_dump_json(indent=indent)


class Finance(BaseModel):
    user_id: str

    # Core financial records
    allocations: List[Allocation] = []
    expenses: List[Expense] = []
    income_streams: List[Income] = []
    debts: List[Debt] = []
    investments: List[Investment] = []
    portfolios: List[Portfolio] = []

    # Optional services (linked accounts, platforms)
    services: List[Service] = []

    # Contextual metadata
    roles: List[str] = []
    features: List[str] = []
    lifecycle_phase: LifecyclePhase = LifecyclePhase.STABILIZING
    risk_profile: Optional[RiskProfile] = RiskProfile.BALANCED
    notes: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def total_net_worth(self) -> float:
        assets = sum(inv.current_value for inv in self.investments)
        liabilities = sum(debt.balance for debt in self.debts)
        return assets - liabilities

    def to_dict(self):
        return self.model_dump()

    def to_json(self, indent: Optional[int] = 4):
        return self.model_dump_json(indent=indent)

    def add_allocation(self, allocation: Allocation):
        """Adds a new allocation to the finance object and auto-assigns the user_id if missing."""
        if not allocation.user_id:
            allocation.user_id = self.user_id
        self.allocations.append(allocation)

    @classmethod
    def default(cls, user_id: str, notes: Optional[str] = None) -> Finance:
        return cls(
            user_id=user_id,
            roles=[
                "freelancer", "parent", "student", "business_owner", "engineer"
            ],
            features=[
                "budgeting",
                "debt_tracking",
                "investment_dashboard",
                "risk_analysis",
                "income_projection",
                "visual_reports",
                "goal_tracking"
            ],
            lifecycle_phase=LifecyclePhase.STABILIZING,
            risk_profile=RiskProfile.BALANCED,
            notes=notes or "Default system initialized with all roles and features."
        )

    def get_allocation_breakdown(self) -> dict[str, float]:
        """Returns a dictionary of allocation names and their budgeted amounts."""
        breakdown: dict[str, float] = {}
        for alloc in self.allocations:
            if alloc.is_active and alloc.budget_amount:
                breakdown[alloc.name] = round(alloc.budget_amount, 2)
        return breakdown

    def plot_allocation_chart(self, show: bool = True, save_path: Optional[str] = None):
        # pyright: ignore[reportMissingTypeStubs]
        import plotly.express as px # type: ignore

        breakdown = self.get_allocation_breakdown()
        if not breakdown:
            print("No allocation data to display.")
            return

        labels = list(breakdown.keys())
        values = list(breakdown.values())

        fig = px.pie(
            names=labels,
            values=values,
            title="Allocation Breakdown",
            hole=0.3  # Donut-style
        )

        if save_path:
            save_path: Path = Path(save_path)
            save_path.parent.mkdir(parents=True, exist_ok=True)
            fig.write_image(save_path)
            print(f"✅ Plotly chart saved to {save_path}")

        if show:
            fig.show()
