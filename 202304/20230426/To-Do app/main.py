from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///toDolist.db')
Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column("Username", String)
    username_id = Column(Integer, ForeignKey("password.id"))


class Password(Base):
    __tablename__ = "password"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    password = Column("Password", String)


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column("Vardas", String)
    description = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)
    user_id = Column(Integer, ForeignKey("user.id"))
    tevas = relationship("Tevas", back_populates="user")


Base.metadata.create_all(engine)
