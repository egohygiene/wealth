from sqlmodel import create_engine, Session, select
from wealth.db import AllocationModel, InvestmentModel, create_db_and_tables
from wealth.mock import generate_mock_finance


def test_allocation_sqlmodel_roundtrip():
    finance = generate_mock_finance("sqlmodel-user")
    alloc = finance.allocations[0]
    model = AllocationModel.from_pydantic(alloc)

    engine = create_engine("sqlite:///:memory:")
    create_db_and_tables(engine)

    with Session(engine) as session:
        session.add(model)
        session.commit()
        result = session.exec(select(AllocationModel)).first()

    assert result
    assert result.uuid == alloc.uuid
    assert result.user_id == alloc.user_id
