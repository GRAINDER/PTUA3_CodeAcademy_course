from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from UserTaskHANDLER import UserHandler, TaskHandler


engine = create_engine('sqlite:///todo2.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


session = Session()
user_handler = UserHandler(session)
task_handler = TaskHandler(session)


user_handler.add_user('Paulius', "paulius@email.lt", "qwerty123")
user_handler.add_user('Antanas', "antanas@email.lt", "qazwsx5656")
user_handler.add_user('Kestutis', "kestutis@email.lt", "qwsascds666")
user_handler.add_user('Algis', "algis@email.lt", "sadsad1212")
task_handler.add_task('Cleaning', "Clean Windows", 1)
task_handler.add_task('Cleaning', "Clean Floor", 2)
task_handler.add_task('Cleaning', "Clean Tables", 3)
task_handler.add_task('Fixing', "Fix broken doors", 4)

# task_handler.update_task(2, "Cleaning", "Clean chair",)

all_tasks = task_handler.get_all_tasks()
for task in all_tasks:
    print(task.title, task.description, task.created_at)