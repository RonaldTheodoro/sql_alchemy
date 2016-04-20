from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemytest import Internet, State, City, Supervisor, Store
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('sqlite:///lojas.db')
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

aux = State(name_state='São Paulo')
session.add(aux)
session.commit()
aux = State(name_state='Rio de Janeiro')
session.add(aux)
session.commit()
aux = State(name_state='Minas Gerais')
session.add(aux)
session.commit()
aux = State(name_state='Espirito Santo')
session.add(aux)
session.commit()

'''

Internet: ip1, ip2, router, sonicwall
State: name_state
City: name_city
Supervisor: name_supervisor
Store: code, ramal, adderess, complement, neighborhood, zip_code, razao_social, grife, cnpj

'''