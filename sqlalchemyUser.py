from sqlalchemy import *
from sqlalchemy import Column
from sqlalchemy.types import Integer, Text, String


class sqlAlchemyUser(db.Model):

    userID = Column(Integer, primary_key = True)
    userName = Column(Text)
    passWord = Column(Text)