import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.infra.config.db_base import Base


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    code = Column(String)
    name = Column(String)
    course_id = Column(UUID, ForeignKey("courses.id"))
    course = relationship("Course")
