from datetime import timedelta
from dataclasses import dataclass

from fastapi import APIRouter, HTTPException, status

from src.domain.core.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from src.domain.core.security import authenticate_user

auth = APIRouter(
    prefix='/api/auth',
    tags=['auth'],
    responses={400: {"description": "Bad Request"}}
)


@dataclass
class AuthBody:
    username: str
    password: str


@auth.post("/token")
async def login_access_token(body: AuthBody):
    user = authenticate_user(body.username, body.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"matricula": user.matricula}, expires_delta=access_token_expires
    )
    return {
        "user": user,
        "token": access_token,
        "token_type": "bearer",
        "expires_in": access_token_expires.seconds
    }
