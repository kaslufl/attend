import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, DATE
from sqlalchemy.orm import relationship

from src.infra.config.db_base import Base


class Lecture(Base):
    __tablename__ = 'lectures'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    content = Column(String)
    date = Column(DATE)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"))
    aclass = relationship("Class")
