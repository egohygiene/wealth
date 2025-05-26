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
