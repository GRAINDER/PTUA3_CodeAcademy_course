from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///mydb.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)



class DatabaseHandler:
    def __init__(self, session):
        self.session = session

    def add_person(self, name, age):
        person = Person(name=name, age=age)
        self.session.add(person)
        self.session.commit()

    def get_person(self, id):
        person = self.session.query(Person).filter_by(id=id).first()
        return person

    def update_person(self, id, name=None, age=None):
        person = self.get_person(id)
        if name is not None:
            person.name = name
        if age is not None:
            person.age = age
        self.session.commit()

    def delete_person(self, id):
        person = self.get_person(id)
        self.session.delete(person)
        self.session.commit()

    def get_all_people(self):
        people = self.session.query(Person).all()
        return people





session = Session()
handler = DatabaseHandler(session)

# handler.add_person('Paulius', 35)
# handler.add_person('Saulius', 27)
# handler.add_person('Birutė', 55)
# person1 = handler.get_person(1)
# person2 = handler.get_person(2)
# print(person1.name, person1.age)
# print(person2.name, person2.age)
# handler.update_person(1, name='Kestutis', age=31)

# people = handler.get_all_people()
# for person in people:
#     print(person.name, person.age)

handler.delete_person(1)
