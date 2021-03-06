"""Remove unique constraint in display_name

Revision ID: 364469432c0
Revises: 41c94f4971e
Create Date: 2017-02-02 11:19:23.376489

"""

# revision identifiers, used by Alembic.
revision = '364469432c0'
down_revision = '41c94f4971e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('uq_display_name', table_name='user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('uq_display_name', 'user', ['display_name'], unique=True)
    ### end Alembic commands ###
