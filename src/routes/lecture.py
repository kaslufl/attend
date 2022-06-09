import uuid
from dataclasses import dataclass
from fastapi import APIRouter, HTTPException, status

from src.composer.lecture_composite import lecture_composer

lecture = APIRouter(
    prefix='/api/lectures',
    tags=['lectures'],
    responses={404: {"description": "Not Found"}}
)


@dataclass
class UpdatedAttendance:
    id: str
    attendance: list


@lecture.get("/{lecture_id}")
def get_class_by_id(lecture_id: uuid.UUID):
    route = lecture_composer()
    response = route.get_lecture(lecture_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecture not found",
        )
    return response


@lecture.put("/{lecture_id}/attendance")
def update_attendance(lecture_id: uuid.UUID, attendance_to_update: UpdatedAttendance):
    route = lecture_composer()
    response = route.update_lecture_attendance(lecture_id, attendance_to_update.attendance)
    return response
