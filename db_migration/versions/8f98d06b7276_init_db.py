"""init DB

Revision ID: 8f98d06b7276
Revises: 
Create Date: 2022-05-08 05:34:26.847120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f98d06b7276'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('top_type', sa.Integer(), nullable=False),
    sa.Column('color', sa.VARCHAR(length=6), nullable=False),
    sa.PrimaryKeyConstraint('top_type', 'color', name='color_key')
    )
    op.create_table('cookie_toppings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cookie_id', sa.Integer(), nullable=False),
    sa.Column('part_num', sa.Integer(), nullable=False),
    sa.Column('part_pos', sa.Integer(), nullable=False),
    sa.Column('is_lock', sa.BOOLEAN(), nullable=False),
    sa.Column('desc', sa.VARCHAR(length=64), nullable=True),
    sa.Column('top_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cookies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cookie_name', sa.VARCHAR(length=32), nullable=False),
    sa.Column('cool_time', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('top_id', sa.Integer(), nullable=False),
    sa.Column('raw_cookie_id', sa.Integer(), nullable=False),
    sa.Column('raw_desc', sa.VARCHAR(length=64), nullable=True),
    sa.Column('cur_cookie_id', sa.Integer(), nullable=False),
    sa.Column('cur_desc', sa.VARCHAR(length=64), nullable=True),
    sa.Column('modify_time', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('top_id', 'modify_time', name='record_key')
    )
    op.create_table('toppings',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('ATK', sa.Float(), nullable=False),
    sa.Column('DEF', sa.Float(), nullable=False),
    sa.Column('HP', sa.Float(), nullable=False),
    sa.Column('SPD', sa.Float(), nullable=False),
    sa.Column('CRIT', sa.Float(), nullable=False),
    sa.Column('COOL', sa.Float(), nullable=False),
    sa.Column('D_RESIST', sa.Float(), nullable=False),
    sa.Column('C_RESIST', sa.Float(), nullable=False),
    sa.Column('BUFF', sa.Float(), nullable=False),
    sa.Column('DEBUFF', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('toppings')
    op.drop_table('records')
    op.drop_table('cookies')
    op.drop_table('cookie_toppings')
    op.drop_table('color')
    # ### end Alembic commands ###