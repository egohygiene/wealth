from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Optional, List, Any
from uuid import uuid4
import pandas as pd

class Wealth(BaseModel):
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    notes: Optional[str] = None
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    def update_timestamp(self):
        """Refresh the ``updated_at`` timestamp to the current time."""
        self.updated_at = datetime.now(timezone.utc)

    def __str__(self):
        """Return a readable representation of the wealth object."""
        return f"Wealth<{self.name} | {self.user_id}>"

    def __repr__(self):
        """Return the ``str`` representation for debugging."""
        return self.__str__()

    def to_dict(self):
        """Serialize the model to a ``dict``."""
        return self.model_dump()

    def to_json(self, indent: Optional[int] = 4, **kwargs: Any):
        """Serialize the model to a JSON string."""
        return self.model_dump_json(indent=indent, **kwargs)

    def to_dataframe(self) -> pd.DataFrame:
        """Convert the model to a single-row ``DataFrame``."""
        return pd.DataFrame([self.model_dump()])
