from pydantic import BaseModel


class UsersModel(BaseModel):
    id: str = None
    matricula: int
    email: str
    password: str
    name: str
    lastLogin: str = None
    photoUrl: str = None
    isActive: bool = None
    role: str
    createdAt: str = None
    updatedAt: str = None
