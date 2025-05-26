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

accountant_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=finance.user_id,  # will be overwritten by add_allocation
    name="Accountant",
    description="TurboTax Premier or similar service (~$240/year split monthly)",
    allocation_type=AllocationType.FIXED,
    budget_amount=20.00,
    savings_bucket="Subscriptions",
    risk_score=0.15,
    risk_level=RiskType.LOW,
    risk=Risk(
        name="Accountant Subscription Risk",
        score=0.15,
        level=RiskType.LOW,
        description="Annual tax prep fee, relatively stable and predictable"
    ),
    tags=["taxes", "professional", "subscriptions"],
    notes="Paid annually, can change if switching software or going full CPA",
    created_at=datetime.now(),
    updated_at=datetime.now()
)

# Alarm System (Arlo) - $300/year = $25/month
alarm_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=finance.user_id,
    name="Alarm System (Arlo)",
    description="Annual subscription for Arlo home security",
    allocation_type=AllocationType.FIXED,
    budget_amount=25.00,
    savings_bucket="Fixed Expenses",
    risk_score=0.1,
    risk_level=RiskType.LOW,
    risk=Risk(
        name="Alarm System Risk",
        score=0.1,
        level=RiskType.LOW,
        description="Stable, recurring subscription for home security"
    ),
    tags=["home", "security"],
    notes="Paid annually, currently using Arlo",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    is_active=True
)

# Alimony - $0
alimony_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=finance.user_id,
    name="Alimony",
    description="Placeholder for potential future alimony",
    allocation_type=AllocationType.FIXED,
    budget_amount=0.00,
    savings_bucket="Fixed Expenses",
    risk_score=0.0,
    risk_level=RiskType.GUARANTEED,
    risk=Risk(
        name="Alimony Risk",
        score=0.0,
        level=RiskType.GUARANTEED,
        description="Inactive allocation for future use"
    ),
    tags=["legal", "family"],
    notes="Inactive until applicable",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    is_active=False
)

# Attorney - $0
attorney_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=finance.user_id,
    name="Attorney",
    description="Placeholder for future legal services or consultations",
    allocation_type=AllocationType.FIXED,
    budget_amount=0.00,
    savings_bucket="Fixed Expenses",
    risk_score=0.0,
    risk_level=RiskType.GUARANTEED,
    risk=Risk(
        name="Attorney Risk",
        score=0.0,
        level=RiskType.GUARANTEED,
        description="Currently inactive, will be activated if needed"
    ),
    tags=["legal", "planning"],
    notes="Inactive until legal services are required",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    is_active=False
)

# Barber/Hairdresser - $420/year = $35/month
barber_allocation = Allocation(
    uuid=str(uuid4()),
    user_id=finance.user_id,
    name="Barber/Hairdresser",
    description="Estimated cost for haircuts, beard trims, and grooming",
    allocation_type=AllocationType.FIXED,
    budget_amount=35.00,
    savings_bucket="Fixed Expenses",
    risk_score=0.2,
    risk_level=RiskType.LOW,
    risk=Risk(
        name="Barber Risk",
        score=0.2,
        level=RiskType.LOW,
        description="Recurring personal care expense"
    ),
    tags=["grooming", "personal_care"],
    notes="Based on $420/year estimation",
    created_at=datetime.now(),
    updated_at=datetime.now(),
    is_active=True
)

allocations: list[Allocation] = [
    aaa_allocation,
    accountant_allocation,
    alarm_allocation,
    alimony_allocation,
    attorney_allocation,
    barber_allocation
]

# 3. Add allocations to the system
finance.add_allocations(allocations)

# 4. Output the result
print(finance.to_json(indent=2))

finance.plot_allocation_chart(show=True, save_path="output/allocation_chart.png")
