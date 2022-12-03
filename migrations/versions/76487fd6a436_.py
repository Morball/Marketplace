"""empty message

Revision ID: 76487fd6a436
Revises: 57a3bdbb1559
Create Date: 2022-08-17 00:22:34.385952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76487fd6a436'
down_revision = '57a3bdbb1559'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listing', sa.Column('listedAt', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('listing', 'listedAt')
    # ### end Alembic commands ###
