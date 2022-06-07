from typing import List

from sqlalchemy import asc
from sqlalchemy.orm.exc import NoResultFound

from src.domain.models import ClassesModel, LecturesModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import Class, Lecture


class ClassRepository:
    """Class to manage class repository"""

    @classmethod
    def select_class(cls, class_id: str = None) -> List[ClassesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(Class)
                    .filter_by(id=class_id)
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
    def select_class_lectures(cls, class_id: str = None) -> List[LecturesModel]:
        with DBConnectionHandler() as db_connection:
            try:
                data = (
                    db_connection.session.query(Lecture)
                    .filter_by(class_id=class_id)
                    .order_by(asc(Lecture.date))
                    .all()
                )
                return data

            except NoResultFound:
                return []

            except:
                db_connection.session.rollback()
                raise

            finally:
                db_connection.session.close()
