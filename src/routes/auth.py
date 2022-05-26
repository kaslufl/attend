from fastapi import APIRouter

auth = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={400: {"description": "Bad Request"}}
)


@auth.post("/token")
async def login_access_token():
    # todo
    pass
