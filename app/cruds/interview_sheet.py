from typing import List

from sqlalchemy.orm.session import Session
from sqlalchemy import select
from sqlalchemy.engine import Result

import schemas.interview_sheet as interview_sheet_schema
from models import InterviewSheet, Patient
import cruds.patient as patient_crud


def get_interview_sheet_list(db: Session):
    return db.query(InterviewSheet).all()

def create_interview_sheet(
    db: Session,
    interview_sheet_create: interview_sheet_schema.InterviewSheetCreate
) -> interview_sheet_schema.InterviewSheet:
    if interview_sheet_create.patient_id == None:
        patient = patient_crud.create_patient(db, interview_sheet_create.patient)
    else:
        patient = patient_crud.get_patient(db, interview_sheet_create.patient_id)
    interview_sheet_create.patient = patient

    interview_sheet = InterviewSheet(**interview_sheet_create.dict())
    db.add(interview_sheet)
    db.commit()
    db.refresh(interview_sheet)
    return interview_sheet
