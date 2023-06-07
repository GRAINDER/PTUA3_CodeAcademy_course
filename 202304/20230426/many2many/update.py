from session import session
from main import Tevas

tevas = session.query(Tevas).get(2)
tevas.vaikai[0].vardas = "Vaikas 1"
session.commit()