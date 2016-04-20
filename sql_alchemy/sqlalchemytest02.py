from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///phones.db')
session = sessionmaker()
session.configure(bind=engine)


class Phone(Base):
    """Telefones"""
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    code = Column(String(2), nullable=False)
    name_employee = Column(String(40), nullable=True)
    phone = Column(String(12), nullable=False)


Base.metadata.create_all(engine)
