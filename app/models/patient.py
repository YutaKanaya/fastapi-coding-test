from database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin


class Patient(Base, TimestampMixin):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    gender = Column(Integer, nullable=True)
    birthday = Column(Timestamp, nullable=False)
    address = Column(String(128), nullable=False)

    interview_sheets = relationship(
        'InterviewSheet',
        back_populates='patient'
    )