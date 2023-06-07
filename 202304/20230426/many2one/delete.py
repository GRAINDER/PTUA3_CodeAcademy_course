from session import session
from main import Tevas, Vaikas

tevas = session.query(Tevas).get(1)
session.delete(tevas)
session.commit()