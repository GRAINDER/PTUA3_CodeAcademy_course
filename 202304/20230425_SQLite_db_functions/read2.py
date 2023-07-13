from main import Projektas
from session import session


search = session.query(Projektas).filter(Projektas.name.ilike("2%"))
search2 = session.query(Projektas).filter(Projektas.price > 1000)
search3 = session.query(Projektas).filter(
    Projektas.price > 1000,
    Projektas.name.ilike("2%"))

print([i for i in search])
print([i for i in search2])
print([i for i in search3])


# [2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]
# [1 Naujas pr. - 20000.0: 2021-02-03 14:29:33.437231, 2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]
# [2 2 projektas - 55000.0: 2021-02-03 14:29:33.477232]

sum_price= 0

for project in search2:
    sum_price += search2.price

print(sum_price)