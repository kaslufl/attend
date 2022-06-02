from fastapi import FastAPI
from src.routes.user import user
from src.routes.auth import auth

app = FastAPI()
app.include_router(user)
app.include_router(auth)
