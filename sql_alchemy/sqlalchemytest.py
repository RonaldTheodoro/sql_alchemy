from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///lojas.db')
session = sessionmaker()
session.configure(bind=engine)


class Internet(Base):
    """Links de internet"""
    __tablename__ = 'internet'
    id = Column(Integer, primary_key=True)
    ip1 = Column(String(15), nullable=False)
    ip2 = Column(String(15), nullable=False)
    router = Column(String(15), nullable=False)
    sonicwall = Column(String(15), nullable=False)


class State(Base):
    """Estados"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name_state = Column(String(20), nullable=False)


class City(Base):
    """Cidades"""
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name_city = Column(String(20), nullable=False)


class Supervisor(Base):
    """Supervisor"""
    __tablename__ = 'supervisor'
    id = Column(Integer, primary_key=True)
    name_supervisor = Column(String(30), nullable=False)


class Store(Base):
    """Dados da loja"""
    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), nullable=False)
    ramal = Column(String(4), nullable=True)
    adderess = Column(String(35), nullable=True)
    complement = Column(String(25), nullable=True)
    neighborhood = Column(String(25), nullable=False)
    zip_code = Column(String(8), nullable=True)
    razao_social = Column(String(20), nullable=True)
    grife = Column(String(20), nullable=False)
    cnpj = Column(String(14), nullable=False)
    internet_link = Column(Integer, ForeignKey(Internet.id))
    internet = relationship(Internet)
    supervisor_name = Column(Integer, ForeignKey(Supervisor.id))
    supervisor = relationship(Supervisor)
    store_state = Column(Integer, ForeignKey(State.id))
    state = relationship(State)
    store_city = Column(Integer, ForeignKey(City.id))
    city = relationship(City)


Base.metadata.create_all(engine)
