from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from UserTaskDB import User, Task




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
