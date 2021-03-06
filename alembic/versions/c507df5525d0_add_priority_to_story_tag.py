"""Add priority to story tag

Revision ID: c507df5525d0
Revises: 0d5da074e3dd
Create Date: 2018-01-08 07:41:51.060368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c507df5525d0'
down_revision = '0d5da074e3dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story_tag', sa.Column('priority', sa.Integer(), server_default='0', nullable=False))
    op.create_index(op.f('ix_story_tag_priority'), 'story_tag', ['priority'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_story_tag_priority'), table_name='story_tag')
    op.drop_column('story_tag', 'priority')
    # ### end Alembic commands ###
