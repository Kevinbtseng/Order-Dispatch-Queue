from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum as SqlEnum
from datetime import datetime, timezone
from enum import Enum

class Status(Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    items = Column(String)
    quantity = Column(Integer)
    status = Column(SqlEnum(Status), default=Status.pending, index=True)
    time_created = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
