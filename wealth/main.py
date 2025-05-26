from uuid import uuid4
from datetime import datetime

from wealth.core.finance import Finance
from wealth.models.allocation import Allocation, AllocationType
from wealth.models.risk import Risk, RiskType

# 1. Create your user and Finance system
user_id = str(uuid4())
user_name = "Alan Szmyt"

finance = Finance.default(user_id=user_id, notes=f"{user_name}'s system initialized.")


# 2. Create the AAA Membership Allocation
aaa_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=user_id,  # will get overwritten by `add_allocation` if omitted
    name="AAA Membership",
    description="Yearly AAA Membership fee ($108) paid monthly",
    allocation_type=AllocationType.FIXED,
    budget_amount=9.00,
    savings_bucket="Subscriptions",
    risk_score=0.1,
    risk_level=RiskType.LOW,
    risk=Risk(
        name="AAA Membership",
        score=0.1,
        level=RiskType.LOW,
        description="Low-risk, recurring annual auto-renewal"
    ),
    tags=["car", "insurance", "emergency"],
    notes="Review every December before auto-renewal",
    created_at=datetime.now(),
    updated_at=datetime.now(),
)

# 3. Add allocation to the system
finance.add_allocation(aaa_allocation)

# 4. Output the result
print(finance.to_json(indent=2))

finance.plot_allocation_chart(show=True, save_path="output/allocation_chart.png")
