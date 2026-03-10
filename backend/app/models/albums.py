from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Date, ForeignKey
from ..db import Base


class Albums(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    artist_id: Mapped[int] = mapped_column(ForeignKey('artists.id'),nullable=False)
    image_path: Mapped[str] = mapped_column(nullable=True)