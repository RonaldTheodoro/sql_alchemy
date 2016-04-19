from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy01 import Base, Address, Person


engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
DBsession = sessionmaker()
DBsession.bind = engine
session = DBsession()
session.query(Person).all()
person = session.query(Person).first()
print(person)
session.query(Address).filter(Address.person == person).all()
address = session.query(Address).filter(Address.person == person).one()
print(address)
