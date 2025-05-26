from enum import Enum, unique
from pydantic import Field
from datetime import datetime, timezone

from wealth.models.wealth import Wealth
from wealth.models.frequency import Frequency

@unique
class ExpenseCategory(str, Enum):
    HOUSING = "housing"
    UTILITIES = "utilities"
    GROCERIES = "groceries"
    TRANSPORTATION = "transportation"
    HEALTHCARE = "healthcare"
    INSURANCE = "insurance"
    ENTERTAINMENT = "entertainment"
    SUBSCRIPTIONS = "subscriptions"
    EDUCATION = "education"
    CHILDCARE = "childcare"
    PETS = "pets"
    CHARITY = "charity"
    PERSONAL_CARE = "personal_care"
    GIFTS = "gifts"
    BUSINESS = "business"
    TAXES = "taxes"
    LOANS = "loans"
    DEBT_REPAYMENT = "debt_repayment"
    INVESTMENT = "investment"
    OTHER = "other"

class Expense(Wealth):
    amount: float = Field(..., description="The cost of the expense")
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="The date the expense occurred")
    category: ExpenseCategory = Field(default=ExpenseCategory.OTHER, description="Type of expense for reporting and analysis")
    frequency: Frequency = Field(default=Frequency.ONE_TIME, description="How often this expense recurs")
    source_account: str = Field(..., description="Bank or account from which the payment was made")
