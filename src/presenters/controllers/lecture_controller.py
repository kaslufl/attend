from src.infra.repo.lecture_repository import LectureRepository
from fastapi import HTTPException, status


class LectureController:

    def __init__(self, lecture_repository: LectureRepository):
        self.lecture_repo = lecture_repository

    def get_lecture(self, lecture_id: str) -> dict | bool:
        result = self.lecture_repo.select_lecture(lecture_id)
        if len(result) == 0:
            return False

        lecture = result[0]
        response = lecture.__dict__
        response["subject"] = self.lecture_repo.select_lecture_subject(lecture_id)[0]
        response["teacher"] = self.lecture_repo.select_lecture_teacher(lecture.class_id)[0]
        response["attendance"] = self.lecture_repo.select_lecture_attendance(lecture_id)
        return response

    def update_lecture_attendance(self, lecture_id: str, attendance: list):
        try:
            result = self.lecture_repo.update_lecture_attendance(lecture_id, attendance)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Bad Request",
            )
        return result
