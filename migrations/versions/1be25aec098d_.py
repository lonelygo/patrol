"""empty message

Revision ID: 1be25aec098d
Revises: 
Create Date: 2018-11-12 17:02:28.613604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1be25aec098d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbchannel',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('channel_id', sa.String(length=36), nullable=True),
    sa.Column('channel_number', sa.String(length=20), nullable=True),
    sa.Column('organization_id', sa.String(length=36), nullable=True),
    sa.Column('device_id', sa.String(length=36), nullable=True),
    sa.Column('task_id', sa.String(length=32), nullable=True),
    sa.Column('platform_id', sa.String(length=36), nullable=True),
    sa.Column('platform_host', sa.String(length=20), nullable=True),
    sa.Column('platform_port', sa.String(length=8), nullable=True),
    sa.Column('platform_user', sa.String(length=20), nullable=True),
    sa.Column('platform_password', sa.String(length=36), nullable=True),
    sa.Column('is_platform', sa.Boolean(), nullable=False),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbfaultcount',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('date', sa.String(length=64), nullable=True),
    sa.Column('num', sa.Integer(), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.Column('work_num', sa.Integer(), nullable=True),
    sa.Column('processed', sa.Integer(), nullable=True),
    sa.Column('misdiagnosis', sa.Integer(), nullable=True),
    sa.Column('ignore', sa.Integer(), nullable=True),
    sa.Column('unprocessed', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbitem',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('item_name', sa.String(length=20), nullable=False),
    sa.Column('item_type', sa.Integer(), nullable=False),
    sa.Column('item_desc', sa.String(length=400), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbtask',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('task_name', sa.String(length=64), nullable=False),
    sa.Column('task_type', sa.Integer(), nullable=False),
    sa.Column('minutes', sa.String(length=32), nullable=True),
    sa.Column('hours', sa.String(length=32), nullable=True),
    sa.Column('day_of_month', sa.String(length=32), nullable=True),
    sa.Column('day_of_week', sa.String(length=32), nullable=True),
    sa.Column('task_priority', sa.Integer(), nullable=False),
    sa.Column('task_status', sa.Integer(), nullable=True),
    sa.Column('task_desc', sa.String(length=200), nullable=True),
    sa.Column('alarm_mode', sa.Integer(), nullable=True),
    sa.Column('task_start_date', sa.Date(), nullable=True),
    sa.Column('task_end_date', sa.Date(), nullable=True),
    sa.Column('system_id', sa.String(length=36), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.Column('run_num', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbfault',
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('pic_url', sa.String(length=128), nullable=True),
    sa.Column('video_url', sa.String(length=128), nullable=True),
    sa.Column('task_id', sa.String(length=32), nullable=True),
    sa.Column('channel_id', sa.String(length=36), nullable=True),
    sa.Column('type1', sa.Boolean(), nullable=True),
    sa.Column('type2', sa.Boolean(), nullable=True),
    sa.Column('type3', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tbtask.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbtaskitemrel',
    sa.Column('task_id', sa.String(length=32), nullable=False),
    sa.Column('item_id', sa.String(length=32), nullable=False),
    sa.Column('threshold', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['tbitem.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tbtask.id'], ),
    sa.PrimaryKeyConstraint('task_id', 'item_id')
    )
    op.create_table('tbfaultitemrel',
    sa.Column('fault_id', sa.String(length=32), nullable=False),
    sa.Column('item_id', sa.String(length=32), nullable=False),
    sa.Column('threshold', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['fault_id'], ['tbfault.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['tbitem.id'], ),
    sa.PrimaryKeyConstraint('fault_id', 'item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbfaultitemrel')
    op.drop_table('tbtaskitemrel')
    op.drop_table('tbfault')
    op.drop_table('tbtask')
    op.drop_table('tbitem')
    op.drop_table('tbfaultcount')
    op.drop_table('tbchannel')
    # ### end Alembic commands ###