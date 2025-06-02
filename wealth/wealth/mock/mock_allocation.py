from random import choice, uniform
from typing import List
from uuid import uuid4
from faker import Faker

from wealth.models.allocation import Allocation, AllocationType
from wealth.models.risk import RiskType, Risk

fake = Faker()

def generate_mock_allocation(user_id: str) -> Allocation:
    """Create a randomized ``Allocation`` instance for testing."""
    allocation_type = choice(list(AllocationType))
    is_fixed = allocation_type == AllocationType.FIXED
    amount = round(uniform(50, 2000), 2) if is_fixed else None
    percentage = round(uniform(1, 20), 2) if not is_fixed else None

    risk_level = choice(list(RiskType))
    risk_score = round(uniform(0.0, 1.0), 2)

    return Allocation(
        uuid=str(uuid4()),
        user_id=user_id,
        name=f"{allocation_type.value.title()} Allocation - {fake.bs().title()}",
        description=fake.sentence(),
        allocation_type=allocation_type,
        budget_amount=amount,
        budget_percentage=percentage,
        savings_bucket=fake.word(),
        risk_score=risk_score,
        risk_level=risk_level,
        risk=Risk(
            name=f"{risk_level.value.title()} Allocation Risk",
            score=risk_score,
            level=risk_level,
            description="Auto-generated mock risk for allocation"
        ),
        tags=[fake.word(), fake.word()],
        notes=fake.paragraph()
    )

def generate_mock_allocation_list(user_id: str, count: int = 3) -> List[Allocation]:
    """Return a list of mocked allocations."""
    return [generate_mock_allocation(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_allocation(test_user_id)
    print(sample.to_json(indent=2))
