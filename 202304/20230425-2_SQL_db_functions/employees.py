import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Employess.db') #pasako kaip prisijungiam prie duombazes
base = declarative_base() #sqlaclhemy bazinis objektas

class Employee(base):
    __tablename__ = 'Employess'
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    birth_date = Column("Birth_date", DateTime)
    salary = Column("Salary", Float)
    starting_date = Column("Starting_date", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name: str, surname: str, birth_date: DateTime, salary: Float):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.salary = salary

    def __repr__(self):
        return f"{self.id} {self.name} - {self.surname}: {self.birth_date} {self.salary} {self.salary_date}"

base.metadata.create_all(engine)