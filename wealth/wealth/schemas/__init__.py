import json
from importlib.resources import files
from typing import Any, Dict

from jsonschema import validate
from jsonschema.validators import Draft7Validator

from wealth.core.finance import Finance


SCHEMA_FILE = "wealth.schema.json"


def load_schema() -> Dict[str, Any]:
    """Load the bundled wealth JSON schema."""
    path = files(__package__) / SCHEMA_FILE
    return json.loads(path.read_text())


def validate_finance(finance: Finance) -> None:
    """Validate a ``Finance`` model against the JSON schema."""
    schema = load_schema()
    validate(
        instance=finance.model_dump(),
        schema=schema,
        format_checker=Draft7Validator.FORMAT_CHECKER,
    )
