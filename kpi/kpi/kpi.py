from sqlalchemy import Column, String, Date, Integer, Numeric

from ..common.base import Base


class Kpi(Base):
    __tablename__ = "kpi"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ts = Column(Date)
    value_decimal = Column(Numeric(12, 2))

    def __init__(self, name, ts, value_decimal):
        self.name = name
        self.ts = ts
        self.value_decimal = value_decimal
