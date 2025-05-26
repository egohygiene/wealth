from abc import ABC, abstractmethod
from wealth.core.finance import Finance

# 💼 Budgeting Strategy Interface
class BudgetingStrategy(ABC):
    @abstractmethod
    def allocate(self, finance: Finance):
        pass

# 💳 Debt Strategy Interface
class DebtStrategy(ABC):
    @abstractmethod
    def pay_debt(self, finance: Finance):
        pass

# 🔥 Risk Evaluation Strategy
class RiskStrategy(ABC):
    @abstractmethod
    def evaluate(self, finance: Finance):
        pass
