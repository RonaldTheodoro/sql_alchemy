from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy01 import Base, Address, Person


engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata os the Base class so that the
# declaratives can be accesed through a DBsession instance
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
# A DBsession() instance establishes all conversations with the database
# and represents a "staging zone"for all objects loaded intro the
# database session object. Any changes made aganist the objects in the
# session won't be persisted intro the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling sesion.rowback()
session = DBsession()

# Insert a person in the person table
new_person = Person(name='Ronald Theodoro')
session.add(new_person)
session.commit()

# Insert a Address in the address table
new_address = Address(post_code='12345789', person=new_person)
session.add(new_address)
session.commit()
