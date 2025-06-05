from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from sqlmodel import SQLModel, Field, create_engine, Session


class WealthSQLModel(SQLModel):
    """Base fields shared across models."""

    uuid: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    user_id: str
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None
    notes: Optional[str] = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AllocationModel(WealthSQLModel, table=True):
    __tablename__ = "allocations"

    allocation_type: str
    budget_amount: Optional[float] = None
    budget_percentage: Optional[float] = None
    savings_bucket: Optional[str] = None
    risk_score: float = 0.0
    risk_level: str = "low"
    active: bool = True

    @classmethod
    def from_pydantic(cls, allocation: "Allocation") -> "AllocationModel":
        return cls.model_validate(allocation.model_dump())


class InvestmentModel(WealthSQLModel, table=True):
    __tablename__ = "investments"

    asset_type: str
    amount_invested: float = 0.0
    current_value: float = 0.0
    platform: Optional[str] = None
    risk_score: float = 0.0
    risk_level: str = "medium"

    @classmethod
    def from_pydantic(cls, investment: "Investment") -> "InvestmentModel":
        return cls.model_validate(investment.model_dump())


def create_db_and_tables(engine):
    """Create tables for all SQLModel models."""
    SQLModel.metadata.create_all(engine)


__all__ = [
    "SQLModel",
    "Session",
    "create_engine",
    "create_db_and_tables",
    "AllocationModel",
    "InvestmentModel",
    "WealthSQLModel",
]
