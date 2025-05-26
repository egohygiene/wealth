import pytest
from wealth.mock import generate_mock_finance
from wealth.core.finance import Finance

# 🔧 Fixture to generate a mock Finance object
@pytest.fixture
def mock_finance() -> Finance:
    """Returns a full mock Finance object using test-user-001."""
    return generate_mock_finance(user_id="test-user-001")

# Optional: You can use this to generate a clean UUID for test separation
@pytest.fixture
def user_id() -> str:
    return "test-user-001"
