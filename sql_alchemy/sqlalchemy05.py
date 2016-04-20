from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///')
session = sessionmaker()
session.configure(bind=engine)


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
            Department,
            backref=backref('employees', uselist=True)
    )


Base.metadata.create_all(engine)

func = Employee(name='Ronald Theodoro')
it_department = Department(name='IT')
func.department = it_department
s = session()
s.add(func)
s.add(it_department)
s.commit()
it = s.query(Department).filter(Department.name == 'IT').one()
print(it.employees, it.employees[0].name)

find_it = select([Department.id]).where(Department.name == 'IT')
rs = s.execute(find_it)
print(rs)
print(rs.fetchone())
print(rs.fetchone())

find_func = select([Employee.id]).where(Employee.department_id == 1)
rs = s.execute(find_func)
print(rs)
print(rs.fetchone())
print(rs.fetchone())
print(rs.fetchone())
