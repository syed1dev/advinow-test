from pydantic import BaseModel
from typing import List

class SymptomCreate(BaseModel):
    code: str
    name: str
    diagnostic: bool

class BusinessCreate(BaseModel):
    id: int
    name: str


class ResourceItemSchema(BaseModel):
    business_id: int
    business_name: str
    symptom_code: str
    symptom_name: str
    symptom_diagnostic: bool