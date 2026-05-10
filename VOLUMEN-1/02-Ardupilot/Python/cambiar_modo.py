#!/usr/bin/env python3
"""
cambiar_modo.py - Cambiar modos de vuelo remotamente

Este script demuestra cómo:
1. Conectar a Ardupilot
2. Leer el modo actual
3. Cambiar a diferentes modos de vuelo
4. Verificar cambios en QGroundControl

Modos disponibles en Copter:
  - STABILIZE      (estabilización manual)
  - ALT_HOLD       (mantener altitud automáticamente)
  - LOITER         (círculos automáticos)
  - GUIDED         (waypoints vía dronekit)
  - AUTO           (misiones del FC)
  - RTL            (regreso a home)
  - LAND           (aterrizaje automático)

Requisitos:
    pip install dronekit

Uso:
    python3 cambiar_modo.py --connect 127.0.0.1:14550

Autor: DroneAcademy.edu
Licencia: MIT
"""

from dronekit import connect, VehicleMode
import argparse
import time
import sys

def cambiar_modo(vehicle, nombre_modo, duracion=3):
    """
    Cambia el modo del dron y lo mantiene por X segundos.

    Args:
        vehicle: Instancia del vehículo
        nombre_modo: Nombre del modo (ej: "ALT_HOLD", "LOITER")
        duracion: Tiempo en segundos que se mantiene el modo
    """
    print(f"\nCambiando a modo: {nombre_modo}")
    print(f"Modo anterior: {vehicle.mode.name}")

    vehicle.mode = VehicleMode(nombre_modo)

    # Esperar a que se confirme el cambio
    timeout = time.time() + 10
    while vehicle.mode.name != nombre_modo:
        if time.time() > timeout:
            print(f"✗ Error: No se pudo cambiar a {nombre_modo}")
            return False
        print(f"  Esperando confirmación... (actual: {vehicle.mode.name})")
        time.sleep(0.5)

    print(f"✓ Modo actual: {vehicle.mode.name}")

    # Mantener el modo
    print(f"  Manteniéndose en {nombre_modo} durante {duracion}s...")
    for i in range(duracion):
        alt = vehicle.location.global_relative_frame.alt
        print(f"    {i+1}s: {vehicle.mode.name} | Alt={alt:.1f}m")
        time.sleep(1)

    return True


def main():
    parser = argparse.ArgumentParser(description='Cambia modos de vuelo remotamente')
    parser.add_argument('--connect', default='127.0.0.1:14550',
                        help='Cadena de conexión')
    parser.add_argument('--tiempo', type=int, default=3,
                        help='Tiempo (segundos) en cada modo (default: 3)')

    args = parser.parse_args()

    print("="*60)
    print("CAMBIAR MODO DE VUELO")
    print("="*60)
    print(f"\nConectando a: {args.connect}")

    try:
        # Conectar
        vehicle = connect(args.connect, wait_ready=True)
        print("✓ Conectado")

        print(f"\nModo inicial: {vehicle.mode.name}")
        print("Observa QGroundControl para ver los cambios en tiempo real")
        print("-" * 60)

        # Secuencia de cambios de modo
        modos = [
            "STABILIZE",     # Manual puro
            "ALT_HOLD",      # Mantiene altitud automáticamente
            "LOITER",        # Circunda automáticamente
        ]

        for modo in modos:
            cambiar_modo(vehicle, modo, duracion=args.tiempo)
            time.sleep(1)

        # Regresar a modo original
        print(f"\nRegresando a modo: STABILIZE")
        cambiar_modo(vehicle, "STABILIZE", duracion=2)

        print("-" * 60)
        print("\n✓ Cambio de modos completado")
        print("✓ El dron debería haber mostrado cada transición en QGC")

        vehicle.close()
        print("✓ Desconectado")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
