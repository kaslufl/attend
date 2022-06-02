import uuid
import enum
from datetime import datetime

from sqlalchemy import Column, Integer, String, Enum, Boolean
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP

from src.infra.config.db_base import Base


class UserTypes(enum.Enum):
    superadmin = 'superadmin'
    student = 'student'


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    matricula = Column(Integer)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    lastLogin = Column(TIMESTAMP)
    photoUrl = Column(String)
    isActive = Column(Boolean, default=True)
    role = Column(Enum(UserTypes))
    createdAt = Column(TIMESTAMP, default=datetime.utcnow())
    updatedAt = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow())
