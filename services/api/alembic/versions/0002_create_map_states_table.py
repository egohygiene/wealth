"""create map_states table"""

from alembic import op
import sqlalchemy as sa

revision = "0002_create_map_states_table"
down_revision = "0001_create_messages_table"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "map_states",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.String(), sa.ForeignKey("users.id"), nullable=False),
        sa.Column("state", sa.JSON(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )



def downgrade() -> None:
    op.drop_table("map_states")
