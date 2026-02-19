import subprocess
from pathlib import Path
#from utils import ensure_dirs, DATA_DIR
from .utils import ensure_dirs, DATA_DIR


def download_audio(url: str, out_path: Path | None = None) -> Path:
    ensure_dirs()
    if out_path is None:
        out_path = DATA_DIR / "audio.mp3"

    cmd = [
        "yt-dlp",
        "-f", "ba",
        "-x",
        "--audio-format", "mp3",
        "-o", str(out_path),
        url
    ]

    # yt-dlp usa template en -o, así que si pasas "data/audio.mp3" queda exacto.
    subprocess.run(cmd, check=True)
    return out_path

if __name__ == "__main__":
    URL = "https://youtu.be/m38drn0ad6s?si=6G42_yB3tZ_DVsST"
    path = download_audio(URL)
    print(f"Audio guardado en: {path}")
