from employees import Employee
from session import session


# projektas1 = session.query(Projektas).all()
# print(projektas1)


projects = session.query(Employee).filter_by(name="2 projektas").first()

print(projects)