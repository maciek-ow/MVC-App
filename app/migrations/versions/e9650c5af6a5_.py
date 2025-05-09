"""empty message

Revision ID: e9650c5af6a5
Revises: 8ae793cfd702
Create Date: 2025-05-06 15:41:57.988591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9650c5af6a5'
down_revision = '8ae793cfd702'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=True))
        batch_op.drop_constraint('Tasks_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Tasks', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('Tasks_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.drop_column('status')

    # ### end Alembic commands ###
