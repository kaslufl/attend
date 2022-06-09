from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.domain.models import LecturesModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import Lecture, Attendance


class LectureRepository:

    @classmethod
    def select_lecture(cls, lecture_id: str = None) -> List[LecturesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(Lecture)
                    .filter_by(id=lecture_id)
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
    def select_lecture_teacher(cls, class_id: str = None) -> List[LecturesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    'select u.id, u.name, u."photoUrl" from users u inner join classes c on '
                    f"c.professor_id = u.id where c.id = '{class_id}'"
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
    def select_lecture_attendance(cls, lecture_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    'select u.id, u.name, u."photoUrl", at.presence from users u inner join attendances at '
                    f"on at.student_id = u.id where at.lecture_id = '{lecture_id}'"
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
    def select_lecture_subject(cls, lecture_id: str = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.execute(
                    'select s.* from subjects s inner join classes cl on cl.subject_id = s.id inner join lectures l '
                    f"on l.class_id = cl.id where l.id = '{lecture_id}'"
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
    def update_lecture_attendance(cls, lecture_id: str = None, attendance: list = None):
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(Attendance)
                    .filter_by(lecture_id=lecture_id)
                    .all()
                )

                for attendee in data:
                    new_attendance = list(filter(lambda d: d["id"] == str(attendee.student_id), attendance))[0]
                    attendee.presence = new_attendance["presence"]
                db_connection.session.commit()

                data = (
                    db_connection.session.query(Attendance)
                    .filter_by(lecture_id=lecture_id)
                    .all()
                )
                return data

            except Exception as e:
                print(e)
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()
