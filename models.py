from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    password_hash = Column(String)
    username = Column(String)

    def hash_password(self, password):
        self.password_hash = pwd_security.encrypt(password)
    def verify_password(self, password):
        return pwd_security.verify(password, self.password_hash)


class Metric(Base):
    __tablename__ = "metrics"
    id = Column(Integer, primary_key=True)
    action = Column(String)
    version = Column(String)
    timestamp = Column(DateTime)
    user = Column(String)
