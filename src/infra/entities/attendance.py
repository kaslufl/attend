from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.infra.config.db_base import Base


class Attendance(Base):
    __tablename__ = 'attendances'
    student_id = Column(UUID, ForeignKey("users.id"), primary_key=True)
    lecture_id = Column(UUID, ForeignKey("lectures.id"), primary_key=True)
    presence = Column(Boolean, default=False)
    student = relationship("User")
    lecture = relationship("Lecture")
