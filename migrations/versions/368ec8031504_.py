"""empty message

Revision ID: 368ec8031504
Revises: 
Create Date: 2020-01-30 19:29:13.636001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '368ec8031504'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True, comment='Логин пользователя'),
    sa.Column('email', sa.String(length=64), nullable=True, comment='Почтовый ящик'),
    sa.Column('password_hash', sa.String(length=365), nullable=True, comment='Пароль(хэш)'),
    sa.Column('token', sa.String(length=365), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_token'), 'users', ['token'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_token'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
