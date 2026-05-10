# Volumen 2 — Capítulo 3: IA en Drones

> **Recursos para el capítulo "Inteligencia Artificial Embarcada en Drones"**  
> **Nivel:** Avanzado  
> **Última actualización:** Mayo 2026

---

## 📦 Contenido

```
VOLUMEN-2/03-IA-Drones/
├── jetson_yolo_optimization.py    # ✅ Convertir YOLO a TensorRT
├── latency_benchmark.py            # ✅ Medir latencia de inferencia
├── power_monitoring.py             # ✅ Monitorear consumo energético
├── requirements.txt                # Dependencias Python
└── README.md                       # Este archivo
```

---

## ✅ Scripts Disponibles

| Script | Descripción | Estado |
|--------|-------------|--------|
| `jetson_yolo_optimization.py` | Conversión a TensorRT en Jetson Nano/Orin | ✅ Listo |
| `latency_benchmark.py` | Medir latencia de inferencia por modelo | ✅ Listo |
| `power_monitoring.py` | Monitoreo de consumo en tiempo real | ✅ Listo |

---

## 🚀 Guía de Uso

### Instalación Rápida

```bash
cd VOLUMEN-2/03-IA-Drones/
pip install -r requirements.txt
```

### 1️⃣ Optimización a TensorRT

Convierte un modelo YOLO a formato optimizado TensorRT (2-10x más rápido):

```bash
# Convertir y comparar latencia
python jetson_yolo_optimization.py --model yolov8n.pt

# Con más workspace para más velocidad
python jetson_yolo_optimization.py --model yolov8m.pt --workspace 4

# Solo hacer benchmark (sin convertir)
python jetson_yolo_optimization.py --model yolov8n.pt --benchmark-only
```

**Salida esperada:**
- Muestra latencia original vs TensorRT
- Calcula factor de aceleración
- Guarda modelo `.engine` para uso futuro

### 2️⃣ Análisis de Latencia

Mide latencia completa del pipeline desglosada por componente:

```bash
# Usar cámara web (requiere --source webcam)
python latency_benchmark.py --model yolov8n.pt --source webcam --frames 100

# Procesar video
python latency_benchmark.py --model yolov8n.pt --source video.mp4

# Usar imágenes dummy (sin hardware)
python latency_benchmark.py --model yolov8n.pt --source dummy --frames 200

# Exportar datos y gráficos
python latency_benchmark.py --model yolov8n.pt --export-csv latencies.csv --plot latency.png
```

**Desglose de latencia:**
- ⏱️ Captura: tiempo de lectura de cámara/archivo
- ⏱️ Preproceso: redimensionamiento y normalización
- ⏱️ Inferencia: forward pass del modelo
- ⏱️ Postproceso: extracción de detecciones

### 3️⃣ Monitoreo de Potencia

Mide consumo energético real durante inferencia (solo en Jetson con `jetson-stats`):

```bash
# Monitoreo básico
python power_monitoring.py --model yolov8n.pt --frames 100

# Monitoreo extendido (60 segundos)
python power_monitoring.py --model yolov8m.pt --duration 60

# Exportar datos
python power_monitoring.py --model yolov8n.pt --export-csv power.csv --plot power.png
```

**Información incluida:**
- Potencia media, mínima, máxima
- Energía consumida (Joules, Wh)
- Autonomía estimada en drones con diferentes baterías
- Temperatura de GPU (si disponible)

---

## 📋 Requisitos del Capítulo

### Hardware recomendado
- **NVIDIA Jetson Nano** (4 GB) o **Jetson Orin NX** (8 GB)
- Cámara CSI (Raspberry Pi Camera v2 o similar)
- Pixhawk 6C con Ardupilot 4.5+

### Software
```bash
# En Jetson: JetPack 5.1+ (incluye CUDA, cuDNN, TensorRT)
# Python 3.10+
pip install ultralytics pymavlink opencv-python numpy
```

### Verificar GPU disponible
```python
import torch
print(torch.cuda.is_available())   # True si Jetson tiene CUDA
print(torch.cuda.get_device_name()) # Nombre de la GPU
```

---

## 🚀 Mientras tanto: Usar scripts de OpenCV+YOLO

Los scripts del Capítulo 2 funcionan también como base para este capítulo:

```bash
# Desde la raíz del repositorio
cd VOLUMEN-2/02-OpenCV-YOLO/Python/

# Detección YOLO (funciona en CPU y GPU)
python yolo_detection.py n        # Nano — ideal para Jetson
python yolo_detection.py s        # Small
```

---

## 📖 Referencia al Libro

Este capítulo acompaña el **Volumen 2, Capítulo 3: IA en Drones** del libro  
*Drones Autónomos II: Robótica, Visión Artificial e IA Embarcada*.

Temas del capítulo en el libro:
- Diferencia entre IA en nube vs. IA embarcada
- Optimización de modelos con TensorRT (Jetson)
- Integración de inferencia con control de vuelo (MAVLink)
- Consumo energético y latencia en plataformas embarcadas

---

**Última actualización:** Abril 2026 | DroneBooks
