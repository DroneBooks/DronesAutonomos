# CMakeLists.txt — Plantilla de compilación para nodos ROS2 en C++
#
# Este archivo configura la compilación de nodos ROS2 usando CMake y colcon.
#
# Conceptos clave (del Anexo A2):
# - cmake_minimum_required: versión mínima de CMake
# - project(): nombre y versión del paquete
# - find_package(): buscar dependencias instaladas
# - add_executable(): compilar archivo .cpp a ejecutable
# - ament_target_dependencies(): linkar dependencias ROS2
# - install(): copiar ejecutables a install/lib/
# - ament_package(): finalizar definición del paquete
#
# Compilación:
#   cd ~/ros2_ws
#   colcon build --packages-select drone_telemetry
#
# Limpieza (si hay errores):
#   rm -rf build/ install/ log/
#   colcon build --packages-select drone_telemetry

cmake_minimum_required(VERSION 3.16)
project(drone_telemetry)

# Estándar C++ (14 mínimo para ROS2, 17 recomendado para características modernas)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Buscar dependencias ROS2
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# ============================================================
# NODO 1: Publicador de Telemetría
# ============================================================
# Compilar nodo_publisher.cpp a ejecutable "nodo_publisher"
add_executable(nodo_publisher src/nodo_publisher.cpp)

# Linkar dependencias ROS2 necesarias
ament_target_dependencies(nodo_publisher
  rclcpp
  std_msgs
)

# ============================================================
# NODO 2: Suscriptor de Telemetría
# ============================================================
add_executable(nodo_subscriber src/nodo_subscriber.cpp)

ament_target_dependencies(nodo_subscriber
  rclcpp
  std_msgs
)

# ============================================================
# NODO 3: Puente MAVLink (opcional, si existe bridge_mavlink.cpp)
# ============================================================
# Descomentar cuando se implemente bridge_mavlink.cpp
# find_package(pymavlink REQUIRED)
# add_executable(bridge_mavlink src/bridge_mavlink.cpp)
# ament_target_dependencies(bridge_mavlink rclcpp std_msgs pymavlink)

# ============================================================
# Instalación
# ============================================================
# Copiar ejecutables compilados a install/lib/drone_telemetry/
install(TARGETS
  nodo_publisher
  nodo_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

# Opcional: copiar archivos de configuración o launch
# install(DIRECTORY config/ DESTINATION share/${PROJECT_NAME}/config)
# install(DIRECTORY launch/ DESTINATION share/${PROJECT_NAME}/launch)

# Finalizar definición del paquete (DEBE ser el último comando)
ament_package()

# ============================================================
# Referencia rápida de compilación
# ============================================================
# Compilar solo este paquete:
#   colcon build --packages-select drone_telemetry
#
# Compilar con salida detallada:
#   colcon build --packages-select drone_telemetry --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebInfo
#
# Ejecutar después de compilar:
#   source install/setup.bash
#   ros2 run drone_telemetry nodo_publisher
#   # (en otra terminal)
#   ros2 run drone_telemetry nodo_subscriber
