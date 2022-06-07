from src.domain.models import UsersModel, ClassesModel
from src.infra.repo.user_repository import UserRepository
from src.domain.core.security import get_password_hash
from fastapi import HTTPException, status
from typing import List


class UserController:

    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    def insert_user(self, user: UsersModel) -> UsersModel:
        hashed_password = get_password_hash(user.password)

        try:
            self.user_repo.insert_user(user.name, hashed_password, user.matricula, user.email, user.role, user.photoUrl)

        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request",
            )
        created_user = self.get_user_by_matricula(user.matricula)
        return created_user

    def get_user_by_id(self, user_id: str) -> UsersModel | bool:
        user = self.user_repo.select_user(user_id)
        if len(user) > 0:
            return user[0]
        return False

    def get_user_by_matricula(self, user_matricula: int) -> UsersModel | bool:
        user = self.user_repo.select_user_by_matricula(user_matricula)
        if len(user) > 0:
            return user[0]
        return False

    def get_user_classes(self, user_id: str) -> List[ClassesModel] | bool:
        classes = self.user_repo.select_user_classes(user_id)
        if len(classes) == 0:
            return False

        result = []
        for aclass in classes:
            dic = aclass._asdict()
            dic["date"] = self.user_repo.select_user_class_first_lecture(aclass.id)
            result.append(dic)

        return result
