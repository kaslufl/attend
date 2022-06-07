from typing import List

from sqlalchemy.orm.exc import NoResultFound

from src.domain.models import ClassesModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import Class


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
