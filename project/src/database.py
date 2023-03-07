from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def create_db_engine(db_url):
    return create_engine(db_url)

def create_db_session(engine):
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return Session()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def create_db_engine(db_url):
    return create_engine(db_url)

def create_db_session(engine):
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return Session()
