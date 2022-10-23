from database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from .mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
