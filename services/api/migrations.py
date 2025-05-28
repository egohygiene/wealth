import asyncio
from pathlib import Path

from alembic import command
from alembic.config import Config

from .database import get_database_url


def run_migrations() -> None:
    alembic_cfg = Config(str(Path(__file__).with_name("alembic.ini")))
    alembic_cfg.set_main_option("sqlalchemy.url", get_database_url())
    command.upgrade(alembic_cfg, "head")


async def run_migrations_async() -> None:
    await asyncio.to_thread(run_migrations)
