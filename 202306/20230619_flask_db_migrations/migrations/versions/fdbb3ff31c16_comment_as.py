"""comment'as

Revision ID: fdbb3ff31c16
Revises: 
Create Date: 2023-06-19 21:21:30.737521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdbb3ff31c16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('publisher_id')
        batch_op.drop_column('book_id')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'address', ['address_id'], ['id'])

    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('address_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'address', ['address_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('publishers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('address_id')
        batch_op.drop_column('book_id')

    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('address_id')

    with op.batch_alter_table('address', schema=None) as batch_op:
        batch_op.add_column(sa.Column('book_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('publisher_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key(None, 'books', ['book_id'], ['id'])
        batch_op.create_foreign_key(None, 'publishers', ['publisher_id'], ['id'])

    # ### end Alembic commands ###