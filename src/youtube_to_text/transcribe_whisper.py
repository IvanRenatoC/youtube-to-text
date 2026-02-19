import json
from pathlib import Path
import whisper

#from utils import ensure_dirs, DATA_DIR, OUTPUTS_DIR, fmt_time
from .utils import ensure_dirs, DATA_DIR, OUTPUTS_DIR, fmt_time


def transcribe(
    audio_path: Path | None = None,
    language: str = "es",
    model_name: str = "small"
) -> dict:
    ensure_dirs()

    if audio_path is None:
        audio_path = DATA_DIR / "audio.mp3"

    model = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path), language=language)

    # 1) texto plano
    (OUTPUTS_DIR / "transcripcion.txt").write_text(result["text"], encoding="utf-8")

    # 2) con tiempos (segmentos)
    lines = []
    for s in result.get("segments", []):
        start = fmt_time(s["start"])
        end = fmt_time(s["end"])
        lines.append(f"[{start} - {end}] {s['text'].strip()}")
    (OUTPUTS_DIR / "transcripcion_con_tiempos.txt").write_text("\n".join(lines), encoding="utf-8")

    # 3) json completo (útil para debug / repro)
    (OUTPUTS_DIR / "transcripcion.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    return result

if __name__ == "__main__":
    res = transcribe()
    print("OK. Archivos generados en outputs/")
