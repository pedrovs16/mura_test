from datetime import datetime
from sqlalchemy import BigInteger, Column, String, Text, DateTime, ForeignKey, JSON
from infrastructure.db import Base
from infrastructure.models.common import CommonBaseModel


class Email(Base, CommonBaseModel):
    __tablename__ = "email"

    id = Column(BigInteger, primary_key=True)
    address = Column(String(255), nullable=False)
    to = Column(String(255), nullable=False)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    reply_to = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Email(id={self.id})>"
