"""create users and map_states tables"""

from alembic import op
import sqlalchemy as sa

revision = "0002_create_map_states_table"
down_revision = "0001_create_messages_table"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("preferred_username", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
    )

    op.add_column("messages", sa.Column("user_id", sa.String(), nullable=False))
    op.create_foreign_key(None, "messages", "users", ["user_id"], ["id"])

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
    op.drop_constraint(None, "messages", type_="foreignkey")
    op.drop_column("messages", "user_id")
    op.drop_table("users")
