from sqlalchemy import Column, Integer, String, Text, DateTime
from models.db_setting import Base
from datetime import datetime


class Characters(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(255), unique=True, nullable=False)
    body = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)


class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)
