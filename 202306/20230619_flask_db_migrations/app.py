import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()  # Leis dirbti su DB modeliais iš konsolės

db = SQLAlchemy(app)
Migrate(app, db)


# Klasėje Book mus domina publisher_id kintamasis. Jis susieja klasę Book su klase Publisher per ForeignKey,
# kuriame parametruose nurodytas kitos lentelės pavadinimas ir prie kurio lauko rišame, t.y. prie id,
# kuris publishers lentelėje yra primary_key.

class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150))
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))


    def __init__(self, author, title, publisher_id):
        self.author = author
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):
        return self.title


'''
Klasėje Publisher, atgalinį ryšį su Books klase sukuria books kintamąjam priskirta eilutė. 
Parametruose nurodyta klasė, su kuria siejame ir backref - kol kas žiūrėkite, kaip į papildomą 
saitą tarp python klasių. 
'''


class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    


class Address(db.Model):

    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(100), unique=True)
    house_number = db.Column(db.Integer, unique=True)
    flat_number = db.Column(db.Integer, unique=True)
    postal_code = db.Column(db.Integer, unique=True)
    publisher_id = db.relationship('Book', backref='address')
    book_id = db.relationship('Publisher', backref='address')

    def __init__(self, street_name, house_number, flat_number, publisher_id, book_id):
        self.street_name = street_name
        self.house_number = house_number
        self.flat_number = flat_number
        self.publisher_id = publisher_id
        self.book_id = book_id


    def __repr__(self):
        return self.street_name



if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0:', port=5000, debug=True)