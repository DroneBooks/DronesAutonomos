# Volumen 1 — Capítulo 3: MAVLink

> **Recursos para el capítulo "MAVLink: Protocolo de Comunicación con Drones"**  
> **Nivel:** Intermedio

---

## 📋 Descripción General

MAVLink (Micro Air Vehicle Link) es el protocolo de comunicación estándar para drones. Este directorio contiene scripts para:
- Lectura de telemetría en tiempo real
- Análisis de datos de vuelo
- Ejemplos de comunicación básica

Todos los scripts funcionan con Ardupilot, PX4 y otros firmware MAVLink-compatibles.

---

## 🛠️ Scripts Disponibles

### 1. **telemetry_reader.py** — Lector de Telemetría en Tiempo Real ⭐
Script que lee continuamente datos de vuelo y los muestra.

```bash
python telemetry_reader.py
```

**Datos que muestra:**
- **Posición GPS:** Latitud, Longitud, Altitud
- **Actitud:** Pitch, Roll, Yaw (ángulos)
- **Velocidad:** Velocidad en XYZ
- **Batería:** Voltaje, Corriente, % restante
- **Estado:** Armado/Desarmado, Modo de vuelo, Satélites GPS

---

### 2. **leer_telemetria_avanzada.py** — Análisis Profundo de Telemetría
Script más completo que registra datos y proporciona análisis.

```bash
python leer_telemetria_avanzada.py
```

**Funcionalidades:**
- Registra datos en CSV para análisis posterior
- Calcula velocidad y aceleración
- Detecta anomalías (voltaje bajo, GPS perdido, etc)
- Estadísticas de vuelo

---

### 3. **examples/connect_to_fc.py** — Ejemplo Básico
Script mínimo para conectarse y leer datos.

```bash
python examples/connect_to_fc.py
```

---

## 📦 Instalación

```bash
pip install -r requirements.txt
python telemetry_reader.py
```

---

## 🧪 Prueba en SITL

```bash
cd ~/ardupilot
./Tools/autotest/sim_vehicle.py -v ArduCopter -L default
# En otra terminal:
python telemetry_reader.py
```

---

## 🔌 Conexión a Hardware

```bash
python telemetry_reader.py --port /dev/ttyACM0 --baudrate 115200
```

---

## 📚 Recursos

- **Libro:** *Drones Autónomos I*, Volumen 1, Capítulo 3 — disponible en Amazon KDP
- **Especificación MAVLink:** https://mavlink.io/
- **pymavlink:** https://github.com/ArduPilot/pymavlink

---

**Última actualización:** 16 Abril 2026
