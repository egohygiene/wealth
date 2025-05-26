from random import choice, uniform
from typing import List
from uuid import uuid4
from faker import Faker

from wealth.models.investment import Investment
from wealth.models.asset import AssetType
from wealth.models.risk import RiskType, Risk

fake = Faker()

def generate_mock_investment(user_id: str) -> Investment:
    asset_type = choice(list(AssetType))
    risk_level = choice(list(RiskType))
    invested = round(uniform(100, 5000), 2)
    current = round(uniform(invested * 0.5, invested * 1.5), 2)
    risk_score = round(uniform(0.0, 1.0), 2)

    return Investment(
        uuid=str(uuid4()),
        user_id=user_id,
        name=f"{asset_type.value.title()} Investment in {fake.company()}",
        description=fake.catch_phrase(),
        asset_type=asset_type,
        amount_invested=invested,
        current_value=current,
        platform=fake.domain_name(),
        risk_score=risk_score,
        risk_level=risk_level,
        risk=Risk(
            name=f"{asset_type.value.title()} Risk",
            score=risk_score,
            level=risk_level,
            description="Mocked investment risk"
        ),
        notes=fake.text()
    )

def generate_mock_investment_list(user_id: str, count: int = 4) -> List[Investment]:
    return [generate_mock_investment(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_investment(test_user_id)
    print(sample.to_json(indent=2))
