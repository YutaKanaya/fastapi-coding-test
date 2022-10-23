from sqlalchemy.orm.session import Session

import schemas.patient as patient_schema
import models.patient as patient_model

def get_patient(db: Session, patient_id: int) -> patient_schema.Patient:
    return db.query(patient_model.Patient).filter(patient_model.Patient.id == patient_id).first()

def create_patient(db: Session, patient_create: patient_schema.PatientCreate) -> patient_schema.Patient:
    patient = patient_model.Patient(**patient_create.dict())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient
