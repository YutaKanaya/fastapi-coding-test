from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from auth.oauth2 import oauth2_scheme
from database import get_db
from typing import List

from models import InterviewSheet
import cruds.interview_sheet as interview_sheet_crud
import schemas.interview_sheet as interview_sheet_schema

router = APIRouter(
    tags=['interview_sheet']
)

@router.get("/interview_sheets", response_model=List[interview_sheet_schema.InterviewSheetResponse])
def get_interview_sheet_list(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return interview_sheet_crud.get_interview_sheet_list(db)

@router.post("/interview_sheets", response_model=interview_sheet_schema.InterviewSheetResponse)
def post_interview_sheet_list(interview_sheet_body: interview_sheet_schema.InterviewSheetCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    result = interview_sheet_crud.create_interview_sheet(db, interview_sheet_body)
    return result
