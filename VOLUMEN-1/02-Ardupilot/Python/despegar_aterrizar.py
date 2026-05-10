#!/usr/bin/env python3
"""
despegar_aterrizar.py - Control básico de vuelo (despegue y aterrizaje)

Este script demuestra cómo:
1. Conectar a Ardupilot
2. Armar el dron
3. Despegar a una altitud específica
4. Mantener altura durante 10 segundos
5. Aterrizar automáticamente

ADVERTENCIA: Este script DESPEGARÁ tu dron físico.
Úsalo solo en:
  - Simulación SITL (sin hardware real)
  - Área abierta y segura con supervisión

Requisitos:
    pip install dronekit

Uso:
    python3 despegar_aterrizar.py --connect 127.0.0.1:14550 --alt 10

Parámetros:
    --connect: Dirección de conexión (default: 127.0.0.1:14550)
    --alt: Altitud de despegue en metros (default: 10)

Autor: DroneAcademy.edu
Licencia: MIT
"""

from dronekit import connect, VehicleMode, LocationGlobalRelative
import argparse
import time
import sys

def arm_and_takeoff(vehicle, altitude):
    """
    Arma el dron y despega hasta la altitud especificada.

    Args:
        vehicle: Instancia del vehículo
        altitude: Altitud objetivo en metros
    """
    print(f"\nPreparando para despegue a {altitude}m...")

    # Verificar que esté desarmado
    while vehicle.is_armable is False:
        print("Esperando que el dron sea armable...")
        time.sleep(1)

    print("✓ Dron listo para armar")

    # Armar
    print("Armando dron...")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while vehicle.armed is False:
        print("  Esperando armado...")
        time.sleep(1)

    print("✓ Dron armado")

    # Despegar
    print(f"Despegando a {altitude}m...")
    vehicle.simple_takeoff(altitude)

    # Monitorear altitud
    while True:
        current_alt = vehicle.location.global_relative_frame.alt
        print(f"  Altitud actual: {current_alt:.1f}m / {altitude}m")

        # Parar cuando alcance 95% de la altitud
        if current_alt >= altitude * 0.95:
            print(f"✓ Altitud objetivo alcanzada: {current_alt:.1f}m")
            break

        time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description='Despega y aterriza el dron')
    parser.add_argument('--connect', default='127.0.0.1:14550',
                        help='Cadena de conexión')
    parser.add_argument('--alt', type=float, default=10,
                        help='Altitud de despegue en metros (default: 10)')
    parser.add_argument('--time', type=int, default=10,
                        help='Tiempo en vuelo en segundos (default: 10)')

    args = parser.parse_args()

    print("="*60)
    print("DESPEGAR Y ATERRIZAR")
    print("="*60)
    print(f"\nConectando a: {args.connect}")

    try:
        # Conectar
        vehicle = connect(args.connect, wait_ready=True)
        print("✓ Conectado")

        # Cambiar a modo GUIDED
        print("\nCambiando a modo GUIDED...")
        vehicle.mode = VehicleMode("GUIDED")

        # Despegar
        arm_and_takeoff(vehicle, args.alt)

        # Mantener vuelo
        print(f"\nManteniendo vuelo durante {args.time} segundos...")
        print("Observa Mission Planner/QGC para ver posición en tiempo real")

        for i in range(args.time):
            alt = vehicle.location.global_relative_frame.alt
            print(f"  {i+1}s: Altitud={alt:.1f}m")
            time.sleep(1)

        # Aterrizar
        print("\nAtterrizar...")
        vehicle.mode = VehicleMode("LAND")

        # Esperar a que aterrice
        while vehicle.location.global_relative_frame.alt > 0.1:
            alt = vehicle.location.global_relative_frame.alt
            print(f"  Altitud: {alt:.1f}m")
            time.sleep(1)

        print("✓ Aterrizaje completado")

        # Desarmar
        vehicle.armed = False
        print("✓ Dron desarmado")

        vehicle.close()
        print("✓ Desconectado")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
