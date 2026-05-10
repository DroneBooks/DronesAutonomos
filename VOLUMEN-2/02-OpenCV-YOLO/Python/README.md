# Volumen 2 — Capítulo 2: OpenCV + YOLO

> **Recursos para el capítulo "Visión Artificial: OpenCV y YOLO en Drones"**  
> **Nivel:** Intermedio a Avanzado

---

## 📋 Descripción General

La visión por computador es crítica para drones autónomos. Este directorio contiene scripts para:
- Detección de colores (métodos clásicos)
- Detección de objetos con deep learning (YOLO v8)
- Procesamiento de imágenes en tiempo real

Incluye tanto métodos tradicionales como redes neuronales.

---

## 🛠️ Scripts Disponibles

### 1. **color_detection.py** — Detección de Colores HSV ⭐
Script interactivo que detecta colores específicos usando el espacio HSV.

```bash
python color_detection.py
```

**Colores soportados:**
- Rojo, Verde, Azul, Amarillo
- Rango HSV ajustable
- Máscara en tiempo real
- FPS mostrado

**Uso:** Ideal para principiantes aprendiendo procesamiento de imágenes.

---

### 2. **yolo_detection.py** — Detección YOLO v8 en Tiempo Real
Script que ejecuta YOLOv8 para detectar 80+ objetos.

```bash
python yolo_detection.py
```

**Características:**
- Detección de personas, vehículos, animales, etc
- Cuadros boundingbox alrededor de objetos
- Mostrador de FPS y latencia
- Confianza de detección

**Modelos disponibles:**
- `yolov8n.pt` (Nano - rápido, menos preciso)
- `yolov8s.pt` (Small - balance)
- `yolov8m.pt` (Medium - preciso, lento)

---

### 3. **examples/basic_detection.py** — Ejemplo Educativo
Script mínimo mostrando la estructura básica de detección.

```bash
python examples/basic_detection.py
```

---

## 📦 Instalación de Dependencias

**Paso 1:** Instalar dependencias
```bash
pip install -r requirements.txt
```

**Paso 2:** Descargar modelo YOLO (primera ejecución automática)
```bash
python yolo_detection.py
# Descargará yolov8n.pt (~6 MB)
```

**Dependencias principales:**
- `opencv-python` — Procesamiento de imágenes
- `numpy` — Cálculos numéricos
- `ultralytics` — Framework YOLO
- `torch` — Deep Learning

---

## 🧪 Prueba Básica

```bash
# Probar con webcam
python color_detection.py     # Presiona 'q' para salir
python yolo_detection.py

# Probar con imagen
python yolo_detection.py --image test.jpg

# Probar con video
python yolo_detection.py --video test.mp4
```

---

## 📊 Comparación: Métodos Clásicos vs YOLO

| Aspecto | HSV (Clásico) | YOLO v8 |
|---------|--------------|---------|
| **Velocidad** | 30-60 FPS | 10-60 FPS* |
| **Precisión** | Sensible luz | 80%+ mAP |
| **Flexibilidad** | 1 color/script | 80+ objetos |
| **Recursos** | CPU | GPU recomendado |
| **Complejidad** | Bajo | Medio-Alto |

*Depende de hardware y modelo

---

## 🔧 Optimización para Drones

Para ejecutar en hardware limitado (Jetson Nano):

```bash
# Usar modelo Nano
python yolo_detection.py --model yolov8n.pt

# Con FP16 (media precisión = más rápido)
python yolo_detection.py --half

# Reducir resolución
python yolo_detection.py --imgsz 320
```

---

## 🎓 Casos de Uso

1. **Detección de personas:** Seguridad, rescate, agricultura
2. **Mapeo aéreo:** Conteo de edificios, análisis de cultivos
3. **Inspección:** Buscar objetos/anomalías
4. **Tracking:** Seguir objetivos en movimiento

---

## ⚠️ Limitaciones

1. **Iluminación:** HSV muy sensible a cambios de luz
2. **Latencia:** YOLO añade 50-100ms (crítico en vuelo cercano)
3. **Recursos:** GPU recomendada para tiempo real en drone
4. **Precisión:** YOLO no es 100% (típicamente 80-90%)

---

## 🐛 Troubleshooting

**"No camera found"**
```bash
ls /dev/video*  # Linux
# Si nada sale, instala UVC:
sudo apt install libopencv-dev
```

**"YOLO model download failed"**
```bash
# Descargar manualmente
wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
```

**"Out of memory"**
- Usa modelo más pequeño (yolov8n)
- Reduce imgsz a 320
- Ejecuta en GPU si disponible

---

## 📈 Métricas de Rendimiento

Ejecutar `python yolo_detection.py` muestra:
- **FPS:** Frames procesados por segundo
- **Latencia:** Tiempo de detección en ms
- **Confianza:** % de certeza en detección

---

## 📚 Recursos

- **Libro:** *Drones Autónomos II*, Volumen 2, Capítulo 2 — disponible en Amazon KDP
- **Ultralytics YOLO:** https://github.com/ultralytics/ultralytics
- **OpenCV Docs:** https://docs.opencv.org/
- **NVIDIA Jetson:** https://docs.nvidia.com/jetson/

---

**Última actualización:** 16 Abril 2026  
**Autor:** DroneAcademy Team
