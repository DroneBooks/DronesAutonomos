# Volumen 1 — Capítulo 2: Ardupilot

> **Recursos para el capítulo "Ardupilot: Firmware de Drones Autónomos"**  
> **Nivel:** Principiante a Intermedio

---

## 📋 Descripción General

Este directorio contiene scripts Python para trabajar con Ardupilot. Incluyen:
- Calibración interactiva de sensores
- Configuración de parámetros del controlador de vuelo (FC)
- Ejemplos básicos de conexión y control

Todos los scripts están diseñados para trabajar con **SITL** (simulador) o hardware real.

---

## 🛠️ Scripts Disponibles

### 1. **calibrate_sensors.py** — Calibración de Sensores ⭐
Asistente interactivo que te guía paso a paso en la calibración:
- **Brújula (Compass):** Calibración de magnetómetro
- **IMU:** Calibración de acelerómetro/giróscopo
- **Radio Control:** Mapping de canales
- **ESC:** Calibración de velocidad de motor
- **Verificación:** Test de sensores

```bash
python calibrate_sensors.py
```

**Uso:** Sigue los prompts interactivos. Ideal para alumnos que necesitan calibrar su drone.

---

### 2. **parameter_configurator.py** — Configurador de Parámetros
Herramienta interactiva para leer y escribir parámetros del FC.

```bash
python parameter_configurator.py
```

**Menú interactivo:**
- Listar parámetros actuales
- Cambiar un parámetro
- Buscar parámetros por nombre
- Guardar configuración

**Ejemplo:** Cambiar sensibilidad de PID, timeouts, etc.

---

### 3. **conexion_basica.py** — Conexión Básica
Ejemplo mínimo para conectarse a un FC y leer estado.

```bash
python conexion_basica.py
```

**Output esperado:**
```
Conectando a 127.0.0.1:14550...
✓ Conectado
Actitud: pitch=0.5°, roll=-0.3°, yaw=45°
Batería: 12.5V
GPS: (0 satélites)
```

---

### 4. **cambiar_modo.py** — Control de Modos de Vuelo
Cambia entre modos de vuelo (Stabilize, Alt Hold, Loiter, etc).

```bash
python cambiar_modo.py
```

**Modos disponibles:**
- STABILIZE (manual con estabilización)
- ALT_HOLD (mantiene altitud)
- LOITER (orbita en punto)
- GUIDED (vuelo autónomo)
- LAND (aterrizaje automático)

---

### 5. **despegar_aterrizar.py** — Despegue/Aterrizaje Automático
Script para despegue y aterrizaje automático.

```bash
python despegar_aterrizar.py
```

**Funcionalidad:**
1. Arma el dron (ARM)
2. Despega a altura especificada
3. Espera entrada del usuario
4. Aterriza automáticamente

⚠️ **Precaución:** Solo usar en simulador primero.

---

### 6. **waypoint_simple.py** — Misión de Waypoints
Crea y ejecuta una misión con waypoints.

```bash
python waypoint_simple.py
```

**Funcionalidad:**
- Define waypoints (lat, lon, altitud)
- Carga misión en FC
- Monitorea progreso de vuelo
- Registra posición actual

---

### 7. **geofence_definir.py** — Límites de Vuelo
Establece un perímetro de seguridad (geofence).

```bash
python geofence_definir.py
```

**Opciones:**
- Geofence cilíndrico (radio/altura)
- Geofence rectangular
- Altitud máxima
- Acción en violación (RTH, Land, etc)

---

## 📦 Instalación de Dependencias

**Paso 1:** Clonar o descargar este directorio

**Paso 2:** Instalar dependencias
```bash
pip install -r requirements.txt
```

**Paso 3:** Verificar instalación
```bash
python -c "import pymavlink; print(pymavlink.__version__)"
```

**Dependencias principales:**
- `pymavlink` — Comunicación MAVLink
- `pexpect` — Interacción con procesos (SITL)
- `pyserial` — Comunicación serial (hardware)

---

## 🧪 Prueba en SITL (Simulador)

Para probar sin hardware, usa SITL (Software-in-the-Loop):

**Paso 1:** Descargar Ardupilot
```bash
git clone https://github.com/ArduPilot/ardupilot
cd ardupilot
./Tools/autotest/sim_vehicle.py -v ArduCopter -L default
```

**Paso 2:** En otra terminal, ejecutar script
```bash
python calibrate_sensors.py  # Se conecta a 127.0.0.1:14550
```

---

## 🔌 Conexión a Hardware Real

**Opción 1: USB Directo**
```bash
python calibrate_sensors.py
# Se conectará a /dev/ttyACM0 (Linux) o COM3 (Windows)
```

**Opción 2: Telemetría Serial (FC → Raspi/Laptop)**
```bash
python calibrate_sensors.py --port /dev/ttyUSB0 --baudrate 57600
```

**Opción 3: Ethernet/WiFi (Advanced)**
Requiere configuración especial del FC.

---

## 📊 Requisitos del Sistema

| Componente | Mínimo | Recomendado |
|-----------|--------|------------|
| Python | 3.8 | 3.10+ |
| SO | Linux/Mac/Windows | Ubuntu 20.04 LTS |
| RAM | 1 GB | 4 GB |
| Almacenamiento | 500 MB | 2 GB |

---

## ⚠️ Notas de Seguridad

1. **Primero en simulador:** Prueba todos los scripts en SITL antes de usar con hardware
2. **Validación de entrada:** Los scripts validan puertos y baudrates
3. **Permisos de puerto:** En Linux, agrega tu usuario a grupo `dialout`:
   ```bash
   sudo usermod -a -G dialout $USER
   ```

---

## 🐛 Troubleshooting

**"Connection refused"**
- Verifica que SITL está ejecutándose (`sim_vehicle.py`)
- Verifica puertos: `netstat -an | grep 14550`

**"Permission denied: /dev/ttyACM0"**
- En Linux: `sudo usermod -a -G dialout $USER` (requiere logout/login)
- En Windows: Ejecuta terminal como administrador

**"pymavlink import error"**
- Reinstala: `pip install pymavlink --upgrade --force`

---

## 🎓 Ejercicios Sugeridos

1. **Ejercicio 1:** Calibra sensores en SITL y verifica output
2. **Ejercicio 2:** Cambia el parámetro `ANGLE_MAX` usando parameter_configurator.py
3. **Ejercicio 3:** Ejecuta despegar_aterrizar.py en simulador
4. **Ejercicio 4:** Define un geofence y prueba violación

---

## 📚 Recursos Relacionados

- **Libro:** *Drones Autónomos I*, Volumen 1, Capítulo 2 — disponible en Amazon KDP
- **Documentación Ardupilot:** https://ardupilot.org/copter/docs/
- **Foro:** https://discuss.ardupilot.org/

---

## 📝 Estructura de Carpetas

```
02-Ardupilot/Python/
├── README.md (Este archivo)
├── requirements.txt
├── calibrate_sensors.py
├── parameter_configurator.py
├── conexion_basica.py
├── cambiar_modo.py
├── despegar_aterrizar.py
├── waypoint_simple.py
├── geofence_definir.py
├── ejemplos/         (Ejemplos adicionales)
├── ejercicios/       (Plantillas de ejercicios)
└── soluciones/       (Soluciones de ejercicios)
```

---

**Última actualización:** 16 Abril 2026  
**Autor:** DroneAcademy Team
