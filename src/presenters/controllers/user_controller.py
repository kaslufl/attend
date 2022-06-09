from src.domain.models import UsersModel, ClassesModel
from src.infra.repo.user_repository import UserRepository
from src.domain.core.security import get_password_hash
from fastapi import HTTPException, status
from typing import List


class UserController:

    def __init__(self, user_repository: UserRepository):
        self.user_repo = user_repository

    def update_last_login(self, user_id: str):
        self.user_repo.update_last_login(user_id)

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

        result.sort(key=lambda d: d["date"])
        return result

    def update_user_by_id(self, user_id: str, user_name: str, user_email: str) -> UsersModel | bool:
        try:
            result = self.user_repo.update_user_by_id(user_id, user_name, user_email)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request",
            )
        return result

    def update_user_photo_by_id(self, user_id: str, user_photo: str) -> UsersModel | bool:
        try:
            result = self.user_repo.update_user_photo(user_id, user_photo)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request",
            )
        return result

    def get_student_classes(self, user_id: str) -> List[ClassesModel] | bool:
        classes = self.user_repo.select_student_classes(user_id)
        if len(classes) == 0:
            return False

        result = []
        for aclass in classes:
            dic = aclass._asdict()
            dic["date"] = self.user_repo.select_user_class_first_lecture(aclass.id)
            dic["professor"] = self.user_repo.select_class_professor(aclass.id)
            dic["attendanceCount"] = self.user_repo.select_student_presence(user_id, aclass.id).count
            dic["lessonsCount"] = self.user_repo.select_class_lectures_count(user_id, aclass.id).count
            result.append(dic)

        result.sort(key=lambda d: d["date"])
        return result

    def get_user_classes_chart(self, user_id: str):
        classes = self.user_repo.select_user_classes(user_id)

        ordered_classes = []
        for aclass in classes:
            dic = aclass._asdict()
            dic["date"] = self.user_repo.select_user_class_first_lecture(aclass.id)
            ordered_classes.append(dic)
        ordered_classes.sort(key=lambda d: d["date"])

        result = []
        for aclass in ordered_classes:
            data = self.user_repo.select_attendance_levels(aclass["id"])
            result.append(data)
        return result
