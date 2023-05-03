from getpass import getpass
from UserTaskDB import User, Task
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from UserTaskHANDLER import TaskHandler, UserHandler


engine = create_engine('sqlite:///todo2.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()
user_handler = UserHandler(session)
task_handler = TaskHandler(session)

def register():
    name = input('Enter a name: ')
    email = input('Enter a email: ')
    password = getpass('Enter a password: ')

    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(name= name, email=email, password=password)
    session.add(user)
    session.commit()

    print('Registration successful!')

def login():
    email = input('Enter your email: ')
    password = getpass('Enter your password: ')

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).filter_by(email=email).first()

    if user is not None and user.password == password:
        print('Login successful!')
    while True:
        print('1. Add task\n2. Delete task\n3. Update task\n4. Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            user_id = input('Enter user id: ')
            task_handler.add_task(title=title, description=description, user_id=user_id)
        elif choice == '2':
            id = input('Enter task id You want to delete:: ')
            task_handler.delete_task(id=id)
        elif choice == '3':
            id = input('Enter task id You want to update: ')
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            task_handler.update_task(id=id, title=title, description=description)
        elif choice == '4':
            print('Logging out...')
            break
        else:
            print('Invalid choice')
    else:
        print('Invalid username or password')

