# 📚 Drones Autónomos — Recursos de Código

**Recursos complementarios para los libros Volumen 1: 'Drones Autónomos I:
Hardware, Ardupilot, MAVLink' y Volumen 2: 'Drones Autónomos II
Robótica, Visión Artificial, IA'**

[![GitHub](https://img.shields.io/badge/GitHub-DroneBooks-blue?logo=github)](https://github.com/DroneBooks)
![License](https://img.shields.io/badge/License-Todos%20los%20derechos%20reservados-red)

---

## 📖 Sobre este repositorio

Este repositorio contiene todos los **scripts de ejemplo, código de referencia, datos de entrenamiento e instaladores** que acompañan a los dos volúmenes principales de DroneBooks.

### 🎯 Audiencia
- Ingenieros junior/mid especializándose en drones autónomos
- Makers avanzados con experiencia en electrónica y programación
- Estudiantes de Ingeniería en Robótica e Informática

---

## 📄 Índice de Contenidos (Preview)

Antes de comprar, puedes consultar el índice completo de cada volumen:

| Volumen | PDF | Páginas |
|---------|-----|---------|
| Drones Autónomos I | [indice_volumen1.pdf](VOLUMEN-1/indice_volumen1.pdf) | 7 pp. |
| Drones Autónomos II | [indice_volumen2.pdf](VOLUMEN-2/indice_volumen2.pdf) | 7 pp. |

---

## 📁 Estructura del Repositorio

```
DronesAutonomos/
│
├── VOLUMEN-1/                      # Drones Autónomos I
│   ├── indice_volumen1.pdf         # Índice completo de contenidos (preview)
│   ├── 01-Hardware/
│   │   └── calculadora_empuje.py   # T:W, tiempo de vuelo, KV, hélice
│   ├── 02-Ardupilot/Python/        # 7 scripts: calibrar, waypoints, etc.
│   ├── 03-MAVLink/Python/          # telemetría, leer_telemetria_avanzada
│   └── Anexos/
│       ├── A1-Git/                 # Referencia rápida de comandos Git
│       └── A2-Python/              # 3 scripts: telemetría, color, avanzado
│
├── VOLUMEN-2/                      # Drones Autónomos II
│   ├── indice_volumen2.pdf         # Índice completo de contenidos (preview)
│   ├── 01-ROS2/
│   │   ├── install_ros2.sh         # Instalador automático ROS2 Humble
│   │   └── Python/                 # 5 nodos: publisher, subscriber, controlador, estado, POI
│   ├── 02-OpenCV-YOLO/Python/      # color_detection.py, yolo_detection.py
│   ├── 03-IA-Drones/               # 5 scripts: optimización, latencia, potencia, seguidor, análisis
│   └── Anexos/
│       ├── A1-Git/                 # Git para proyectos ROS2
│       └── A2-Cpp/                 # 4 scripts: publisher, subscriber, bridge MAVLink, CMakeLists
│
├── README.md                       (Este archivo)
├── INDICE_SCRIPTS.md               (Catálogo completo con rutas y ejemplos)
└── requirements.txt                (Dependencias Python globales)
```

---

## 🚀 Quick Start

### Para Volumen 1 (Fundamentos)
```bash
# 1. Clonar el repo
git clone https://github.com/DroneBooks/DronesAutonomos.git
cd DronesAutonomos

# 2. Instalar dependencias Python
pip install -r requirements.txt

# 3. Ir a scripts del Volumen 1
cd VOLUMEN-1/02-Ardupilot/Python
python3 calibrate_sensors.py
```

### Para Volumen 2 (Robótica & IA)
```bash
# 1. Clonar el repo
git clone https://github.com/DroneBooks/DronesAutonomos.git
cd DronesAutonomos

# 2. Instalar ROS2 Humble
bash VOLUMEN-2/01-ROS2/install_ros2.sh

# 3. Probar visión artificial
cd VOLUMEN-2/02-OpenCV-YOLO/Python
python3 yolo_detection.py
```

---

## 📚 Flujo de Aprendizaje

### Volumen 1 — *Drones Autónomos I: Hardware, Ardupilot y MAVLink*
```
Lee Capítulo 1 (Hardware)
    ↓
Prueba: VOLUMEN-1/01-Hardware/calculadora_empuje.py
    ↓
Lee Capítulo 2 (Ardupilot)
    ↓
Ejecuta: VOLUMEN-1/02-Ardupilot/Python/calibrate_sensors.py
         VOLUMEN-1/02-Ardupilot/Python/waypoint_simple.py
    ↓
Lee Capítulo 3 (MAVLink)
    ↓
Ejecuta: VOLUMEN-1/03-MAVLink/Python/telemetry_reader.py
         VOLUMEN-1/03-MAVLink/Python/leer_telemetria_avanzada.py
    ↓
Lee Anexo A1 (Git) — referencia: VOLUMEN-1/Anexos/A1-Git/README.md
    ↓
Lee Anexo A2 (Python)
    ↓
Ejecuta: VOLUMEN-1/Anexos/A2-Python/telemetry_basic.py
         VOLUMEN-1/Anexos/A2-Python/advanced_example.py
```

### Volumen 2 — *Drones Autónomos II: Robótica, Visión Artificial e IA Embarcada*
```
Lee Capítulo 1 (ROS2)
    ↓
Ejecuta: bash VOLUMEN-2/01-ROS2/install_ros2.sh
         VOLUMEN-2/01-ROS2/Python/publisher_simple.py
         VOLUMEN-2/01-ROS2/Python/controlador_dron.py
         VOLUMEN-2/01-ROS2/Python/estado_vuelo_node.py
    ↓
Lee Capítulo 2 (OpenCV + YOLO)
    ↓
Ejecuta: VOLUMEN-2/02-OpenCV-YOLO/Python/color_detection.py red
         VOLUMEN-2/02-OpenCV-YOLO/Python/yolo_detection.py n
    ↓
Lee Capítulo 3 (IA en Drones)
    ↓
Ejecuta: VOLUMEN-2/03-IA-Drones/jetson_yolo_optimization.py
         VOLUMEN-2/03-IA-Drones/latency_benchmark.py
         VOLUMEN-2/03-IA-Drones/power_monitoring.py
         VOLUMEN-2/03-IA-Drones/drone_person_follower.py
         VOLUMEN-2/03-IA-Drones/mission_analyzer.py
    ↓
Lee Anexo A1 (Git) — referencia: VOLUMEN-2/Anexos/A1-Git/README.md
    ↓
Lee Anexo A2 (C++)
    ↓
Ejecuta: VOLUMEN-2/Anexos/A2-Cpp/nodo_publisher.cpp (compilar + ejecutar)
         VOLUMEN-2/Anexos/A2-Cpp/nodo_subscriber.cpp
         VOLUMEN-2/Anexos/A2-Cpp/bridge_mavlink.cpp
```

---

## 🔧 Scripts Disponibles

### VOLUMEN-1 — *Drones Autónomos I*
| Recurso | Capítulo / Anexo | Ruta | Descripción |
|---------|-----------------|------|-------------|
| `calculadora_empuje.py` | Cap. 1: Hardware | `VOLUMEN-1/01-Hardware/` | T:W, vuelo, KV, hélice |
| `calibrate_sensors.py` | Cap. 2: Ardupilot | `VOLUMEN-1/02-Ardupilot/Python/` | Calibra IMU, brújula, ESC |
| `parameter_configurator.py` | Cap. 2: Ardupilot | `VOLUMEN-1/02-Ardupilot/Python/` | Lee/escribe parámetros del FC |
| `conexion_basica.py` | Cap. 2-3 | `VOLUMEN-1/02-Ardupilot/Python/` | Conexión y telemetría básica |
| `despegar_aterrizar.py` | Cap. 2-3 | `VOLUMEN-1/02-Ardupilot/Python/` | Vuelo autónomo en GUIDED |
| `waypoint_simple.py` | Cap. 2-3 | `VOLUMEN-1/02-Ardupilot/Python/` | Misión con 4 waypoints |
| `cambiar_modo.py` | Cap. 2-3 | `VOLUMEN-1/02-Ardupilot/Python/` | Cambio de modos de vuelo |
| `geofence_definir.py` | Cap. 2-3 | `VOLUMEN-1/02-Ardupilot/Python/` | Límite virtual de vuelo |
| `telemetry_reader.py` | Cap. 3: MAVLink | `VOLUMEN-1/03-MAVLink/Python/` | Telemetría en tiempo real |
| `leer_telemetria_avanzada.py` | Cap. 3: MAVLink | `VOLUMEN-1/03-MAVLink/Python/` | Telemetría + exportación CSV |
| `README.md` | Anexo A1: Git | `VOLUMEN-1/Anexos/A1-Git/` | Referencia rápida de Git |
| `telemetry_basic.py` | Anexo A2: Python | `VOLUMEN-1/Anexos/A2-Python/` | Telemetría básica educativa |
| `color_detection_simple.py` | Anexo A2: Python | `VOLUMEN-1/Anexos/A2-Python/` | Detección de color HSV |
| `advanced_example.py` | Anexo A2: Python | `VOLUMEN-1/Anexos/A2-Python/` | Telemetría + visión en paralelo |

### VOLUMEN-2 — *Drones Autónomos II*
| Recurso | Capítulo / Anexo | Ruta | Descripción |
|---------|-----------------|------|-------------|
| `install_ros2.sh` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/` | Instalador ROS2 Humble |
| `publisher_simple.py` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/Python/` | Nodo publicador básico |
| `subscriber_simple.py` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/Python/` | Nodo suscriptor básico |
| `controlador_dron.py` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/Python/` | Control GUIDED + armar vía MAVROS |
| `estado_vuelo_node.py` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/Python/` | Monitor telemetría (4 tópicos → JSON) |
| `navegador_poi.py` | Cap. 1: ROS2 | `VOLUMEN-2/01-ROS2/Python/` | Navegación POI con Nav2 |
| `color_detection.py` | Cap. 2: OpenCV+YOLO | `VOLUMEN-2/02-OpenCV-YOLO/Python/` | Detección HSV multi-color |
| `yolo_detection.py` | Cap. 2: OpenCV+YOLO | `VOLUMEN-2/02-OpenCV-YOLO/Python/` | Detección objetos YOLOv8 |
| `jetson_yolo_optimization.py` | Cap. 3: IA Drones | `VOLUMEN-2/03-IA-Drones/` | Optimización TensorRT |
| `latency_benchmark.py` | Cap. 3: IA Drones | `VOLUMEN-2/03-IA-Drones/` | Medición de latencia |
| `power_monitoring.py` | Cap. 3: IA Drones | `VOLUMEN-2/03-IA-Drones/` | Monitoreo de potencia |
| `drone_person_follower.py` | Cap. 3: IA Drones | `VOLUMEN-2/03-IA-Drones/` | Seguidor de personas |
| `mission_analyzer.py` | Cap. 3: IA Drones | `VOLUMEN-2/03-IA-Drones/` | Análisis post-misión |
| `README.md` | Anexo A1: Git | `VOLUMEN-2/Anexos/A1-Git/` | Git para proyectos ROS2 |
| `nodo_publisher.cpp` | Anexo A2: C++ | `VOLUMEN-2/Anexos/A2-Cpp/` | Publicador ROS2 |
| `nodo_subscriber.cpp` | Anexo A2: C++ | `VOLUMEN-2/Anexos/A2-Cpp/` | Suscriptor ROS2 |
| `bridge_mavlink.cpp` | Anexo A2: C++ | `VOLUMEN-2/Anexos/A2-Cpp/` | Puente MAVLink-ROS2 |
| `CMakeLists.txt` | Anexo A2: C++ | `VOLUMEN-2/Anexos/A2-Cpp/` | Compilación C++ ROS2 |

Ver **INDICE_SCRIPTS.md** para lista completa con detalles.

---

## ⚙️ Requisitos del Sistema

### Hardware Mínimo
- **CPU:** Intel i5 / Ryzen 5 (simulación)
- **RAM:** 8 GB
- **GPU:** RTX 3060+ (recomendado para YOLO)
- **Drone:** Pixhawk 6C con Ardupilot 4.5+

### Software
- **OS:** Ubuntu 22.04 LTS (recomendado)
- **Python:** 3.10+
- **Git:** para clonar este repo
- **ROS2:** Humble (instalador incluido en VOLUMEN-2/01-ROS2/)

---

## 📞 Contacto & Soporte

- **GitHub:** [@DroneBooks](https://github.com/DroneBooks)
- **Issues/Preguntas:** https://github.com/DroneBooks/DronesAutonomos/issues


---

**Versión:** 1.1 | **Última actualización:** 3 Mayo 2026

