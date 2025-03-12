from sqlalchemy import Column, DateTime, func

from infrastructure.models.common.soft_delete import SoftDeleteMixin


class CommonBaseModel(SoftDeleteMixin):
    created_at = Column(DateTime(True), nullable=False, default=func.now())
    updated_at = Column(DateTime(True), nullable=False, default=func.now(), onupdate=func.now())
