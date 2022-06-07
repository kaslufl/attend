from src.infra.repo.lecture_repository import LectureRepository
from src.presenters.controllers.lecture_controller import LectureController


def lecture_composer():
    lecture_repo = LectureRepository()
    lecture_routes = LectureController(lecture_repo)
    return lecture_routes
