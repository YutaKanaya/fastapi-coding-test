from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    name: str
    gender: Optional[int]
    birthday: datetime
    address: str

class PatientCreate(BaseModel):
    name: str
    gender: Optional[int]
    birthday: datetime
    address: str
