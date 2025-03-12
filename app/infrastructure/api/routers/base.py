from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.db import get_session_dependency


class BaseRouter:
    session: Session = Depends(get_session_dependency)
