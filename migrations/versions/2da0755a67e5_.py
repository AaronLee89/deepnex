"""empty message

Revision ID: 2da0755a67e5
Revises: 0d4598c71808
Create Date: 2017-11-03 10:59:32.024000

"""

# revision identifiers, used by Alembic.
revision = '2da0755a67e5'
down_revision = '0d4598c71808'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('poster', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'poster')
    ### end Alembic commands ###