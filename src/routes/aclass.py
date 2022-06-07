import uuid

from fastapi import APIRouter, HTTPException, status

from src.composer.class_composite import class_composer

aclass = APIRouter(
    prefix='/api/classes',
    tags=['classes'],
    responses={404: {"description": "Not Found"}}
)


@aclass.get("/{class_id}")
def get_class_by_id(class_id: uuid.UUID):
    route = class_composer()
    response = route.get_class_by_id(class_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found",
        )
    return {"class": response}


@aclass.get("/{class_id}/lectures")
def get_class_lectures(class_id: uuid.UUID):
    route = class_composer()
    a_class = route.get_class_by_id(class_id)
    lectures = route.get_class_lectures(class_id)
    if not aclass:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found",
        )
    if not lectures:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lectures not found",
        )
    return {"class": a_class, "lectures": lectures}
