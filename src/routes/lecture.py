import uuid

from fastapi import APIRouter, HTTPException, status, Depends

from src.composer.lecture_composite import lecture_composer
from src.domain.core.jwt import get_current_active_user
from src.domain.models.users import UsersModel

lecture = APIRouter(
    prefix='/api/lectures',
    tags=['lectures'],
    responses={404: {"description": "Not Found"}}
)


@lecture.get("/{lecture_id}")
def get_class_by_id(lecture_id: uuid.UUID):
    route = lecture_composer()
    response = route.get_lecture(lecture_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecture not found",
        )
    return {"lecture": response}
