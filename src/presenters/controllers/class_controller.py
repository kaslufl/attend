from src.domain.models.classes import ClassesModel
from src.infra.repo.class_repository import ClassRepository


class ClassController:

    def __init__(self, class_repository: ClassRepository):
        self.class_repo = class_repository

    def get_class_by_id(self, class_id: str) -> ClassesModel | bool:
        aclass = self.class_repo.select_class(class_id)
        if len(aclass) > 0:
            return aclass[0]
        return False
