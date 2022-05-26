from typing import List

from src.domain.models import UsersModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import User
from sqlalchemy.orm.exc import NoResultFound


class UserRepository:
    """Class to manage User repository"""

    @classmethod
    def insert_user(cls, name: str, password: str, matricula: int, email: str, role: str) -> UsersModel:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(name=name, password=password, matricula=matricula, email=email, role=role)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return UsersModel(**new_user.__dict__)

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def select_user(cls, user_id: str = None) -> List[UsersModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(id=user_id)
                    .one()
                )
                return [data]

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()
