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
