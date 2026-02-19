# youtube-to-text

Pipeline simple para convertir un video de YouTube a texto:

1) Descargar audio desde YouTube (yt-dlp)
2) Transcribir con Whisper
3) Guardar outputs:
   - `outputs/transcripcion.txt`
   - `outputs/transcripcion_con_tiempos.txt`
   - `outputs/transcripcion.json`

> Este repo está pensado **principalmente para ejecutarse en la nube (Google Colab)**.
> La ejecución local es **opcional** para quien lo necesite.

---

## Estructura del repo

- `colab/`: notebook principal (Colab)
- `src/youtube_to_text/`: scripts reutilizables (paquete)
- `data/`: audio local (NO se sube a git)
- `outputs/`: resultados (NO se sube a git)

---

## Requisitos

### Google Colab (recomendado)
En una celda de Colab:

```bash
!apt-get -y update
!apt-get -y install ffmpeg
!pip -q install -r requirements.txt
