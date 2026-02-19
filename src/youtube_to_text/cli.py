import argparse
from pathlib import Path

from .download_audio import download_audio
from .transcribe_whisper import transcribe


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube audio and transcribe to text using Whisper."
    )
    parser.add_argument("--url", required=True, help="YouTube video URL (full or youtu.be short link)")
    parser.add_argument(
        "--audio-out",
        default=None,
        help="Audio output path (e.g., data/audio.mp3). Default: data/audio.mp3",
    )
    parser.add_argument("--language", default="es", help="Language code (default: es)")
    parser.add_argument("--model", default="small", help="Whisper model: tiny/base/small/medium/large")

    args = parser.parse_args()

    audio_out = Path(args.audio_out) if args.audio_out else None

    # 1) Download audio
    try:
        audio_path = download_audio(args.url, out_path=audio_out)
    except Exception as e:
        raise SystemExit(
            "❌ Error descargando audio.\n"
            "- Revisa que la URL sea válida (no uses placeholders como VIDEO_ID).\n"
            "- Revisa que `yt-dlp` esté instalado y accesible en PATH.\n"
            f"Detalle: {e}"
        )

    # 2) Transcribe
    try:
        _ = transcribe(audio_path=audio_path, language=args.language, model_name=args.model)
    except Exception as e:
        raise SystemExit(
            "❌ Error transcribiendo con Whisper.\n"
            "- Revisa que `ffmpeg` esté instalado.\n"
            "- Revisa que `openai-whisper` esté instalado en tu entorno.\n"
            f"Detalle: {e}"
        )

    print(f"✅ Audio guardado en: {audio_path}")
    print("✅ Transcripción generada en: outputs/ (txt, txt con tiempos, json)")


if __name__ == "__main__":
    main()

