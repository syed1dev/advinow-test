from fastapi import APIRouter, Depends, File, UploadFile, status
from fastapi.responses import JSONResponse
from typing import Optional, List
from models import Business, Symptom
from schemas import BusinessCreate, SymptomCreate, ResourceItemSchema
from database import get_db
from sqlalchemy.orm import Session
import csv
from io import StringIO


router = APIRouter()


def validate_csv(file: UploadFile):
    contents = file.file.read()
    buffer = StringIO(contents.decode('utf-8'))
    reader = csv.DictReader(buffer)

    validated_data = []

    for row in reader:
        row['Symptom Diagnostic'] = row['Symptom Diagnostic'].strip().lower() in ('true', 'yes')

        # Map CSV header names to Pydantic model field names
        business_data = {
            'id': row['Business ID'],
            'name': row['Business Name']
        }
        symptom_data = {
            'code': row['Symptom Code'],
            'name': row['Symptom Name'],
            'diagnostic': row['Symptom Diagnostic']
        }

        validated_data.append((BusinessCreate(**business_data), SymptomCreate(**symptom_data)))

    return validated_data



@router.post('/import_csv')
async def import_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        validated_data = validate_csv(file)
        for business, symptom in validated_data:
            db_business = db.query(Business).filter(Business.id == business.id).first()
            if not db_business:
                db_business = Business(**business.dict())
                db.add(db_business)
                db.commit()

            db_symptom = db.query(Symptom).filter(Symptom.code == symptom.code).first()
            if not db_symptom:
                db_symptom = Symptom(**symptom.dict())
                db.add(db_symptom)
                db.commit()

            if db_symptom not in db_business.symptoms:
                db_business.symptoms.append(db_symptom)
                db.commit()

    except Exception as e:
        file.file.close()
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"result": f"ERROR: {e}"}
        )

    file.file.close()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"result": "SUCCESS"}
    )


@router.get("/business_symptoms", response_model=List[ResourceItemSchema])
def get_resources(
    business_id: Optional[int] = None,
    diagnostic: Optional[bool] = None,
    db: Session = Depends(get_db)
) -> List[ResourceItemSchema]:
    
    query = (
        db.query(
            Business.id.label("business_id"),
            Business.name.label("business_name"),
            Symptom.code.label("symptom_code"),
            Symptom.name.label("symptom_name"),
            Symptom.diagnostic.label("symptom_diagnostic")
        )
        .join(Symptom, Business.symptoms)
    )
    
    if business_id:
        query = query.filter(Business.id == business_id)
    
    if diagnostic is not None:
        query = query.filter(Symptom.diagnostic == diagnostic)
    
    res = query.all()
    return [ResourceItemSchema(**row._asdict()) for row in res]