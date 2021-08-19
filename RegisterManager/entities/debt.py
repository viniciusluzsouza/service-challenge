from entities.base import Base

from sqlalchemy import Column, Integer, Float


class Debt(Base):
    __tablename__ = 'debt'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    months = Column(Integer)

    def __init__(self, value, months):
        self.value = value
        self.months = months
