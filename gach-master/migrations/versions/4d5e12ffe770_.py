"""empty message

Revision ID: 4d5e12ffe770
Revises: None
Create Date: 2014-09-28 15:25:48.945381

"""

# revision identifiers, used by Alembic.
revision = '4d5e12ffe770'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accusation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('who', sa.String(length=255), nullable=True),
    sa.Column('when_s', sa.String(length=255), nullable=True),
    sa.Column('when_e', sa.String(length=255), nullable=True),
    sa.Column('how', sa.String(length=255), nullable=True),
    sa.Column('made_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accusation')
    ### end Alembic commands ###
