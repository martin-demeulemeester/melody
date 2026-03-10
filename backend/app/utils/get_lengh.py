"""Utility to get the duration/length of audio files."""
from pathlib import Path
from datetime import timedelta
from mutagen import File as MutagenFile


def get_audio_length(file_path: str | Path) -> timedelta | None:
    """
    Get the duration of an audio file.

    Args:
        file_path: Path to the audio file

    Returns:
        timedelta object with the duration, or None if unable to read
    """
    try:
        audio = MutagenFile(file_path)
        if audio is not None and audio.info is not None:
            duration_seconds = audio.info.length
            return timedelta(seconds=duration_seconds)
        return None
    except Exception as e:
        print(f"Error reading audio file {file_path}: {e}")
        return None


def get_audio_length_formatted(file_path: str | Path) -> str:
    """
    Get the duration of an audio file as a formatted string (HH:MM:SS).

    Args:
        file_path: Path to the audio file

    Returns:
        Formatted duration string (e.g., "00:03:45") or "Unknown" if unable to read
    """
    duration = get_audio_length(file_path)
    if duration is None:
        return "Unknown"

    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours > 0:
        return f"{duration}"
    else:
        return f"{duration}"


# Example usage
if __name__ == "__main__":
    # Example: Get length of music files in the music directory
    music_dir = Path(__file__).resolve().parents[3] / "music"

    if music_dir.exists():
        print("Audio file durations:")
        print("-" * 60)
        for audio_file in music_dir.glob("*.opus"):
            duration = get_audio_length_formatted(audio_file)
            print(f"{audio_file.name}: {duration}")
    else:
        print(f"Music directory not found: {music_dir}")
