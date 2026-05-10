# Volumen 1 — Capítulo 1: Hardware

> **Recursos para el capítulo "Hardware de Drones: Componentes y Selección"**  
> **Nivel:** Principiante

---

## 📦 Contenido

```
VOLUMEN-1/01-Hardware/
├── README.md
└── calculadora_empuje.py    # ✅ Calculadora de especificaciones
```

---

## 🛠️ Herramientas Disponibles

### **calculadora_empuje.py** — Calculadora de Especificaciones

Herramienta interactiva con 4 calculadoras para dimensionar tu drone antes de comprarlo o ensamblarlo:

| Calculadora | Qué calcula |
|-------------|-------------|
| **1. T:W (empuje/peso)** | Si el drone tendrá potencia suficiente para volar |
| **2. Tiempo de vuelo** | Autonomía estimada según batería y consumo |
| **3. Motor KV** | Rango de KV recomendado según categoría de drone |
| **4. Velocidad de hélice** | Comprueba límites de seguridad de la hélice |

```bash
python calculadora_empuje.py
```

**Ejemplo de uso (T:W):**
```
Número de motores: 4
Empuje por motor a plena potencia (g): 850
Peso total del drone con batería (g): 1500

  Empuje total (100% throttle) :  3400 g
  Peso total                   :  1500 g
  Relación empuje/peso (T:W)   :  2.27 : 1
  ✅  IDEAL — buena maniobrabilidad y autonomía.
```

---

## 📐 Fórmulas Usadas

| Concepto | Fórmula |
|----------|---------|
| Relación T:W | `(motores × empuje_motor) / peso_total` |
| Tiempo de vuelo | `(batería_Ah × eficiencia%) / corriente_A × 60` |
| RPM estimadas | `KV × voltaje × 0.85` (factor de carga) |
| Vel. punta hélice | `2π × radio_m × RPM / 60` |

---

## 📖 Referencia al Libro

Estas calculadoras acompañan el **Volumen 1, Capítulo 1: Hardware** del libro  
*Drones Autónomos I: Hardware, Ardupilot y MAVLink*.

Temas relacionados en el capítulo:
- Selección de motores y hélices
- Dimensionado de batería LiPo
- Relación empuje/peso para diferentes aplicaciones
- Seguridad mecánica en componentes rotativos

---

## ⚠️ Requisitos

- Python 3.10+
- Sin dependencias externas (solo librería estándar)

---

**Última actualización:** Abril 2026 | DroneBooks
