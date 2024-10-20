from datetime import date

from .kpi import Kpi
from ..common.base import session_factory


def create_kpis():
    session = session_factory()
    january = Kpi("cash", date(2024, 1, 1), 1000000)
    february = Kpi("cash", date(2024, 3, 1), 900000)
    march = Kpi("cash", date(2024, 3, 1), 800000)
    session.add(january)
    session.add(february)
    session.add(march)
    session.commit()
    session.close()


def get_kpis():
    session = session_factory()
    kpis_query = session.query(Kpi)
    session.close()
    return kpis_query.all()


if __name__ == "__main__":
    kpis = get_kpis()
    if len(kpis) == 0:
        create_kpis()
    kpis = get_kpis()

    for kpi in kpis:
        print(f"{kpi.name} was set on {kpi.ts} and its value is {kpi.value_decimal}")
