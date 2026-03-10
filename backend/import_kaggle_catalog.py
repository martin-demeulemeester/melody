from pathlib import Path
import math

import pandas as pd
from sqlalchemy import select

from app.db import SessionLocal
from backend.app.config import DIR_PATH
from backend.app.models import Artists, Albums, Tracks


CSV_PATH = Path(DIR_PATH/"data/dataset.csv")


def normalize(text: str | None) -> str:
    if text is None:
        return ""
    return " ".join(str(text).strip().lower().split())


def clean_optional_text(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    text = str(value).strip()
    return text if text else None


def clean_int(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return None


def get_or_create_Artists(db, Artists_name: str) -> Artists:
    Artists_name = Artists_name.strip()
    stmt = select(Artists).where(Artists.artist == Artists_name)
    artist = db.scalar(stmt)
    if artist:
        return artist

    artist = Artists(artist=Artists_name)
    db.add(artist)
    db.flush()
    return artist


def get_or_create_Albums(db, Albums_title: str, artist_id: int) -> Albums:
    stmt = select(Albums).where(
        Albums.title == Albums_title,
        Albums.artist_id == artist_id,
    )
    album = db.scalar(stmt)
    if album:
        return album

    album = Albums(
        title=Albums_title,
        artist_id=artist_id,
        image_path=None,
    )
    db.add(album)
    db.flush()
    return album


def find_existing_Tracks(db, title: str, artist_id: int, album_id: int | None):
    if album_id is not None:
        stmt = select(Tracks).where(
            Tracks.title == title,
            Tracks.artist_id == artist_id,
            Tracks.album_id == album_id,
        )
        track = db.scalar(stmt)
        if track:
            return track

    return None


def import_catalog():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)

    # Adapt this mapping to your Kaggle dataset column names
    COLUMN_MAP = {
        "title": "track_name",
        "Artists": "artists",
        "Albums": "album_name",
        "duration": "duration_ms",
    }

    required = ["title", "Artists"]
    for key in required:
        source_col = COLUMN_MAP[key]
        if source_col not in df.columns:
            raise ValueError(f"Missing required column in CSV: {source_col}")

    db = SessionLocal()

    created_Artistss = 0
    created_Albumss = 0
    created_Tracks = 0
    updated_Tracks = 0
    skipped_rows = 0

    # simple caches to reduce DB queries
    artist_cache = {}
    album_cache = {}

    try:
        for _, row in df.iterrows():
            raw_title = clean_optional_text(row.get(COLUMN_MAP["title"]))
            raw_artist = clean_optional_text(row.get(COLUMN_MAP["Artists"]))
            raw_album = clean_optional_text(row.get(COLUMN_MAP["Albums"])) or "Unknown Albums"
            raw_duration = clean_int(row.get(COLUMN_MAP["duration"]))

            if not raw_title or not raw_artist:
                skipped_rows += 1
                continue

            title = raw_title.strip()
            artist_name = raw_artist.strip()
            album_title = raw_album.strip()

            artist_key = normalize(artist_name)
            if artist_key in artist_cache:
                artist = artist_cache[artist_key]
            else:
                existing_artist = db.scalar(select(Artists).where(Artists.artist == artist_name))
                if existing_artist:
                    artist = existing_artist
                else:
                    artist = Artists(artist=artist_name)
                    db.add(artist)
                    db.flush()
                    created_Artistss += 1
                artist_cache[artist_key] = artist

            album_key = (normalize(album_title), artist.id)
            if album_key in album_cache:
                album = album_cache[album_key]
            else:
                existing_album = db.scalar(
                    select(Albums).where(
                        Albums.title == album_title,
                        Albums.artist_id == artist.id,
                    )
                )
                if existing_album:
                    album = existing_album
                else:
                    album = Albums(
                        title=album_title,
                        artist_id=artist.id,
                        image_path=None,
                    )
                    db.add(album)
                    db.flush()
                    created_Albumss += 1
                album_cache[album_key] = album

            existing_track = find_existing_Tracks(
                db=db,
                title=title,
                artist_id=artist.id,
                album_id=album.id,
            )

            if existing_track:
                changed = False

                if existing_track.duration is None and raw_duration is not None:
                    existing_track.duration = raw_duration
                    changed = True

                if changed:
                    updated_Tracks += 1
                continue

            track = Tracks(
                title=title,
                artist_id=artist.id,
                album_id=album.id,
                duration=raw_duration,
                file_path=None,
                image_path=None,
            )
            db.add(track)
            created_Tracks += 1

        db.commit()

        print("=== IMPORT FINISHED ===")
        print(f"Artistss created : {created_Artistss}")
        print(f"Albumss created  : {created_Albumss}")
        print(f"Tracks created  : {created_Tracks}")
        print(f"Tracks updated  : {updated_Tracks}")
        print(f"Rows skipped    : {skipped_rows}")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    import_catalog()