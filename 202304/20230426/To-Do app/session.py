from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import engine

engine = create_engine('sqlite:///toDolist.db') #sukuriam
Session = sessionmaker(bind=engine) #uzbindinam failui
session = Session() #pasileidziam
""":type: sqlalchemy.orm.Session"""