from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        Base.metadata.create_all(self.engine)

    def add_item(self, item):
        self.session.add(item)
        self.session.commit()

    def get_item_by_id(self, item_id):
        return self.session.query(Item).filter_by(id=item_id).first()

    def get_all_items(self):
        return self.session.query(Item).all()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, description={self.description})>"






db = Database('sqlite:///test.db')
item1 = Item(name='Item 1', description='This is item 1')
db.add_item(item1)
item2 = db.get_item_by_id(1)
all_items = db.get_all_items()
