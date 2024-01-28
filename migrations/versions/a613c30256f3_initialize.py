"""initialize

Revision ID: a613c30256f3
Revises: 
Create Date: 2024-01-26 17:49:48.337473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a613c30256f3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='orders_pkey')
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name='products_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='products_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    op.drop_table('products')
    op.drop_table('orders')
    # ### end Alembic commands ###
