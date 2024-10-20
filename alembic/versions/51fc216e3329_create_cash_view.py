"""create cash view

Revision ID: 51fc216e3329
Revises: bb499cbf2109
Create Date: 2024-10-20 23:31:44.904857

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_view import PGView
from sqlalchemy import text as sql_text

# revision identifiers, used by Alembic.
revision: str = "51fc216e3329"
down_revision: Union[str, None] = "bb499cbf2109"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    public_cash_view = PGView(
        schema="public",
        signature="cash_view",
        definition="select id, ts, value_decimal as value from kpi where name = 'cash'",
    )
    op.create_entity(public_cash_view)


def downgrade() -> None:
    public_cash_view = PGView(
        schema="public",
        signature="cash_view",
        definition="select id, ts, value_decimal as value from kpi where name = 'cash'",
    )
    op.drop_entity(public_cash_view)
