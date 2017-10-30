"""empty message

Revision ID: 2443cb35413c
Revises: 7bc09a268523
Create Date: 2017-10-30 11:06:03.495000

"""

# revision identifiers, used by Alembic.
revision = '2443cb35413c'
down_revision = '7bc09a268523'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('app_name', sa.String(length=128), nullable=True),
    sa.Column('web_url', sa.String(length=128), nullable=True),
    sa.Column('ssh_url', sa.String(length=128), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instances')
    ### end Alembic commands ###
