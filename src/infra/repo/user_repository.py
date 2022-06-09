from datetime import datetime
from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.domain.models import UsersModel, ClassesModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import User


def get_chart_data(total_attendance: int, total_students: int, total_lectures: int):
    div = total_students * total_lectures
    if div == 0:
        return 0
    return total_attendance * 100 / div


class UserRepository:
    """Class to manage User repository"""

    @classmethod
    def update_last_login(cls, user_id) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(id=user_id)
                    .one()
                )
                data.lastLogin = datetime.utcnow()
                db_connection.session.commit()

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

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

    @classmethod
    def update_user_by_id(cls, user_id: str = None, user_name: str = None, user_email: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(id=user_id)
                    .one()
                )
                if user_name:
                    data.name = user_name

                if user_email:
                    data.email = user_email

                db_connection.session.commit()
                db_connection.session.refresh(data)
                return data

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def update_user_photo(cls, user_id: str = None, user_photo: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(User)
                    .filter_by(id=user_id)
                    .one()
                )
                data.photoUrl = user_photo

                db_connection.session.commit()
                db_connection.session.refresh(data)
                return data


            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def select_student_classes(cls, user_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    'select c.id, c.code, c."photoUrl", s.name as subject '
                    'from classes c inner join subjects s on c.subject_id = s.id '
                    'inner join users u on u.id = c.professor_id '
                    f"inner join studentclass s2 on c.id = s2.class_id where s2.student_id = '{user_id}'"
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
    def select_class_professor(cls, class_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    f"select u.* from users u inner join classes c on u.id = c.professor_id"
                    f" where c.id = '{class_id}'"
                ).one()
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def select_student_presence(cls, user_id: str = None, class_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    f"select count(*) from attendances a inner join lectures l on a.lecture_id = l.id "
                    f"inner join classes c on c.id = l.class_id "
                    f"where student_id = '{user_id}' and a.presence = 'f' and c.id = '{class_id}'"
                    f'and l."date" <= '
                    f"'{datetime.utcnow()}'"
                ).one()
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()

    @classmethod
    def select_class_lectures_count(cls, user_id: str = None, class_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    f"select count(*) from attendances a inner join lectures l on a.lecture_id = l.id "
                    f"inner join classes c on c.id = l.class_id "
                    f"where student_id = '{user_id}' and c.id = '{class_id}'"
                ).one()
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()


    @classmethod
    def select_attendance_levels(cls, class_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                total_students = db_connection.session.execute(
                    f"select count(*) from studentclass s where class_id = '{class_id}'"
                ).one()

                total_attendance = db_connection.session.execute(
                    f"select count(*) from attendances a inner join lectures l on a.lecture_id = l.id "
                    f"where l.class_id = '{class_id}' and a.presence = 't' and l.date <= '{datetime.utcnow()}'"
                ).one()

                total_lectures = db_connection.session.execute(
                    f"select count(*) from lectures l where l.class_id = '{class_id}' "
                    f"and l.date <= '{datetime.utcnow()}'"
                ).one()

                return get_chart_data(total_attendance.count, total_students.count, total_lectures.count)

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()
