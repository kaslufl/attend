from fastapi import APIRouter

user = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {"description": "Not Found"}}
)


@user.get("/{user_id}")
def get_user_by_id():
    # todo
    pass
