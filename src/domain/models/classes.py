from pydantic import BaseModel


class ClassesModel(BaseModel):
    id: str
    code: str
    subject_id: str
    professor_id: str
    period_id: str
