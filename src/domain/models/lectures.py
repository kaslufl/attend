from pydantic import BaseModel


class LecturesModel(BaseModel):
    id: str
    content: str
    date: str
    class_id: str
