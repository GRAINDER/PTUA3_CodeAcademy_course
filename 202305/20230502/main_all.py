from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


engine = create_engine('sqlite:///todo2.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(50))
    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(200))
    created_at = Column(DateTime, default=datetime.now())
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")



Base.metadata.create_all(engine)



class UserHandler:
    def __init__(self, session):
        self.session = session

    def add_user(self, name, email, password):
        user = User(name=name, email=email, password=password)
        self.session.add(user)
        self.session.commit()

    def get_user(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        return user

    def get_user_by_email(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        return user

    def update_user(self, id, name=None, email=None, password=None):
        user = self.get_user(id)
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        if password is not None:
            user.password = password
        self.session.commit()

    def delete_user(self, id):
        user = self.get_user(id)
        self.session.delete(user)
        self.session.commit()

class TaskHandler:
    def __init__(self, session):
        self.session = session

    def add_task(self, title, description, user_id):
        task = Task(title=title, description=description, user_id=user_id)
        self.session.add(task)
        self.session.commit()

    def get_task(self, id):
        task = self.session.query(Task).filter_by(id=id).first()
        return task

    def update_task(self, id, title=None, description=None, completed=None):
        task = self.get_task(id)
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        self.session.commit()

    def delete_task(self, id):
        task = self.get_task(id)
        self.session.delete(task)
        self.session.commit()

    def get_all_tasks(self):
        tasks = self.session.query(Task).all()
        return tasks

session = Session()
user_handler = UserHandler(session)
task_handler = TaskHandler(session)


# user_handler.add_user('Paulius', "paulius@email.lt", "qwerty123")
# user_handler.add_user('Antanas', "antanas@email.lt", "qazwsx5656")
# user_handler.add_user('Kestutis', "kestutis@email.lt", "qwsascds666")
# user_handler.add_user('Algis', "algis@email.lt", "sadsad1212")
# # task_handler.add_task('Cleaning', "Clean Windows", 1)
# task_handler.add_task('Cleaning', "Clean Floor", 2)
# task_handler.add_task('Cleaning', "Clean Tables", 3)
# task_handler.add_task('Fixing', "Fix broken doors", 4)

all_tasks = task_handler.get_all_tasks()
for task in all_tasks:
    print(task.title, task.description, task.created_at)
