from __future__ import annotations
from pathlib import Path

from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import List, Optional

from wealth.core.utils import format_currency

from wealth.models import (
    Allocation,
    Expense,
    Income,
    Debt,
    Investment,
    LifecyclePhase,
    Portfolio,
    RiskProfile,
    Service,
    Frequency,
)
import structlog

log = structlog.get_logger(__name__)

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

    def add_allocations(self, allocations: List[Allocation]):
        """Adds multiple allocations using the single-object add_allocation method."""
        for allocation in allocations:
            self.add_allocation(allocation)

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

    def plot_allocation_chart(
        self,
        frequency: Frequency = Frequency.MONTHLY,
        show: bool = True,
        save_path: Optional[str] = None
    ):
        import plotly.express as px  # type: ignore
        from pathlib import Path

        breakdown = self.get_allocation_breakdown()
        if not breakdown:
            log.info("No allocation data to display")
            return

        # 💡 Frequency conversion via enum method
        transformed = {k: frequency.from_monthly(v) for k, v in breakdown.items()}

        names = list(transformed.keys())
        values = list(transformed.values())
        formatted_values = [format_currency(v) for v in values]

        # ✨ Create DataFrame with custom hover data
        import pandas as pd
        df = pd.DataFrame({
            "label": names,
            "value": values,
            "formatted": formatted_values
        })

        # 📈 Build pie chart with custom data
        fig = px.pie(
            df,
            names="label",
            values="value",
            title=f"Allocation Breakdown – {frequency.value.replace('_', ' ').title()}",
            hole=0.3,
            custom_data=["formatted"]
        )

        # ✅ Show only % on chart, and formatted currency in hover
        fig.update_traces(
            textinfo="percent",
            hovertemplate="%{label}<br>%{customdata[0]}<extra></extra>"
        )

        if save_path:
            output_path: Path = Path(save_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            fig.write_image(output_path)
            log.info("Plotly chart saved", path=str(output_path))

        if show:
            fig.show()
