from random import choice, uniform
from typing import List
from uuid import uuid4
from faker import Faker

from wealth.models.expense import Expense, ExpenseCategory, ExpenseFrequency

fake = Faker()

def generate_mock_expense(user_id: str) -> Expense:
    """Generate a random ``Expense`` for a user."""
    category = choice(list(ExpenseCategory))
    frequency = choice(list(ExpenseFrequency))
    vendor = fake.company()
    amount = round(uniform(10, 800), 2)
    expense_date = fake.date_time_between(start_date="-60d", end_date="now")

    return Expense(
        uuid=str(uuid4()),
        user_id=user_id,
        name=f"{category.value.title()} expense at {vendor}",
        description=fake.sentence(),
        category=category,
        frequency=frequency,
        source_account=fake.iban(),
        amount=amount,
        date=expense_date,
        notes=fake.paragraph()
    )

def generate_mock_expense_list(user_id: str, count: int = 5) -> List[Expense]:
    """Return a list of mocked expenses."""
    return [generate_mock_expense(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_expense(test_user_id)
    print(sample.to_json(indent=2))
