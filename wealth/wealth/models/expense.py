from enum import Enum, unique
from pydantic import Field
from datetime import datetime, timezone

from wealth.models.wealth import Wealth

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

@unique
class ExpenseFrequency(str, Enum):
    ONE_TIME = "one_time"
    DAILY = "daily"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    SEMIMONTHLY = "semimonthly"
    MONTHLY = "monthly"
    BIMONTHLY = "bimonthly"
    QUARTERLY = "quarterly"
    SEMIANNUALLY = "semiannually"
    ANNUALLY = "annually"
    IRREGULAR = "irregular"

class Expense(Wealth):
    amount: float = Field(..., description="The cost of the expense")
    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="The date the expense occurred")
    category: ExpenseCategory = Field(default=ExpenseCategory.OTHER, description="Type of expense for reporting and analysis")
    frequency: ExpenseFrequency = Field(default=ExpenseFrequency.ONE_TIME, description="How often this expense recurs")
    source_account: str = Field(..., description="Bank or account from which the payment was made")
