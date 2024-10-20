from alembic_utils.pg_view import PGView

cash_view = PGView(
    schema="public",
    signature="cash_view",
    definition="select id, ts, value_decimal as value from kpi where name = 'cash'",
)
