from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_user(name,secret_word):
    user = User(username=name)
    user.hash_password(secret_word)
    session.add(user)
    session.commit()

def get_user(username):
    return session.query(User).filter_by(username=username).first()

def get_user_id(id_num):
    return session.query(User).filter_by(id=id_num).first()

def create_metric(descrip,version,timestamp,username):
    metric = Metric(action=descrip, version=version, timestamp=timestamp, user=username)
    session.add(metric)
    session.commit()

def get_metrics():
    return session.query(Metric).all()

