from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from ..db import Base

class Tracks(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    artist_id: Mapped[int] = mapped_column(ForeignKey('artists.id'), nullable=False)
    album_id: Mapped[int] = mapped_column(ForeignKey('albums.id'), nullable=True)
    image_path: Mapped[str] = mapped_column(nullable=True)
    duration: Mapped[int] = mapped_column(nullable=False)
    file_path: Mapped[str | None] = mapped_column(nullable=True)