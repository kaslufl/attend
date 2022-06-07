from src.domain.models import ClassesModel, LecturesModel
from src.infra.repo.class_repository import ClassRepository
from typing import List


class ClassController:

    def __init__(self, class_repository: ClassRepository):
        self.class_repo = class_repository

    def get_class_by_id(self, class_id: str) -> ClassesModel | bool:
        aclass = self.class_repo.select_class(class_id)
        if len(aclass) > 0:
            return aclass[0]
        return False

    def get_class_lectures(self, class_id: str) -> List[LecturesModel] | bool:
        lectures = self.class_repo.select_class_lectures(class_id)
        if len(lectures) == 0:
            return False
        return lectures
