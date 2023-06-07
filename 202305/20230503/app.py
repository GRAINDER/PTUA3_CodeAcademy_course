from login import login, register
from UserTaskHANDLER import TaskHandler, UserHandler
from UserTaskDB import User, Task
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



def main():
    while True:
        print('1. Register\n2. Login\n3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()