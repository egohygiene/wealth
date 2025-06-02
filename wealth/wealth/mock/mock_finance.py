from uuid import uuid4

from wealth.core.finance import Finance
from wealth.models.lifecycle import LifecyclePhase
from wealth.models.risk import RiskProfile

from wealth.mock.mock_income import generate_mock_income_list
from wealth.mock.mock_expense import generate_mock_expense_list
from wealth.mock.mock_allocation import generate_mock_allocation_list
from wealth.mock.mock_investment import generate_mock_investment_list
from wealth.mock.mock_debt import generate_mock_debt_list
from wealth.mock.mock_portfolio import generate_mock_portfolio_list
from wealth.mock.mock_services import generate_mock_service_list

def generate_mock_finance(user_id: str | None = None) -> Finance:
    """Assemble a ``Finance`` object populated with mock data."""
    user_id = user_id or str(uuid4())

    return Finance(
        user_id=user_id,
        allocations=generate_mock_allocation_list(user_id),
        expenses=generate_mock_expense_list(user_id),
        income_streams=generate_mock_income_list(user_id),
        debts=generate_mock_debt_list(user_id),
        investments=generate_mock_investment_list(user_id),
        portfolios=generate_mock_portfolio_list(user_id),
        services=generate_mock_service_list(user_id),
        lifecycle_phase=LifecyclePhase.STABILIZING,
        risk_profile=RiskProfile.BALANCED,
        roles=["freelancer", "parent"],
        features=["budgeting", "debt_tracking", "investment_dashboard"],
        notes="This is a mocked financial profile for testing and prototyping."
    )

# 🧪 Standalone test
if __name__ == "__main__":
    mock_finance = generate_mock_finance()
    print(mock_finance.to_json(indent=4))
