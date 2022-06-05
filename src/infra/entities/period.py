import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from src.infra.config.db_base import Base


class Period(Base):
    __tablename__ = 'periods'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    year = Column(Integer)
    code = Column(String)
