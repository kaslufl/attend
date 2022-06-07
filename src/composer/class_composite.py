from src.infra.repo.class_repository import ClassRepository
from src.presenters.controllers.class_controller import ClassController


def class_composer():
    class_repo = ClassRepository()
    class_routes = ClassController(class_repo)
    return class_routes
