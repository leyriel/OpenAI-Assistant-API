"""Change Thread model's identifier columne from integer to string

Revision ID: 0528826a5adb
Revises: ac14ce77f3b7
Create Date: 2024-02-18 23:47:09.479635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0528826a5adb'
down_revision: Union[str, None] = 'ac14ce77f3b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('threads', 'identifier',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('threads', 'identifier',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=True)
    # ### end Alembic commands ###