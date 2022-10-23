from database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin


class InterviewSheet(Base, TimestampMixin):
    __tablename__ = 'interview_sheets'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    subjective_symptoms = Column(String(128), nullable=False)
    symptom_cause = Column(String(128), nullable=True)
    since_when_symptoms = Column(Timestamp, nullable=True)
    request_inspection = Column(String(128), nullable=True)

    patient = relationship(
        'Patient',
        back_populates='interview_sheets'
    )
