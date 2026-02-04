# youtube-to-text

Pipeline simple para convertir un video de YouTube a texto:
1) Descargar audio (yt-dlp)
2) Transcribir (Whisper)
3) Guardar outputs (txt / txt con tiempos / json)

## Estructura
- `colab/`: notebook principal
- `src/`: scripts reutilizables
- `data/`: audio local (NO se sube a git)
- `outputs/`: resultados

## Uso (local)
```bash
pip install -r requirements.txt
python src/download_audio.py
python src/transcribe_whisper.py
