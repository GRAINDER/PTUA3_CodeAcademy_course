from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Projektas

engine = create_engine('sqlite:///projektai.db') #sukuriam
Session = sessionmaker(bind=engine) #uzbindinam failui
session = Session() #pasileidziam
""":type: sqlalchemy.orm.Session"""