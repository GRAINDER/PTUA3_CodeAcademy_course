from main import Projektas
from session import session

projektas1 = session.query(Projektas).filter_by(name="Naujas pr.").one()

session.delete(projektas1)
session.commit()