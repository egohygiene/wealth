from wealth.schemas import load_schema, validate_finance
from wealth.mock import generate_mock_finance


def test_load_schema():
    schema = load_schema()
    assert "definitions" in schema


def test_validate_finance(mock_finance):
    validate_finance(mock_finance)
