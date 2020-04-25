"""empty message

Revision ID: bb8572ebe9cb
Revises: 
Create Date: 2020-04-01 23:26:54.924870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb8572ebe9cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('approved', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('reason', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'verified')
    op.drop_column('users', 'role')
    op.drop_column('users', 'reason')
    op.drop_column('users', 'approved')
    # ### end Alembic commands ###
