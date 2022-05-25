"""empty message

Revision ID: 033bf0f2eaef
Revises: c5ed1c306f59
Create Date: 2022-05-25 15:14:41.470270

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "033bf0f2eaef"
down_revision = "c5ed1c306f59"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "status",
        sa.Column("created_utc", sa.DateTime(timezone=True), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("message", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("status")
    # ### end Alembic commands ###
