from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infra.config.db_base import Base


class StudentClass(Base):
    __tablename__ = 'studentclass'
    student_id = Column(UUID, ForeignKey("users.id"), primary_key=True)
    class_id = Column(UUID, ForeignKey("classes.id"), primary_key=True)
    student = relationship("User")
    aclass = relationship("User")
