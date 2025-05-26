from pydantic import Field
from typing import Optional
from datetime import datetime
from models.wealth import Wealth

class Expense(Wealth):
    amount: float
    date: datetime = Field(default_factory=datetime.utcnow)
    source_account: Optional[str] = None
