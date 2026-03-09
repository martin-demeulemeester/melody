from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from ..db import Base
from sqlalchemy import Date
from datetime import datetime, UTC


class Playlists(Base):
    __tablename__ = "playlists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, default=lambda: datetime.now(UTC), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

class PlaylistsTracks(Base):
    __tablename__ = "playlists_tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    playlist_id: Mapped[int] = mapped_column(ForeignKey('playlists.id'), nullable=False)
    track_id: Mapped[int] = mapped_column(ForeignKey('tracks.id'), nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
