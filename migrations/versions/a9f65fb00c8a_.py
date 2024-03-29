"""empty message

Revision ID: a9f65fb00c8a
Revises: f848efc9ecec
Create Date: 2020-09-22 02:10:42.095540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9f65fb00c8a'
down_revision = 'f848efc9ecec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'admin_name')
    op.drop_column('news', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.add_column('news', sa.Column('admin_name', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
