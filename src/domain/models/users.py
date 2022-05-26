from pydantic import BaseModel


class UsersModel(BaseModel):
    id: str
    matricula : int
    email: str
    password: str
    name: str
    lastLogin: str
    photoUrl: str
    isActive: bool
    role: str
    createdAt = str
    updatedAt = str
