# Capítulo 4: ROS2 — Scripts Python

Scripts del **Capítulo 4** de *Drones Autónomos II*.

## Prerrequisitos

- Ubuntu 22.04 LTS
- ROS2 Humble (instalar con `../install_ros2.sh`)
- MAVROS: `sudo apt install ros-humble-mavros ros-humble-mavros-msgs`
- Nav2: `sudo apt install ros-humble-nav2-bringup ros-humble-navigation2`

## Scripts Disponibles

| Script | Descripción |
|--------|-------------|
| `publisher_simple.py` | Nodo publicador básico — publica un String cada segundo |
| `subscriber_simple.py` | Nodo suscriptor básico — recibe y loguea mensajes |
| `controlador_dron.py` | Control de dron vía MAVROS: modo GUIDED + armar |
| `estado_vuelo_node.py` | Monitor de telemetría: suscribe a 4 tópicos MAVROS, publica JSON |
| `navegador_poi.py` | Navegador POI con Nav2: vuela a lista de coordenadas (x, y, z) |

## Uso

```bash
# Activar ROS2 antes de ejecutar cualquier script
source /opt/ros/humble/setup.bash

# Terminal 1 — publicador
python3 publisher_simple.py

# Terminal 2 — suscriptor (ejecutar simultáneamente)
python3 subscriber_simple.py

# Controlador de dron (requiere MAVROS + SITL activos)
python3 controlador_dron.py

# Monitor de estado (requiere MAVROS)
python3 estado_vuelo_node.py

# Navegador POI (requiere MAVROS + Nav2)
python3 navegador_poi.py
```

## Quick Start con SITL

```bash
# Terminal 1: Ardupilot SITL
sim_vehicle.py -v ArduCopter -l 37.416,-122.144,14,0 -w --console

# Terminal 2: puente MAVROS
ros2 launch mavros apm.launch fcu_url:=udp://@127.0.0.1:14550@

# Terminal 3: tu script
source /opt/ros/humble/setup.bash
python3 controlador_dron.py
```
