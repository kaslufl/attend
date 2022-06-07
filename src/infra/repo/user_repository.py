from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.domain.models import UsersModel, ClassesModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import User


class UserRepository:
    """Class to manage User repository"""

    @classmethod
    def insert_user(cls, name: str, password: str, matricula: int, email: str, role: str, photoUrl: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = User(
                    name=name,
                    password=password,
                    matricula=matricula,
                    email=email,
                    role=role,
                    photoUrl=photoUrl
                )
                db_connection.session.add(new_user)
                db_connection.session.commit()

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

    @classmethod
    def select_user_by_matricula(cls, user_matricula: int = None) -> List[UsersModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(matricula=user_matricula)
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

    @classmethod
    def select_user_classes(cls, user_id: str = None) -> List[ClassesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    f"select c.id, c.code, s.name as subject from classes c inner join subjects s "
                    f"on c.subject_id = s.id  where c.professor_id = '{user_id}'"
                ).all()
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def select_user_class_first_lecture(cls, class_id: str = None) -> List[ClassesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    f"select l.date from lectures l where l.class_id = '{class_id}'"
                ).first()
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()
