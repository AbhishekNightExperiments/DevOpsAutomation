from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt
from datetime import datetime

Base = declarative_base()


class Instances(Base):
    """ This Class Store Detail of the Server"""
    __tablename__ = "Instances"
    id = Column(Integer, autoincrement=True, primary_key=True)
    ip = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)
    dbUser = Column(String(100), nullable=False)
    dbName = Column(String(100), nullable=False)
    dbPass = Column(String(100), nullable=False)
    sshUser = Column(String(100), nullable=False)
    sshPass = Column(String(100), nullable=False)


class User(Base):
    """ This Class Store the Detail of the User"""
    __tablename__ = "User"
    id = Column(Integer, autoincrement=True, primary_key=True)
    role = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), nullable=True)
    avatar = Column(String(200))
    active = Column(Boolean, default=False)
    tokens = Column(String(200))
    created_at = Column(DateTime, default=dt.datetime.utcnow())



class Roles(Base):
    """ This Class Store the Detail of the User"""
    __tablename__ = "Roles"
    id = Column(Integer, autoincrement=True, primary_key=True)
    role = Column(String(100), nullable=True)
    capabilities = Column(String(200), nullable=True)


engine = create_engine('mysql+pymysql://root:root@localhost:3306/automation')
Base.metadata.create_all(engine)
