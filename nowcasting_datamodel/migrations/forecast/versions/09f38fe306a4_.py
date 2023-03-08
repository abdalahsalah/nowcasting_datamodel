"""empty message

Revision ID: 09f38fe306a4
Revises: 155dcbad36df
Create Date: 2023-03-08 11:57:23.566779

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '09f38fe306a4'
down_revision = '155dcbad36df'
branch_labels = None
depends_on = None


def upgrade(): # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecast_value', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2022_08', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2022_09', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2022_10', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2022_11', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2022_12', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_01', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_02', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_03', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_04', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_05', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_06', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_07', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_08', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_09', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_10', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_11', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_2023_12', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_last_seven_days', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_latest', sa.Column('adjust_mw', sa.Float(), nullable=True))
    op.add_column('forecast_value_old', sa.Column('adjust_mw', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade(): # noqa
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forecast_value_old', 'adjust_mw')
    op.drop_column('forecast_value_latest', 'adjust_mw')
    op.drop_column('forecast_value_last_seven_days', 'adjust_mw')
    op.drop_column('forecast_value_2023_12', 'adjust_mw')
    op.drop_column('forecast_value_2023_11', 'adjust_mw')
    op.drop_column('forecast_value_2023_10', 'adjust_mw')
    op.drop_column('forecast_value_2023_09', 'adjust_mw')
    op.drop_column('forecast_value_2023_08', 'adjust_mw')
    op.drop_column('forecast_value_2023_07', 'adjust_mw')
    op.drop_column('forecast_value_2023_06', 'adjust_mw')
    op.drop_column('forecast_value_2023_05', 'adjust_mw')
    op.drop_column('forecast_value_2023_04', 'adjust_mw')
    op.drop_column('forecast_value_2023_03', 'adjust_mw')
    op.drop_column('forecast_value_2023_02', 'adjust_mw')
    op.drop_column('forecast_value_2023_01', 'adjust_mw')
    op.drop_column('forecast_value_2022_12', 'adjust_mw')
    op.drop_column('forecast_value_2022_11', 'adjust_mw')
    op.drop_column('forecast_value_2022_10', 'adjust_mw')
    op.drop_column('forecast_value_2022_09', 'adjust_mw')
    op.drop_column('forecast_value_2022_08', 'adjust_mw')
    op.drop_column('forecast_value', 'adjust_mw')
    # ### end Alembic commands ###
