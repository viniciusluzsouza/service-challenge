from sqlalchemy import Column, String, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship

from entities.base import Base

# Many to many relationship
personalRegistryAndDebtAssociation = Table(
    'personalRegistry_Debt', Base.metadata,
    Column('idPersonalRegistry', Integer, ForeignKey('personalRegistry.id')),
    Column('idDebt', Integer, ForeignKey('debt.id'))
)


class PersonalRegistry(Base):
    __tablename__ = 'personalRegistry'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(11), nullable=False)
    name = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    debts = relationship("Debt", secondary=personalRegistryAndDebtAssociation, backref='personalRegistry')

    def __init__(self, cpf, name, address, debts):
        self.cpf = cpf
        self.name = name
        self.address = address
        self.debts = debts
