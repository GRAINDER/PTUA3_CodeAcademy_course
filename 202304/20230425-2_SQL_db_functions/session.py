from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from employees import Employee


engine = create_engine('sqlite:///Employess.db') #sukuriam
Session = sessionmaker(bind=engine) #uzbindinam failui
session = Session() #pasileidziam
""":type: sqlalchemy.orm.Session"""