# ANEXO Python — Scripts Educativos

> **Scripts educativos de Python enfocados en drones**  
> **Nivel:** Principiante → Intermedio

---

## 📦 Contenido

```
Anexos/A2-Python/
├── README.md
├── requirements.txt
├── telemetry_basic.py              # ✅ Lectura básica de telemetría
├── color_detection_simple.py       # ✅ Detección de color HSV simple
└── advanced_example.py             # ✅ Telemetría + Visión en paralelo
```

---

## 🛠️ Scripts Disponibles

### 1. **telemetry_basic.py** — Lectura de Telemetría Básica ⭐
Script simple (30 líneas) para leer datos de GPS, Batería y Actitud.

```bash
python telemetry_basic.py
```

**Propósito:** Aprender a conectarse a un Flight Controller y leer datos.

**Datos capturados (30 segundos):**
- GPS: Latitud, Longitud, Altitud
- Batería: Voltaje, Corriente, % restante
- Actitud: Roll, Pitch, Yaw

**Ideal para:** Primeros pasos en comunicación drone-PC

---

### 2. **color_detection_simple.py** — Detección de Color HSV
Script educativo que detecta color rojo en tiempo real desde webcam.

```bash
python color_detection_simple.py
```

**Características:**
- Detección automática de color rojo
- Filtrado de ruido
- Muestra contornos y centroides detectados
- FPS en tiempo real

**Controles:**
- `q` — Salir
- `c` — Calibrar color (clic en imagen)

**Ideal para:** Aprender OpenCV y procesamiento de imágenes

---

### 3. **advanced_example.py** — Telemetría + Visión en Paralelo ⭐⭐
Ejemplo avanzado que combina pymavlink y OpenCV usando threads,
con registro automático de datos en CSV.

```bash
python advanced_example.py
```

**Características:**
- Telemetría MAVLink y visión OpenCV ejecutándose simultáneamente
- Threads independientes para cada módulo
- Detección de objetos rojos con anotación de altitud y batería
- Log CSV: `telemetry_vision_log.csv`
- Duración configurable (60 segundos por defecto)

**Controles:**
- `q` — Salir antes del tiempo límite

**Ideal para:** Prepararse para el Proyecto Integrador del Anexo Python

---

## 📦 Instalación

```bash
# Paso 1: Instalar dependencias
pip install -r requirements.txt

# Paso 2: Ejecutar un script
python telemetry_basic.py
```

**Dependencias:**
- `pymavlink` — Comunicación MAVLink
- `opencv-python` — Visión por computador
- `numpy` — Cálculos numéricos

---

## 🧪 Prueba Rápida

### Opción 1: Sin hardware (Simulador)
```bash
# Terminal 1: Iniciar SITL
cd ~/ardupilot
./Tools/autotest/sim_vehicle.py -v ArduCopter

# Terminal 2: Ejecutar telemetría
python telemetry_basic.py
```

### Opción 2: Solo OpenCV
```bash
python color_detection_simple.py
# Usa webcam integrada
```

---

## 🎓 Contenido del ANEXO Python

| Lección | Tema | Duración |
|---------|------|----------|
| P.1 | Introducción a Python | 10 min |
| P.2 | Instalación y Setup | 15 min |
| P.3 | Variables y Tipos | 15 min |
| P.4 | Funciones y Módulos | 20 min |
| P.5 | Librerías de Drones | 20 min |
| P.6 | Proyecto: Telemetría | 25 min |

**Total:** ~90 minutos de video

---

## 🔌 Conexión a Flight Controller

Scripts soportan:
- **SITL (simulación):** `127.0.0.1:14550`
- **USB:** `/dev/ttyUSB0` (Linux) o `COM3` (Windows)
- **Baudrate:** 57600 o 115200

---

## ⚠️ Requisitos

- Python 3.10+
- Conexión a SITL o Flight Controller (telemetry_basic.py)
- Cámara conectada (color_detection_simple.py)

---

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'pymavlink'"**
```bash
pip install -r requirements.txt --upgrade
```

**"Cannot connect to 127.0.0.1:14550"**
- Verifica que SITL está ejecutándose
- Intenta puerto 14551 si hay múltiples instancias

**"Camera not found"**
- Verifica que tienes webcam conectada
- En Linux: `ls /dev/video*`

---

## 📚 Recursos

- **Libro:** *Drones Autónomos I*, Volumen 1, Anexo A2 — disponible en Amazon KDP
- **PyMavLink Docs:** https://mavlink.io/
- **OpenCV Tutorials:** https://docs.opencv.org/

---

**Última actualización:** 16 Abril 2026  
**Autor:** DroneAcademy Team

