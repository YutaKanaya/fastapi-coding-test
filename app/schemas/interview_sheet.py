from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel

from schemas.patient import Patient, PatientCreate

class InterviewSheet(BaseModel):
    id: int
    patient_id: int
    subjective_symptoms: str
    symptom_cause: Optional[str]
    since_when_symptoms: Optional[datetime]
    request_inspection: Optional[str]

class InterviewSheetResponse(InterviewSheet):
    pass

    class Config:
        orm_mode = True

class InterviewSheetCreate(BaseModel):
    subjective_symptoms: str
    symptom_cause: Optional[str]
    since_when_symptoms: Optional[datetime]
    request_inspection: Optional[str]
    patient_id: Optional[int]
    patient: Optional[PatientCreate]
