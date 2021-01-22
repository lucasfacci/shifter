"""empty message

Revision ID: 7a8d8720fda5
Revises: a9f65fb00c8a
Create Date: 2020-09-22 02:13:16.063134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8d8720fda5'
down_revision = 'a9f65fb00c8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'news', type_='foreignkey')
    op.create_foreign_key(None, 'news', 'admins', ['admin_name'], ['name'])
    op.drop_column('news', 'admin_id')
    op.drop_column('news', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.add_column('news', sa.Column('admin_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'news', type_='foreignkey')
    op.create_foreign_key(None, 'news', 'admins', ['admin_id'], ['id'])
    # ### end Alembic commands ###