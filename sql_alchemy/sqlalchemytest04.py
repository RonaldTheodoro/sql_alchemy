from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemytest import Internet, State, City, Supervisor, Store
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///lojas.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
DBsession.bind = engine
session = DBsession()


session.query(State).all()
state = session.query(State).all()
for st in state:
    print(st.name_state)

'''

session.query(Address).filter(Address.person == person).all()
address = session.query(Address).filter(Address.person == person).one()
print(address)

'''