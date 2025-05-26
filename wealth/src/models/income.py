from pydantic import BaseModel
from typing import Literal

class Income(BaseModel):
    source: str
    amount: float
    frequency: Literal["monthly", "weekly", "annually"] = "monthly"
    type: Literal["active", "passive", "side-hustle", "business"] = "active"
