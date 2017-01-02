"""empty message

Revision ID: 3f05ade0151e
Revises: 
Create Date: 2016-12-26 20:55:22.307091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f05ade0151e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), server_default=u'', nullable=False),
    sa.Column('label', sa.Unicode(length=255), server_default=u'', nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Unicode(length=255), server_default=u'', nullable=False),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('first_name', sa.Unicode(length=50), server_default=u'', nullable=False),
    sa.Column('last_name', sa.Unicode(length=50), server_default=u'', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_roles')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###