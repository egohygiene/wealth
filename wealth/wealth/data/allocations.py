from uuid import uuid4
from datetime import datetime

from wealth.core.finance import Finance
from wealth.models.allocation import Allocation, AllocationType
from wealth.models.risk import Risk, RiskType

def create_default_allocations(finance: Finance) -> list[Allocation]:
    """Return a list of example ``Allocation`` records for the given finance."""
    # 2. Create the AAA Membership Allocation
    aaa_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
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
        user_id=finance.user_id,
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

    # Books/Movie Rentals – $0
    books_movies_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Books/Movie Rentals",
        description="Inactive placeholder for occasional media purchases or rentals",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Discretionary",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Books/Movies Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Inactive until purchases are tracked"
        ),
        tags=["entertainment", "media"],
        notes="Consider reactivating if recurring movie or book expenses arise",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Cable TV – $0
    cable_tv_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Cable TV",
        description="Currently unused. Placeholder for traditional cable services.",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Utilities",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Cable TV Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="No active cable subscription"
        ),
        tags=["utilities", "media"],
        notes="Revisit only if a cable service is subscribed",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Car Insurance – $1600/year → ~$133.33/month
    car_insurance_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Car Insurance",
        description="Annual premium split monthly",
        allocation_type=AllocationType.FIXED,
        budget_amount=133.33,
        savings_bucket="Auto",
        risk_score=0.3,
        risk_level=RiskType.LOW,
        risk=Risk(
            name="Car Insurance Risk",
            score=0.3,
            level=RiskType.LOW,
            description="Necessary vehicle insurance, recurring annually"
        ),
        tags=["auto", "insurance"],
        notes="Reevaluate premiums and provider each renewal period",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=True
    )

    # Car Repairs/Maintenance – $600/year = $50/month
    car_maintenance_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Car Repairs/Maintenance",
        description="Maintenance and repair budget for vehicle upkeep",
        allocation_type=AllocationType.FIXED,
        budget_amount=50.00,
        savings_bucket="Auto",
        risk_score=0.4,
        risk_level=RiskType.MEDIUM,
        risk=Risk(
            name="Car Maintenance Risk",
            score=0.4,
            level=RiskType.MEDIUM,
            description="Variable maintenance costs, potential unexpected repairs"
        ),
        tags=["auto", "maintenance"],
        notes="Includes oil changes, inspections, and minor repairs",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=True
    )

    # Cellular Phone – $1200/year = $100/month
    cell_phone_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Cellular Phone",
        description="Monthly phone bill (e.g. Google Fi, Verizon)",
        allocation_type=AllocationType.FIXED,
        budget_amount=100.00,
        savings_bucket="Utilities",
        risk_score=0.1,
        risk_level=RiskType.LOW,
        risk=Risk(
            name="Cell Phone Risk",
            score=0.1,
            level=RiskType.LOW,
            description="Recurring mobile service expense"
        ),
        tags=["phone", "communication"],
        notes="Adjust if changing plans or providers",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=True
    )

    # Child Support – $0
    child_support_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Child Support",
        description="Placeholder for potential legal child support obligations",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Legal/Family",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Child Support Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Currently inactive; can be activated if needed"
        ),
        tags=["legal", "family"],
        notes="Inactive until triggered by custody or court process",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Children’s Nanny – $0
    nanny_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Children’s Nanny",
        description="Nanny or in-home childcare support",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Family",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Nanny Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Not in use unless full/part-time nanny is hired"
        ),
        tags=["children", "care", "support"],
        notes="Adjust when nanny services are needed",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Children’s School Lunch – $0
    school_lunch_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Children’s School Lunch",
        description="School lunch payments or meal account refills",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Family",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="School Lunch Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Inactive unless enrolled in meal plans"
        ),
        tags=["children", "school", "meals"],
        notes="Enable when child enrolls in a school with paid lunch",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Children’s Summer Camp – $0
    summer_camp_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Children’s Summer Camp",
        description="Seasonal camp expenses for children",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Education/Enrichment",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Summer Camp Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Only enabled when child is registered for summer programs"
        ),
        tags=["children", "enrichment", "seasonal"],
        notes="Set cost based on summer schedule",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    # Donations – $0
    donations_allocation = Allocation(
        uuid=str(uuid4()),
        user_id=finance.user_id,
        name="Donations",
        description="Placeholder for charitable giving and donations",
        allocation_type=AllocationType.FIXED,
        budget_amount=0.00,
        savings_bucket="Giving",
        risk_score=0.0,
        risk_level=RiskType.GUARANTEED,
        risk=Risk(
            name="Donations Risk",
            score=0.0,
            level=RiskType.GUARANTEED,
            description="Inactive unless regular donations are made"
        ),
        tags=["charity", "donations", "giving"],
        notes="Can be enabled when setting up recurring donations (e.g. DonorBox, ShareTheMeal)",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_active=False
    )

    allocations: list[Allocation] = [
        aaa_allocation,
        accountant_allocation,
        alarm_allocation,
        alimony_allocation,
        attorney_allocation,
        barber_allocation,
        books_movies_allocation,
        cable_tv_allocation,
        car_insurance_allocation,
        car_maintenance_allocation,
        cell_phone_allocation,
        child_support_allocation,
        nanny_allocation,
        school_lunch_allocation,
        summer_camp_allocation,
        donations_allocation
    ]

    return allocations
