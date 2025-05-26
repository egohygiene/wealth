from typing import Optional
from pydantic import Field
from enum import Enum, unique

from wealth.models.wealth import Wealth
from wealth.models.risk import Risk, RiskType

@unique
class DebtType(str, Enum):
    CREDIT_CARD = "credit_card"
    PERSONAL_LOAN = "personal_loan"
    STUDENT_LOAN = "student_loan"
    AUTO_LOAN = "auto_loan"
    MORTGAGE = "mortgage"
    MEDICAL = "medical"
    BUSINESS_LOAN = "business_loan"
    LINE_OF_CREDIT = "line_of_credit"
    BUY_NOW_PAY_LATER = "buy_now_pay_later"
    OTHER = "other"

@unique
class DebtStatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    DEFAULTED = "defaulted"
    DEFERRED = "deferred"
    PAID_OFF = "paid_off"

class Debt(Wealth):
    debt_type: DebtType = Field(default=DebtType.OTHER, description="Type of debt or liability")
    status: DebtStatus = Field(default=DebtStatus.OPEN, description="Current payment status of the debt")
    balance: float = Field(..., description="Remaining balance of the debt")
    apr: float = Field(..., description="Annual percentage rate (interest rate)")
    min_payment: float = Field(..., description="Minimum monthly payment required")
    snowball_priority: Optional[int] = Field(default=None, description="Custom priority value for debt payoff strategy")
    risk_score: float = Field(default=0.0, ge=0.0, le=1.0, description="Numeric score indicating repayment risk")
    risk_level: RiskType = Field(default=RiskType.MEDIUM, description="Overall classification of repayment risk")
    risk: Optional[Risk] = Field(default=None, description="Optional structured Risk object")
    lender: Optional[str] = Field(default=None, description="Name of the lender or institution")
    account_number: Optional[str] = Field(default=None, description="(Optional) masked or hashed account reference")
    due_day: Optional[int] = Field(default=None, ge=1, le=31, description="Day of the month payment is typically due")
    is_tax_deductible: bool = Field(default=False, description="Whether interest paid is tax deductible")
    auto_pay_enabled: bool = Field(default=False, description="Whether automatic payment is enabled")
    notes: Optional[str] = None
