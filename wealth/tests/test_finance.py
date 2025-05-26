from wealth.core.engine import FinanceEngine
from wealth.core.finance import Finance

def test_finance_structure(mock_finance: Finance):
    """Validate that the mock Finance object loads correctly and has all core fields."""
    assert mock_finance.user_id == "test-user-001"
    assert isinstance(mock_finance.allocations, list)
    assert isinstance(mock_finance.income_streams, list)
    assert isinstance(mock_finance.expenses, list)
    assert isinstance(mock_finance.investments, list)
    assert isinstance(mock_finance.debts, list)
    assert isinstance(mock_finance.portfolios, list)
    assert mock_finance.lifecycle_phase
    assert mock_finance.risk_profile

def test_net_worth_calculation(mock_finance: Finance):
    """Ensure that net worth can be calculated without error."""
    net_worth = mock_finance.total_net_worth()
    assert isinstance(net_worth, float)

def test_finance_engine_summary(mock_finance: Finance):
    """Test the FinanceEngine summary method."""
    engine = FinanceEngine(mock_finance)
    summary = engine.summary()
    assert summary.net_worth == mock_finance.total_net_worth()
    assert summary.investment_count == len(mock_finance.investments)
    assert summary.debt_count == len(mock_finance.debts)
