from passlib.context import CryptContext
from src.infra.repo.user_repository import UserRepository
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def authenticate_user(matricula: str, password: str):
    user = UserRepository().select_user_by_matricula(int(matricula))[0]
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
