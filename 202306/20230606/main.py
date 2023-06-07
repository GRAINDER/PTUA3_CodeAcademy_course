import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos
db = SQLAlchemy(app)
# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę

class Tevas(db.Model):
    __tablename__ = "tevas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)
    vaikas_id = db.Column(db.Integer, db.ForeignKey("vaikas.id"))
    vaikas = db.relationship("Vaikas")


class Vaikas(db.Model):
    __tablename__ = "vaikas"
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column("Vardas", db.String)
    pavarde = db.Column("Pavardė", db.String)


with app.app_context():
    db.create_all()