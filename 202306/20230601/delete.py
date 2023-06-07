from main import db, Message, app


with app.app_context():

    jonas = db.session.get(Message,1)
    db.session.delete(jonas)
    db.session.commit()
    print(Message.query.all())

# [Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]