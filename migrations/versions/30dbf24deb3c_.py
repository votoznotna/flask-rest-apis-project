"""empty message

Revision ID: 30dbf24deb3c
Revises: a0997ea512d8
Create Date: 2023-11-29 12:18:19.348068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30dbf24deb3c'
down_revision = 'a0997ea512d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint("email", ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint("email", type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
