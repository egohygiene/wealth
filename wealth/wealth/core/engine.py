from wealth.core.finance import Finance, FinanceSummary
from wealth.core.strategies import BudgetingStrategy, DebtStrategy, RiskStrategy

class FinanceEngine:
    def __init__(self, finance: Finance):
        """Create a new engine for the provided ``Finance`` instance."""
        self.finance = finance

    def run_all_strategies(self, budgeting: BudgetingStrategy, debt: DebtStrategy, risk: RiskStrategy):
        """Run each of the supplied strategies against the finance data."""
        budgeting.allocate(self.finance)
        debt.pay_debt(self.finance)
        risk.evaluate(self.finance)

    def summary(self) -> FinanceSummary:
        """Return a ``FinanceSummary`` for the current finance state."""
        return FinanceSummary(
            net_worth=self.finance.total_net_worth(),
            investment_count=len(self.finance.investments),
            debt_count=len(self.finance.debts),
            allocation_count=len(self.finance.allocations)
        )

