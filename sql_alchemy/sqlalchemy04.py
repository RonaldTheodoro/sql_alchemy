from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship(Person)


engine = create_engine('sqlite:///')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

s = session()
p = Person(name='person')
s.add(p)
a = Address(address='address', person=p)
s.add(a)

p = s.query(Person).filter(Person.name == 'person').one()
print(p.id, p.name)

a = s.query(Address).filter(Address.person == p).one()
print(a.id, a.address)
