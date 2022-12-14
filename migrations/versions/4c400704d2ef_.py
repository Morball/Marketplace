"""empty message

Revision ID: 4c400704d2ef
Revises: 67319b88660d
Create Date: 2022-08-17 18:31:25.070872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c400704d2ef'
down_revision = '67319b88660d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('vendor', sa.String(length=80), nullable=True))
    op.add_column('review', sa.Column('experience', sa.String(length=80), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'experience')
    op.drop_column('review', 'vendor')
    # ### end Alembic commands ###
