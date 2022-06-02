from src.infra.repo.user_repository import UserRepository
from src.presenters.controllers.user_controller import UserController


def user_composer():
    user_repo = UserRepository()
    user_routes = UserController(user_repo)
    return user_routes
