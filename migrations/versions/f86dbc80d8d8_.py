"""empty message

Revision ID: f86dbc80d8d8
Revises: 1e5b3dee638d
Create Date: 2020-10-15 09:02:40.423251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f86dbc80d8d8'
down_revision = '1e5b3dee638d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('firstName', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('lastName', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('userName', sa.String(length=80), nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', 'userName')
    op.drop_column('user', 'lastName')
    op.drop_column('user', 'firstName')
    op.drop_table('follower')
    # ### end Alembic commands ###
