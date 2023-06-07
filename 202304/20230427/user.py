from sqlalchemy import Column, Integer, String
from database import Database

db = Database('sqlite:///test.db')

class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

db.create_all_tables()

session = db.create_session()

user = User(name='John', age=30)
db.add_to_session(session, user)

user = db.get_from_session(session, User, name='John')
print(user.name)

users = db.get_all_from_session(session, User)
for user in users:
    print(user.name)

session.close()

# db.drop_all_tables()
