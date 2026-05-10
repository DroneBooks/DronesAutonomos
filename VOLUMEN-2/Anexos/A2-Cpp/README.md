# Volumen 2 — Anexo A2: C++ para ROS2

> **Recursos para el anexo "C++: Desarrollo de Nodos ROS2 de Alta Performance"**  
> **Nivel:** Intermedio a Avanzado

---

## 📦 Contenido

```
VOLUMEN-2/Anexos/A2-Cpp/
├── README.md                 # Esta guía
├── CMakeLists.txt           # Plantilla de compilación
├── nodo_publisher.cpp       # Publicador de telemetría
├── nodo_subscriber.cpp      # Suscriptor con lógica de control
├── bridge_mavlink.cpp       # Puente MAVLink ↔ ROS2
└── src/                     # (crear cuando clones el repo)
    ├── nodo_publisher.cpp
    ├── nodo_subscriber.cpp
    └── bridge_mavlink.cpp
```

---

## ✅ Ejemplos Disponibles

| Archivo | Descripción | Estado |
|---------|-------------|--------|
| `nodo_publisher.cpp` | Nodo ROS2 publicador básico en C++ | ✅ Listo |
| `nodo_subscriber.cpp` | Nodo ROS2 suscriptor básico en C++ | ✅ Listo |
| `CMakeLists.txt` | Plantilla de compilación para nodos C++ | ✅ Listo |
| `bridge_mavlink.cpp` | Puente MAVLink ↔ ROS2 topics en C++ | ✅ Listo |

---

## 🚀 Instalación de ROS2 (Prerequisito)

Antes de compilar cualquier nodo C++, instala ROS2 Humble con el script incluido:

```bash
# Desde la raíz del repositorio
bash VOLUMEN-2/01-ROS2/install_ros2.sh
```

El script instala automáticamente:
- ROS2 Humble Desktop
- Herramientas de compilación (colcon, cmake)
- Dependencias Python de ROS2

---

## 🔧 Estructura de un Nodo C++ para ROS2

```cpp
// Ejemplo mínimo — publicador de telemetría
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

class NodoTelemetria : public rclcpp::Node {
public:
    NodoTelemetria() : Node("telemetria") {
        publisher_ = create_publisher<std_msgs::msg::Float64>(
            "altitud", 10);
        timer_ = create_wall_timer(
            std::chrono::milliseconds(500),
            std::bind(&NodoTelemetria::publicar, this));
    }

private:
    void publicar() {
        auto msg = std_msgs::msg::Float64();
        msg.data = 25.3;  // En producción: leer de MAVLink
        publisher_->publish(msg);
        RCLCPP_INFO(get_logger(), "Altitud: %.1f m", msg.data);
    }
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<NodoTelemetria>());
    rclcpp::shutdown();
    return 0;
}
```

### CMakeLists.txt mínimo
```cmake
cmake_minimum_required(VERSION 3.8)
project(telemetria_nodo)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(nodo_telemetria src/nodo_telemetria.cpp)
ament_target_dependencies(nodo_telemetria rclcpp std_msgs)

install(TARGETS nodo_telemetria DESTINATION lib/${PROJECT_NAME})
ament_package()
```

### Compilar y ejecutar

**Paso 1: Preparar workspace**
```bash
# Crear workspace ROS2 si no existe
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Clonar o copiar el paquete drone_telemetry
git clone <repo>
cd ..
```

**Paso 2: Copiar archivos al lugar correcto**
```bash
# La estructura esperada es:
# ~/ros2_ws/src/drone_telemetry/
# ├── CMakeLists.txt
# ├── package.xml
# ├── src/
# │   ├── nodo_publisher.cpp
# │   ├── nodo_subscriber.cpp
# │   └── bridge_mavlink.cpp
```

**Paso 3: Crear package.xml** (si no existe)
```bash
cd ~/ros2_ws/src/drone_telemetry
cat > package.xml << 'EOF'
<?xml version="1.0"?>
<package format="3">
  <name>drone_telemetry</name>
  <version>0.0.1</version>
  <description>Nodos ROS2 C++ para telemetría de drones</description>
  <maintainer email="student@droneacademy.local">Student</maintainer>
  <license>BSD-3-Clause</license>
  <buildtool_depend>ament_cmake</buildtool_depend>
  <depend>rclcpp</depend>
  <depend>std_msgs</depend>
  <depend>geometry_msgs</depend>
</package>
EOF
```

**Paso 4: Compilar**
```bash
cd ~/ros2_ws
colcon build --packages-select drone_telemetry

# Compilar con salida detallada si hay errores:
colcon build --packages-select drone_telemetry --cmake-args -DCMAKE_BUILD_TYPE=Debug
```

**Paso 5: Ejecutar nodos**
```bash
# Terminal 1: Publicador
source ~/ros2_ws/install/setup.bash
ros2 run drone_telemetry nodo_publisher

# Terminal 2: Suscriptor
source ~/ros2_ws/install/setup.bash
ros2 run drone_telemetry nodo_subscriber

# Terminal 3: Bridge MAVLink (opcional, requiere Pixhawk o SITL)
source ~/ros2_ws/install/setup.bash
ros2 run drone_telemetry bridge_mavlink --connect 127.0.0.1:14550
```

**Paso 6: Monitorear tópicos**
```bash
# Terminal 4: Ver tópicos publicados
source ~/ros2_ws/install/setup.bash
ros2 topic list

# Ver contenido en tiempo real
ros2 topic echo /telemetria/altitud
ros2 topic echo /telemetria/bateria
ros2 topic echo /telemetria/velocidad
```

---

## 📊 Python vs C++ en ROS2

| Característica | Python | C++ |
|----------------|--------|-----|
| Velocidad de desarrollo | ✅ Rápida | Lenta |
| Performance en tiempo real | Limitada | ✅ Óptima |
| Gestión de memoria | Automática | Manual |
| Uso en controladores críticos | No recomendado | ✅ Ideal |
| Curva de aprendizaje | Baja | Alta |

> **Regla de oro:** Python para prototipo, C++ para producción.

---

## 📖 Referencia al Libro

Este anexo acompaña el **Volumen 2, Anexo A2: C++** del libro  
*Drones Autónomos II: Robótica, Visión Artificial e IA Embarcada*.

Temas del anexo en el libro:
- Sintaxis C++ esencial para robótica (punteros, referencias, clases)
- Nodos publisher/subscriber en C++
- Servicios y acciones ROS2 en C++
- Integración MAVLink con ROS2 en C++
- CMake y colcon para compilación

---

## ⚙️ Requisitos

- **OS:** Ubuntu 22.04 LTS
- **ROS2:** Humble (instalado via `install_ros2.sh`)
- **Compilador:** g++ 11+, cmake 3.22+

---

**Última actualización:** Abril 2026 | DroneBooks
