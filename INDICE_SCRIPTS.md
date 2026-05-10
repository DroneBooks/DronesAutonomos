# 📚 Índice de Scripts — DroneBooks

> **Repositorio:** `DronesAutonomos`  
> **Última actualización:** Mayo 2026  
> **Licencia:** Todos los derechos reservados — DroneBooks

Todos los scripts están organizados por **Volumen** y **Capítulo**, siguiendo exactamente
la numeración que aparece en los libros.

---

## 🗺️ Navegación Rápida

### Volumen 1 — *Drones Autónomos I: Hardware, Ardupilot y MAVLink*
- [Índice de contenidos (PDF)](VOLUMEN-1/indice_volumen1.pdf) — Preview antes de comprar
- [Capítulo 1: Hardware](#volumen-1--capítulo-1-hardware) — Calculadoras de especificaciones
- [Capítulo 2: Ardupilot](#volumen-1--capítulo-2-ardupilot) — Calibración y configuración
- [Capítulo 3: MAVLink](#volumen-1--capítulo-3-mavlink) — Telemetría y comunicación
- [Anexo A1: Git](#volumen-1--anexo-a1-git) — Referencia rápida de comandos
- [Anexo A2: Python](#volumen-1--anexo-a2-python) — Scripts educativos de Python

### Volumen 2 — *Drones Autónomos II: Robótica, Visión Artificial e IA Embarcada*
- [Índice de contenidos (PDF)](VOLUMEN-2/indice_volumen2.pdf) — Preview antes de comprar
- [Capítulo 1: ROS2](#volumen-2--capítulo-1-ros2) — Instalador y framework robótico
- [Capítulo 2: OpenCV + YOLO](#volumen-2--capítulo-2-opencv--yolo) — Visión artificial
- [Capítulo 3: IA en Drones](#volumen-2--capítulo-3-ia-en-drones) — IA embarcada en Jetson
- [Anexo A1: Git](#volumen-2--anexo-a1-git) — Git para proyectos ROS2
- [Anexo A2: C++](#volumen-2--anexo-a2-c) — Nodos ROS2 en C++

---

## 🚀 Cómo Empezar

```bash
# 1. Clonar el repositorio completo
git clone https://github.com/DroneBooks/DronesAutonomos.git
cd DronesAutonomos

# 2. Instalar dependencias globales
pip install -r requirements.txt

# 3. Ir al capítulo que estás leyendo, por ejemplo:
cd VOLUMEN-1/02-Ardupilot/Python/
python calibrate_sensors.py
```

---

## 📘 VOLUMEN 1 — Capítulo 1: Hardware

📁 **Ruta:** `VOLUMEN-1/01-Hardware/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `calculadora_empuje.py` | Calculadora interactiva de especificaciones | ✅ Listo |

### Calculadoras incluidas

```bash
cd VOLUMEN-1/01-Hardware/
python calculadora_empuje.py
```

**Menú de la calculadora:**
1. **Relación empuje/peso (T:W)** — ¿tiene potencia suficiente el drone?
2. **Tiempo de vuelo** — autonomía según batería y consumo
3. **Selección de motor (KV)** — rango de KV según categoría
4. **Velocidad de punta de hélice** — verificación de seguridad

**Sin dependencias externas** — solo Python 3.10+.

---

## 📘 VOLUMEN 1 — Capítulo 2: Ardupilot

📁 **Ruta:** `VOLUMEN-1/02-Ardupilot/Python/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `calibrate_sensors.py` | Asistente interactivo de calibración | ✅ Listo |
| `parameter_configurator.py` | Leer/escribir parámetros del FC | ✅ Listo |
| `conexion_basica.py` | Conexión y lectura de telemetría | ✅ Listo |
| `despegar_aterrizar.py` | Vuelo autónomo en modo GUIDED | ✅ Listo |
| `waypoint_simple.py` | Misión con 4 waypoints en cuadrado | ✅ Listo |
| `cambiar_modo.py` | Cambiar modos de vuelo remotamente | ✅ Listo |
| `geofence_definir.py` | Crear límites virtuales de vuelo | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-1/02-Ardupilot/Python/
pip install -r requirements.txt

# Calibrar sensores (con FC conectado)
python calibrate_sensors.py

# Vuelo en SITL (simulación)
python conexion_basica.py --connect 127.0.0.1:14550
python despegar_aterrizar.py --connect 127.0.0.1:14550 --alt 10 --time 5
python waypoint_simple.py --connect 127.0.0.1:14550 --alt 25
```

### Conexiones Soportadas

| Tipo | Cadena de conexión |
|------|-------------------|
| SITL (simulación) | `127.0.0.1:14550` |
| USB Linux | `/dev/ttyUSB0` |
| USB Windows | `COM3` |
| Telemetría radio | `127.0.0.1:14551` |

---

## 📘 VOLUMEN 1 — Capítulo 3: MAVLink

📁 **Ruta:** `VOLUMEN-1/03-MAVLink/Python/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `telemetry_reader.py` | Lector continuo de telemetría MAVLink | ✅ Listo |
| `leer_telemetria_avanzada.py` | Telemetría completa con exportación CSV | ✅ Listo |
| `examples/connect_to_fc.py` | Ejemplo mínimo de conexión MAVLink | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-1/03-MAVLink/Python/
pip install -r requirements.txt

# Leer telemetría en tiempo real (SITL)
python telemetry_reader.py 127.0.0.1:14550 60

# Telemetría avanzada con exportación a CSV
python leer_telemetria_avanzada.py --connect 127.0.0.1:14550

# Ejemplo básico de conexión
python examples/connect_to_fc.py 127.0.0.1:14550
```

---

## 📘 VOLUMEN 1 — Anexo A1: Git

📁 **Ruta:** `VOLUMEN-1/Anexos/A1-Git/`

### Contenido

El Anexo A1 no incluye scripts Python — Git es la herramienta en sí misma.
El `README.md` contiene una **referencia rápida de todos los comandos** del capítulo:
- Configuración inicial, flujo básico, ramas, repositorios remotos
- Estructura de proyecto recomendada para drones
- `.gitignore` para proyectos Python

```bash
cat VOLUMEN-1/Anexos/A1-Git/README.md
```

---

## 📘 VOLUMEN 1 — Anexo A2: Python

📁 **Ruta:** `VOLUMEN-1/Anexos/A2-Python/`

### Archivos Disponibles

| Archivo | Descripción | Nivel | Estado |
|---------|-------------|-------|--------|
| `telemetry_basic.py` | Lectura básica de GPS, batería y actitud | Principiante | ✅ Listo |
| `color_detection_simple.py` | Detección de color rojo con OpenCV | Principiante | ✅ Listo |
| `advanced_example.py` | Telemetría + visión en paralelo (threads) | Intermedio | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-1/Anexos/A2-Python/
pip install -r requirements.txt

# Script 1 — Telemetría básica (necesita SITL o FC real)
python telemetry_basic.py

# Script 2 — Detección de color (necesita cámara)
python color_detection_simple.py

# Script 3 — Ejemplo avanzado (ambos en paralelo)
python advanced_example.py
```

---

## 📗 VOLUMEN 2 — Capítulo 1: ROS2

📁 **Ruta:** `VOLUMEN-2/01-ROS2/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `install_ros2.sh` | Instalador automático de ROS2 Humble | ✅ Listo |
| `Python/publisher_simple.py` | Nodo publicador básico (pub/sub demo) | ✅ Listo |
| `Python/subscriber_simple.py` | Nodo suscriptor básico (pub/sub demo) | ✅ Listo |
| `Python/controlador_dron.py` | Control de dron vía MAVROS: GUIDED + armar | ✅ Listo |
| `Python/estado_vuelo_node.py` | Monitor de telemetría: 4 tópicos MAVROS → JSON | ✅ Listo |
| `Python/navegador_poi.py` | Navegación a Puntos de Interés con Nav2 | ✅ Listo |

### Uso

```bash
# Instalar ROS2 Humble completo en Ubuntu 22.04
bash VOLUMEN-2/01-ROS2/install_ros2.sh

# Verificar instalación
source /opt/ros/humble/setup.bash
ros2 --version

# Ejecutar demos pub/sub (dos terminales)
cd VOLUMEN-2/01-ROS2/Python/
source /opt/ros/humble/setup.bash
python3 publisher_simple.py    # Terminal 1
python3 subscriber_simple.py   # Terminal 2

# Control de dron (requiere MAVROS + SITL)
python3 controlador_dron.py

# Monitor de telemetría (requiere MAVROS)
python3 estado_vuelo_node.py
```

El instalador incluye: ROS2 Humble Desktop, colcon, dependencias Python y configura el `.bashrc`.

---

## 📗 VOLUMEN 2 — Capítulo 2: OpenCV + YOLO

📁 **Ruta:** `VOLUMEN-2/02-OpenCV-YOLO/Python/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `color_detection.py` | Detección HSV multi-color configurable | ✅ Listo |
| `yolo_detection.py` | Detección de objetos con YOLO v8 | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-2/02-OpenCV-YOLO/Python/
pip install -r requirements.txt

# Detección de color (elige: red, green, blue, yellow)
python color_detection.py red

# YOLO en webcam (modelos: n, s, m, l, x)
python yolo_detection.py n          # Nano — rápido, pocos recursos
python yolo_detection.py m          # Medium — equilibrado

# YOLO en archivo de video
python yolo_detection.py n video.mp4
```

### Rendimiento de Modelos YOLO

| Modelo | GPU (RTX) | CPU (i7) | Jetson Nano |
|--------|-----------|----------|-------------|
| Nano (n) | ~60 FPS | ~8 FPS | ~12 FPS |
| Small (s) | ~45 FPS | ~4 FPS | ~7 FPS |
| Medium (m) | ~30 FPS | ~2 FPS | ~3 FPS |

> **Nota:** Primera ejecución descarga el modelo (~6-50 MB según tamaño).

---

## 📗 VOLUMEN 2 — Capítulo 3: IA en Drones

📁 **Ruta:** `VOLUMEN-2/03-IA-Drones/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `jetson_yolo_optimization.py` | Convertir YOLO a TensorRT y comparar latencia | ✅ Listo |
| `latency_benchmark.py` | Análisis detallado de latencia (captura, preproceso, inferencia, postproceso) | ✅ Listo |
| `power_monitoring.py` | Monitoreo de consumo energético en Jetson (real o estimado) | ✅ Listo |
| `drone_person_follower.py` | Dron que sigue personas con YOLO + estimación de distancia + control PID | ✅ Listo |
| `mission_analyzer.py` | Análisis post-misión: reportes, timeline y exportación GPS de detecciones | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-2/03-IA-Drones/
pip install -r requirements.txt

# Optimizar modelo a TensorRT y medir mejora
python jetson_yolo_optimization.py --model yolov8n.pt

# Analizar latencia completa
python latency_benchmark.py --model yolov8n.pt --source dummy --frames 100

# Monitorear consumo de potencia
python power_monitoring.py --model yolov8n.pt --frames 100 --export-csv power.csv
```

### Conceptos Clave (del Capítulo)

- **TensorRT:** Motor de inferencia de NVIDIA que acelera 2-10x modelos YOLO
- **Latencia:** Tiempo total del pipeline (< 100ms recomendado para drones)
- **Potencia:** Consumo energético en plataformas embarcadas (crítico para autonomía)

---

## 📗 VOLUMEN 2 — Anexo A1: Git

📁 **Ruta:** `VOLUMEN-2/Anexos/A1-Git/`

Referencia rápida de Git aplicada a proyectos **ROS2 y C++**.
Incluye `.gitignore` específico para ROS2 y estructura recomendada de paquetes.

```bash
cat VOLUMEN-2/Anexos/A1-Git/README.md
```

---

## 📗 VOLUMEN 2 — Anexo A2: C++

📁 **Ruta:** `VOLUMEN-2/Anexos/A2-Cpp/`

### Archivos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `nodo_publisher.cpp` | Nodo ROS2 publicador de telemetría (altitud, batería, velocidad) | ✅ Listo |
| `nodo_subscriber.cpp` | Nodo ROS2 suscriptor con lógica de control y alertas | ✅ Listo |
| `bridge_mavlink.cpp` | Puente MAVLink ↔ ROS2 para integración con Pixhawk | ✅ Listo |
| `CMakeLists.txt` | Plantilla de compilación para nodos C++ en ROS2 | ✅ Listo |

### Uso Típico

```bash
cd VOLUMEN-2/Anexos/A2-Cpp/

# Preparar workspace ROS2
mkdir -p ~/ros2_ws/src
cp -r . ~/ros2_ws/src/drone_telemetry

# Compilar
cd ~/ros2_ws
colcon build --packages-select drone_telemetry

# Ejecutar nodos
source install/setup.bash
ros2 run drone_telemetry nodo_publisher    # Terminal 1
ros2 run drone_telemetry nodo_subscriber   # Terminal 2
ros2 run drone_telemetry bridge_mavlink    # Terminal 3 (opcional)
```

### Conceptos Clave (del Anexo)

- **ROS2 Nodes:** Procesos independientes que comunican via tópicos
- **Publishers/Subscribers:** Patrones pub-sub para telemetría y comandos
- **MAVLink Bridge:** Traducción entre protocolo binario y tópicos ROS2
- **CMake:** Sistema de compilación para proyectos C++ complejos

---

## 📦 Estructura Completa del Repositorio

```
DronesAutonomos/
│
├── README.md                           ← Punto de entrada
├── INDICE_SCRIPTS.md                   ← Este archivo
├── requirements.txt                    ← Dependencias globales
│
├── VOLUMEN-1/                          # Drones Autónomos I
│   ├── indice_volumen1.pdf             📄 Índice completo (preview)
│   ├── 01-Hardware/
│   │   ├── README.md
│   │   └── calculadora_empuje.py       ✅
│   ├── 02-Ardupilot/Python/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── calibrate_sensors.py        ✅
│   │   ├── parameter_configurator.py   ✅
│   │   ├── conexion_basica.py          ✅
│   │   ├── despegar_aterrizar.py       ✅
│   │   ├── waypoint_simple.py          ✅
│   │   ├── cambiar_modo.py             ✅
│   │   └── geofence_definir.py         ✅
│   ├── 03-MAVLink/Python/
│   │   ├── README.md
│   │   ├── requirements.txt
│   │   ├── telemetry_reader.py         ✅
│   │   ├── leer_telemetria_avanzada.py ✅
│   │   └── examples/
│   │       └── connect_to_fc.py        ✅
│   └── Anexos/
│       ├── A1-Git/
│       │   └── README.md               ✅ Referencia rápida
│       └── A2-Python/
│           ├── README.md
│           ├── requirements.txt
│           ├── telemetry_basic.py       ✅
│           ├── color_detection_simple.py ✅
│           └── advanced_example.py      ✅
│
└── VOLUMEN-2/                          # Drones Autónomos II
    ├── indice_volumen2.pdf             📄 Índice completo (preview)
    ├── 01-ROS2/
    │   ├── install_ros2.sh             ✅
    │   └── Python/
    │       ├── README.md               ✅
    │       ├── publisher_simple.py     ✅
    │       ├── subscriber_simple.py    ✅
    │       ├── controlador_dron.py     ✅
    │       ├── estado_vuelo_node.py    ✅
    │       └── navegador_poi.py        ✅
    ├── 02-OpenCV-YOLO/Python/
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── color_detection.py          ✅
    │   └── yolo_detection.py           ✅
    ├── 03-IA-Drones/
    │   ├── README.md                   ✅
    │   ├── requirements.txt            ✅
    │   ├── jetson_yolo_optimization.py ✅
    │   ├── latency_benchmark.py        ✅
    │   ├── power_monitoring.py         ✅
    │   ├── drone_person_follower.py    ✅
    │   └── mission_analyzer.py         ✅
    └── Anexos/
        ├── A1-Git/
        │   └── README.md               ✅ Referencia rápida ROS2
        └── A2-Cpp/
            ├── README.md               ✅
            ├── CMakeLists.txt          ✅
            ├── nodo_publisher.cpp      ✅
            ├── nodo_subscriber.cpp     ✅
            └── bridge_mavlink.cpp      ✅
```

---

## ⚙️ Requisitos Globales

| Componente | Versión mínima |
|------------|---------------|
| Python | 3.10+ |
| Ubuntu (recomendado) | 22.04 LTS |
| ROS2 (solo Vol.2 Cap.1+) | Humble |
| GPU (solo YOLO con velocidad) | NVIDIA con CUDA |

---

## 🐛 Problemas Frecuentes

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Cannot connect to 127.0.0.1:14550"
```bash
# Inicia SITL primero
sim_vehicle.py -v ArduCopter --location=-35.362882,149.165230,584,0
```

### "Camera not found"
```bash
ls /dev/video*   # Linux — identifica tu cámara
```

### "Port /dev/ttyUSB0 not found"
```bash
ls /dev/tty*     # Linux
```

---

## 📞 Soporte

- **Issues:** https://github.com/DroneBooks/DronesAutonomos/issues


---

**© 2026 DroneBooks — Todos los derechos reservados**
