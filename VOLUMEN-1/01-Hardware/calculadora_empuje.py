#!/usr/bin/env python3
"""
Volumen 1 — Capítulo 1: Hardware
Calculadora de especificaciones para drones multirotor
Ayuda a dimensionar componentes antes de comprar/ensamblar
"""

def separador(titulo=""):
    if titulo:
        print(f"\n{'=' * 60}")
        print(f"  {titulo}")
        print('=' * 60)
    else:
        print('-' * 60)


# ─── 1. Relación Empuje / Peso ───────────────────────────────────

def calcular_relacion_empuje_peso():
    separador("CALCULADORA: Relación Empuje / Peso (T:W)")
    print("Determina si el drone tiene suficiente potencia para volar.")
    print("Valor recomendado: 2:1 — 3:1 para drones FPV / autónomos\n")

    try:
        num_motores   = int(input("Número de motores (ej. 4 para quadrotor): "))
        empuje_motor  = float(input("Empuje por motor a plena potencia (gramos): "))
        peso_total    = float(input("Peso total del drone con batería (gramos): "))
    except ValueError:
        print("[ERROR] Introduce valores numéricos válidos.")
        return

    empuje_total = num_motores * empuje_motor
    relacion     = empuje_total / peso_total

    separador()
    print(f"  Empuje total (100% throttle) : {empuje_total:.0f} g")
    print(f"  Peso total                   : {peso_total:.0f} g")
    print(f"  Relación empuje/peso (T:W)   : {relacion:.2f} : 1")
    separador()

    if relacion < 1.5:
        print("  ⛔  INSUFICIENTE — el drone no despegará correctamente.")
    elif relacion < 2.0:
        print("  ⚠️   AJUSTADO — para fotografía estacionaria.")
    elif relacion <= 3.5:
        print("  ✅  IDEAL — buena maniobrabilidad y autonomía.")
    else:
        print("  🚀  EXCESO DE POTENCIA — apto para racing / acrobático.")


# ─── 2. Tiempo de Vuelo Estimado ─────────────────────────────────

def calcular_tiempo_vuelo():
    separador("CALCULADORA: Tiempo de Vuelo Estimado")
    print("Estima la autonomía según batería y consumo.\n")

    try:
        capacidad_mah = float(input("Capacidad de batería (mAh, ej. 5000): "))
        corriente_a   = float(input("Corriente media de vuelo (A, ej. 20): "))
        eficiencia    = float(input("Eficiencia estimada (%, defecto 80): ") or "80")
    except ValueError:
        print("[ERROR] Introduce valores numéricos válidos.")
        return

    # Capacidad útil aplicando eficiencia (no descargar batería al 100%)
    capacidad_util_ah = (capacidad_mah / 1000.0) * (eficiencia / 100.0)
    tiempo_min        = (capacidad_util_ah / corriente_a) * 60.0

    separador()
    print(f"  Capacidad batería            : {capacidad_mah:.0f} mAh")
    print(f"  Corriente media              : {corriente_a:.1f} A")
    print(f"  Eficiencia aplicada          : {eficiencia:.0f}%")
    print(f"  Tiempo de vuelo estimado     : {tiempo_min:.1f} min")
    separador()

    if tiempo_min < 5:
        print("  ⛔  Muy corto — revisa consumo o aumenta batería.")
    elif tiempo_min < 10:
        print("  ⚠️   Autonomía baja — suficiente para prácticas cortas.")
    elif tiempo_min <= 25:
        print("  ✅  Autonomía buena — adecuado para misiones estándar.")
    else:
        print("  ✅  Excelente autonomía — plataforma eficiente.")

    print(f"\n  Consejo: Para {tiempo_min * 2:.0f} min de vuelo, necesitarías")
    print(f"  {capacidad_mah * 2:.0f} mAh o reducir peso/consumo a la mitad.")


# ─── 3. Selección de Motor (KV) ──────────────────────────────────

