import uuid

from fastapi import APIRouter, HTTPException, status, Depends

from src.composer.user_composite import user_composer
from src.domain.core.jwt import get_current_active_user
from src.domain.models.users import UsersModel

user = APIRouter(
    prefix='/api/users',
    tags=['users'],
    responses={404: {"description": "Not Found"}}
)


@user.get("/{user_id}")
def get_user_by_id(user_id: uuid.UUID, current_user: UsersModel = Depends(get_current_active_user)):
    route = user_composer()
    response = route.get_user_by_id(user_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    return {"user": response}


@user.post("/", status_code=201)
def insert_user(user: UsersModel, current_user: UsersModel = Depends(get_current_active_user)):
    route = user_composer()
    response = route.insert_user(user)
    return {"user": response}
