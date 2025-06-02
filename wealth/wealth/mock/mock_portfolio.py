from uuid import uuid4
from random import choice
from typing import List
from faker import Faker

from wealth.models.portfolio import Portfolio
from wealth.models.risk import RiskProfile
from wealth.mock.mock_investment import generate_mock_investment_list

fake = Faker()

def generate_mock_portfolio(user_id: str, count: int = 1) -> Portfolio:
    """Create a portfolio with a set of random investments."""
    portfolio_id = str(uuid4())
    investments = generate_mock_investment_list(user_id=user_id, count=4)
    name = f"{choice(['Core', 'Growth', 'Speculative'])} Portfolio - {fake.word().capitalize()}"

    return Portfolio(
        uuid=portfolio_id,
        user_id=user_id,
        name=name,
        description=fake.sentence(),
        risk_profile=RiskProfile.BALANCED,
        investments=investments,
        strategy_label="Long-term growth",
        notes=fake.paragraph()
    )

def generate_mock_portfolio_list(user_id: str, count: int = 2) -> List[Portfolio]:
    """Return multiple mocked portfolios."""
    return [generate_mock_portfolio(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_portfolio(test_user_id)
    print(sample.to_json(indent=2))
