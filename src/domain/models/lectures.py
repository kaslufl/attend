from pydantic import BaseModel


class LecturesModel(BaseModel):
    id: str
    code: str
    subject_id: str
    professor_id: str
    period_id: str
