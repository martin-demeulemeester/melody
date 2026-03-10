from pathlib import Path

from sqlalchemy.orm import Session

from backend.app.config import DIR_PATH
from backend.app.db import engine
from backend.app.models import Artists, Albums, Tracks, User

with Session(engine) as session:
    user = User(username="Martin", password_hash="sigsfghisugfd1321")

    session.add(user)
    session.commit()
    session.refresh(user)

    artist = Artists(artist="C418")

    session.add(artist)
    session.commit()
    session.refresh(artist)

    album = Albums(title="Minecraft Volume Beta",artist_id=artist.id,image_path=None)

    session.add(album)
    session.commit()
    session.refresh(album)

    track = Tracks(title="Aria Math", artist_id=artist.id, album_id=album.id, image_path=None, duration=309161, file_path = str(Path(DIR_PATH / "music" / "C418 - Aria Math (Minecraft Volume Beta).opus")))

    session.add(track)
    session.commit()