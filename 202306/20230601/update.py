from main import db, Message, app
with app.app_context():

    antanas = db.session.get(Message,2)
    antanas.email = 'geras.zmogus@lrs.lt'
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())

# [Jonas - jonas@mail.com, Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]