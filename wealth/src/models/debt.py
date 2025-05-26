from pydantic import BaseModel
from typing import Optional

class Debt(BaseModel):
    name: str
    balance: float
    apr: float  # interest rate
    min_payment: float
    snowball_priority: int
    notes: Optional[str] = None
