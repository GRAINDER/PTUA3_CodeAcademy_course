from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Database:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    def create_all_tables(self):
        self.Base.metadata.create_all(self.engine)

    def drop_all_tables(self):
        self.Base.metadata.drop_all(self.engine)

    def create_session(self):
        return self.Session()

    def add_to_session(self, session, instance):
        session.add(instance)
        session.commit()

    def get_from_session(self, session, model, **kwargs):
        return session.query(model).filter_by(**kwargs).first()

    def get_all_from_session(self, session, model):
        return session.query(model).all()