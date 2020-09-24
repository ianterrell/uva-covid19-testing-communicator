"""empty message

Revision ID: 3525dcf128cb
Revises: 39a845579587
Create Date: 2020-09-23 16:23:09.383030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3525dcf128cb'
down_revision = '39a845579587'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invitation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_sent', sa.DateTime(timezone=True), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('total_recipients', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invitation')
    # ### end Alembic commands ###