from pydantic import Field
from typing import Optional, List, Dict, Literal
from datetime import datetime
from models.wealth import Wealth

class Allocation(Wealth):
    allocation_type: Literal["fixed", "variable"]
    budget_amount: Optional[float] = None
    budget_percentage: Optional[float] = None
    savings_bucket: Optional[str] = None
    risk: float = 0.0
    risk_level: Optional[Literal["low", "medium", "high"]] = None
    services: List[Dict[str, str]] = []
    emotional_context: List[str] = []
    goals: List[Dict[str, Optional[float]]] = []

    def set_risk_level(self):
        if self.risk < 0.3:
            self.risk_level = "low"
        elif self.risk < 0.7:
            self.risk_level = "medium"
        else:
            self.risk_level = "high"
