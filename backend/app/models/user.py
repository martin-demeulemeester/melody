from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date
from ..db import Base
from datetime import datetime, UTC

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, default=lambda: datetime.now(UTC), nullable=False)
