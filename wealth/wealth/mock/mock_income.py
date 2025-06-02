from random import choice, uniform
from typing import List
from uuid import uuid4
from faker import Faker

from wealth.models.income import Income, IncomeType, IncomeFrequency

fake = Faker()

def generate_mock_income(user_id: str) -> Income:
    """Generate a random ``Income`` entry."""
    income_type = choice(list(IncomeType))
    frequency = choice(list(IncomeFrequency))
    source_name = fake.company()

    return Income(
        uuid=str(uuid4()),
        user_id=user_id,
        name=f"{income_type.value.title()} from {source_name}",
        source=source_name,
        amount=round(uniform(300, 10000), 2),
        frequency=frequency,
        type=income_type,
        description=fake.sentence(),
        notes=fake.paragraph()
    )

def generate_mock_income_list(user_id: str, count: int = 2) -> List[Income]:
    """Return a list of mocked income streams."""
    return [generate_mock_income(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_income(test_user_id)
    print(sample.to_json(indent=2))
