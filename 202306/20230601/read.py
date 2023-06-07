from main import db, Message, app


with app.app_context():
    all_messages = Message.query.all()
    print(all_messages)

#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]

    message_1 = db.session.get(Message,1)
    print(message_1)

    # Jonas - jonas@mail.com


    antanas = Message.query.get(2)
    antanas.email = 'geras.zmogus@lrs.lt'
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())

# [Jonas - jonas@mail.com, Antanas - geras.zmogus@lrs.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]