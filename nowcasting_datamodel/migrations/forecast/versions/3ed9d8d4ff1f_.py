"""empty message

Revision ID: 3ed9d8d4ff1f
Revises: 848c1673e7be
Create Date: 2022-09-21 08:25:53.202001

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "3ed9d8d4ff1f"
down_revision = "848c1673e7be"
branch_labels = None
depends_on = None


def upgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "forecast_value",
        sa.Column(
            "uuid", postgresql.UUID(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
    )
    op.alter_column(
        "forecast_value",
        "target_time",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
    )
    op.drop_column("forecast_value", "id")

    # SQL commands to make partition tables

    # 1. make new forecast_value_new table
    # CREATE TABLE forecast_value_new (
    #         created_utc TIMESTAMP WITH TIME ZONE,
    #         uuid UUID DEFAULT gen_random_uuid() NOT NULL,
    #         target_time TIMESTAMP WITH TIME ZONE NOT NULL,
    #         expected_power_generation_megawatts FLOAT,
    #         forecast_id INTEGER,
    #         PRIMARY KEY (uuid, target_time),
    #         FOREIGN KEY(forecast_id) REFERENCES forecast (id)
    # )
    #  PARTITION BY RANGE(target_time)

    # 2. Make partitions tables
    # ALTER TABLE forecast_value
    #       ATTACH PARTITION forecast_value_2020_01
    #       FOR VALUES FROM ('2020_01-01') TO ('2020_02-01');

    # 3. Rename forecast_value table to forecast_value_old
    # ALTER TABLE forecast_value RENAME TO forecast_value_old

    # 4. Rename forecast_value_new table to forecast_value
    # ALTER TABLE forecast_value_new RENAME TO forecast_value

    # ### end Alembic commands ###


def downgrade():  # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "forecast_value", sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False)
    )
    op.alter_column(
        "forecast_value",
        "target_time",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
    )
    op.drop_column("forecast_value", "uuid")
    # ### end Alembic commands ###

    # to remove partition table

    # 1. Rename forecast_value table to forecast_value_new
    # ALTER TABLE forecast_value RENAME TO forecast_value_new

    # 2. Rename forecast_value_old table to forecast_value
    # ALTER TABLE forecast_value_old RENAME TO forecast_value

    # 3. Drop table 'forecast_value_new'
    # DROP TABLE forecast_value_new
