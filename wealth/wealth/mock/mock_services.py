from uuid import uuid4
from typing import List
from faker import Faker
from pydantic import HttpUrl

from wealth.models.services import Service

fake = Faker()

def generate_mock_service(user_id: str) -> Service:
    """Return a mocked ``Service`` instance."""
    company = fake.company()
    return Service(
        uuid=str(uuid4()),
        name=company,
        url=HttpUrl(f"https://{fake.domain_name()}"),
        logo_url=HttpUrl(f"https://logo.clearbit.com/{fake.domain_name()}"),
        provider=company,
        notes=fake.sentence()
    )

def generate_mock_service_list(user_id: str, count: int = 3) -> List[Service]:
    """Create multiple mocked services."""
    return [generate_mock_service(user_id) for _ in range(count)]

# 🧪 Standalone test
if __name__ == "__main__":
    test_user_id = "test-user-001"
    sample = generate_mock_service(test_user_id)
    print(sample.to_json(indent=2))
