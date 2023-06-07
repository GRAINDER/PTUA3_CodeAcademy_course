from main import Vaikas, Tevas
from session import session



vaikas = Vaikas(vardas="Vaikas", pavarde="Tevaika", mokymo_istaiga = "Čiurlionio gimnazija")
vaikas_antras = Vaikas(vardas="Vaikas_vaikas", pavarde="Tevaika_tevaika", mokymo_istaiga = "Neries gimnazija")
tevas = Tevas(vardas="Antras_Tevas", pavarde="Tevaika_Antrasis", vaikas=vaikas)
session.add(tevas)
session.commit()