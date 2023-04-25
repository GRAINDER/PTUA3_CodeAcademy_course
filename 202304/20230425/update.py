from session import session
from main import Projektas


# projektas1 = session.query(Projektas).get(2)
# projektas1.price = 50000
# session.commit()

projektas1 = session.query(Projektas).get(1)
projektas1.name = "Project 1"
session.commit()