def recomendar_motor_kv():
    separador("CALCULADORA: Selección de Motor por KV y Hélice")
    print("Relaciona KV del motor, tensión de batería y tamaño de hélice.")
    print("Regla: KV × Voltaje ≈ RPM sin carga\n")

    TABLA_KV = [
        # (tipo, peso_drone_g, prop_pulg, celulas_lipo, kv_min, kv_max)
        ("Micro / Racing 3\"",    250,   3,  4, 2400, 3000),
        ("Mini / FPV 5\"",        600,   5,  4, 1700, 2400),
        ("Freestyle 5-6\"",       800,   6,  4, 1500, 2000),
        ("Fotografía 7-8\"",     1500,   8,  4,  800, 1200),
        ("Fotografía 10\"",      2500,  10,  6,  400,  700),
        ("Carga pesada 12-15\"", 5000,  13,  6,  200,  400),
    ]

    print("  Categorías disponibles:")
    for i, (tipo, _, _, _, _, _) in enumerate(TABLA_KV, 1):
        print(f"  [{i}] {tipo}")

    try:
        sel = int(input("\n  Selecciona categoría: ")) - 1
        if not 0 <= sel < len(TABLA_KV):
            raise ValueError
    except ValueError:
        print("[ERROR] Selección inválida.")
        return

    tipo, peso, prop, celdas, kv_min, kv_max = TABLA_KV[sel]
    voltaje = celdas * 3.7  # Voltaje nominal LiPo

    separador()
    print(f"  Categoría                    : {tipo}")
    print(f"  Peso drone estimado          : {peso} g")
    print(f"  Hélice recomendada           : {prop}\"")
    print(f"  Batería recomendada          : {celdas}S LiPo ({voltaje:.1f}V nominal)")
    print(f"  Rango de KV recomendado      : {kv_min} — {kv_max} KV")
    print(f"  RPM estimadas (a plena carga): {int(kv_max * voltaje * 0.85)} rpm")
    separador()
    print("  Nota: Valores orientativos. Consulta las fichas técnicas")
    print("  del fabricante para datos exactos de empuje por hélice.")


# ─── 4. Velocidad de Punta de Hélice (Seguridad) ─────────────────

def calcular_velocidad_punta_helice():
    separador("CALCULADORA: Velocidad de Punta de Hélice")
    print("Comprueba si la hélice está dentro de límites seguros.")
    print("Límite recomendado: < 120 m/s (Mach 0.35)\n")

    try:
        kv       = float(input("KV del motor: "))
        voltaje  = float(input("Voltaje de batería (V, ej. 14.8 para 4S): "))
        diametro = float(input("Diámetro de hélice (pulgadas, ej. 5): "))
    except ValueError:
        print("[ERROR] Introduce valores numéricos válidos.")
        return

    rpm_sin_carga  = kv * voltaje
    rpm_carga      = rpm_sin_carga * 0.85          # ~85% bajo carga
    radio_m        = (diametro * 0.0254) / 2.0     # pulg → metros
    vel_punta_ms   = (2 * 3.14159 * radio_m * rpm_carga) / 60.0

    separador()
    print(f"  RPM sin carga (KV × V)       : {rpm_sin_carga:.0f}")
    print(f"  RPM estimadas bajo carga     : {rpm_carga:.0f}")
    print(f"  Radio de hélice              : {radio_m * 100:.1f} cm")
    print(f"  Velocidad punta de hélice    : {vel_punta_ms:.1f} m/s")
    separador()

    if vel_punta_ms < 100:
        print("  ✅  Seguro — dentro de límites operativos normales.")
    elif vel_punta_ms < 120:
        print("  ⚠️   En el límite — usa hélice de fibra de carbono.")
    else:
        print("  ⛔  PELIGROSO — riesgo de rotura de hélice.")
        print("  → Reduce KV, voltaje o tamaño de hélice.")


# ─── Menú Principal ──────────────────────────────────────────────

def main():
    separador("DroneAcademy — Calculadora de Hardware")
    print("  Volumen 1, Capítulo 1: Hardware")
    print("  Herramienta de apoyo para dimensionar tu drone\n")

    opciones = {
        '1': ("Relación empuje / peso (T:W)",   calcular_relacion_empuje_peso),
        '2': ("Tiempo de vuelo estimado",        calcular_tiempo_vuelo),
        '3': ("Selección de motor (KV)",         recomendar_motor_kv),
        '4': ("Velocidad de punta de hélice",    calcular_velocidad_punta_helice),
        '5': ("Salir", None),
    }

    while True:
        separador("MENÚ PRINCIPAL")
        for clave, (desc, _) in opciones.items():
            print(f"  [{clave}] {desc}")

        eleccion = input("\n  Selecciona opción: ").strip()

        if eleccion not in opciones:
            print("\n[ERROR] Opción no válida.")
            continue

        desc, funcion = opciones[eleccion]
        if funcion is None:
            print("\n[OK] ¡Hasta pronto!\n")
            break

        funcion()
        input("\n  Presiona Enter para continuar...")


if __name__ == "__main__":
    main()
