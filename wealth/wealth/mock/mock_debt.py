from random import choice, uniform, randint
from typing import List
from uuid import uuid4
from faker import Faker

from wealth.models.debt import Debt, DebtType, DebtStatus
from wealth.models.risk import RiskType, Risk

fake = Faker()

def generate_mock_debt(user_id: str) -> Debt:
    debt_type = choice(list(DebtType))
    risk_level = choice(list(RiskType))
    status = choice(list(DebtStatus))
    balance = round(uniform(100, 20000), 2)
    apr = round(uniform(2.0, 25.0), 2)
    min_payment = round(balance * uniform(0.01, 0.05), 2)
    risk_score = round(uniform(0.0, 1.0), 2)

    return Debt(
        uuid=str(uuid4()),
        user_id=user_id,
        name=f"{debt_type.value.replace('_', ' ').title()} with {fake.company()}",
        description=fake.sentence(),
        debt_type=debt_type,
        status=status,
        balance=balance,
        apr=apr,
        min_payment=min_payment,
        snowball_priority=randint(1, 5),
        risk_score=risk_score,
        risk_level=risk_level,
        risk=Risk(
            name=f"{debt_type.value.title()} Risk",
            score=risk_score,
            level=risk_level,
            description="Mocked risk profile for debt"
        ),
        lender=fake.company(),
        account_number=fake.bban(),
        due_day=randint(1, 28),
        is_tax_deductible=choice([True, False]),
        auto_pay_enabled=choice([True, False]),
        notes=fake.paragraph()
    )

def generate_mock_debt_list(user_id: str, count: int = 3) -> List[Debt]:
    return [generate_mock_debt(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_debt(test_user_id)
    print(sample.to_json(indent=2))
