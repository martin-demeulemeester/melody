from sqlalchemy.orm import Mapped, mapped_column
from ..db import Base

class Artists(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True)
    artist: Mapped[str] = mapped_column(nullable=False)