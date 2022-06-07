import uuid

from fastapi import APIRouter, HTTPException, status, Depends

from src.composer.class_composite import class_composer
from src.domain.core.jwt import get_current_active_user
from src.domain.models.users import UsersModel

aclass = APIRouter(
    prefix='/api/classes',
    tags=['classes'],
    responses={404: {"description": "Not Found"}}
)


@aclass.get("/{class_id}")
def get_class_by_id(class_id: uuid.UUID, current_user: UsersModel = Depends(get_current_active_user)):
    route = class_composer()
    response = route.get_class_by_id(class_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found",
        )
    return {"class": response}
