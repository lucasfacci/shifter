"""empty message

Revision ID: c1c59223435f
Revises: a355faf18abb
Create Date: 2020-09-14 20:47:07.430438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1c59223435f'
down_revision = 'a355faf18abb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'subtitle')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('subtitle', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###