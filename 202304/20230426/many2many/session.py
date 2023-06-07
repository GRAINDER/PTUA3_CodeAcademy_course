from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import engine
from main import Tevas, Vaikas

Session = sessionmaker(bind=engine)
session = Session()