from sqlalchemy.orm import sessionmaker
from Model.Server import engine


def getSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session