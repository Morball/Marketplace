"""empty message

Revision ID: 2418ebd77b09
Revises: 427187a8ae45
Create Date: 2022-08-17 18:45:33.259013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2418ebd77b09'
down_revision = '427187a8ae45'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('listing', sa.Column('vendor', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('listing', 'vendor')
    # ### end Alembic commands ###
