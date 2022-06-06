import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.infra.config.db_base import Base


class Class(Base):
    __tablename__ = 'classes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    code = Column(String)
    subject_id = Column(UUID, ForeignKey("subjects.id"))
    professor_id = Column(UUID, ForeignKey("users.id"))
    period_id = Column(UUID, ForeignKey("periods.id"))
    subject = relationship("Subject")
    professor = relationship("User")
    period = relationship("Period")
