from sqlalchemy import Boolean, Column, Integer, String, DateTime


from database.db import Base


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    birthdate = Column(DateTime)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)


