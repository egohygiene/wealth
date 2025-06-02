from abc import ABC, abstractmethod
from wealth.core.finance import Finance

# 💼 Budgeting Strategy Interface
class BudgetingStrategy(ABC):
    @abstractmethod
    def allocate(self, finance: Finance):
        """Allocate funds within the provided ``Finance`` instance."""
        pass

# 💳 Debt Strategy Interface
class DebtStrategy(ABC):
    @abstractmethod
    def pay_debt(self, finance: Finance):
        """Apply a debt payment strategy to the ``Finance`` object."""
        pass

# 🔥 Risk Evaluation Strategy
class RiskStrategy(ABC):
    @abstractmethod
    def evaluate(self, finance: Finance):
        """Evaluate risk for the given ``Finance`` instance."""
        pass
