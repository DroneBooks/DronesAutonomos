#!/usr/bin/env python3
"""
conexion_basica.py - Conectar a Ardupilot y leer telemetría básica

Este script demuestra cómo:
1. Conectar a un Flight Controller Ardupilot
2. Leer datos de telemetría en tiempo real
3. Mostrar información del dron

Requisitos:
    pip install dronekit

Uso:
    python3 conexion_basica.py --connect /dev/ttyUSB0   (Linux)
    python3 conexion_basica.py --connect COM3             (Windows)
    python3 conexion_basica.py --connect 127.0.0.1:14550 (SITL)

Autor: DroneAcademy.edu
Licencia: MIT
"""

from dronekit import connect, VehicleMode
import argparse
import time
import sys

def main():
    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Conecta a Ardupilot y muestra telemetría')
    parser.add_argument('--connect', default='127.0.0.1:14550',
                        help='Cadena de conexión (puerto serie o IP:puerto)')
    parser.add_argument('--baudrate', type=int, default=57600,
                        help='Velocidad de bauds (default: 57600)')

    args = parser.parse_args()

    print("="*60)
    print("CONEXIÓN BÁSICA A ARDUPILOT")
    print("="*60)
    print(f"\nConectando a: {args.connect}")
    print("Esperando telemetría...\n")

    try:
        # Conectar al vehículo
        vehicle = connect(args.connect, baud=args.baudrate, wait_ready=True)

        print("✓ Conectado exitosamente!\n")

        # Información básica
        print("INFORMACIÓN DEL VEHÍCULO:")
        print("-" * 60)
        print(f"Tipo de vehículo: {vehicle.system_status.state}")
        print(f"Modo actual: {vehicle.mode.name}")
        print(f"Armado: {'Sí' if vehicle.armed else 'No'}")
        print(f"¿Listo para armar? {vehicle.is_armable}\n")

        # Lectura continua de telemetría (10 segundos)
        print("TELEMETRÍA EN TIEMPO REAL (10 segundos):")
        print("-" * 60)
        print(f"{'Tiempo':<8} {'Altitud':<12} {'Velocidad':<12} {'Batería':<10} {'Satélites':<10}")
        print("-" * 60)

        start_time = time.time()
        while time.time() - start_time < 10:
            elapsed = int(time.time() - start_time)
            altitude = vehicle.location.global_relative_frame.alt or 0
            speed = vehicle.airspeed or 0
            battery = vehicle.battery.voltage or 0
            satellites = vehicle.gps_0.satellites_visible or 0

            print(f"{elapsed:<8} {altitude:<12.2f}m {speed:<12.2f}m/s {battery:<10.2f}V {satellites:<10}")

            time.sleep(1)

        print("-" * 60)
        print("\n✓ Lectura completada")

        # Desconectar
        vehicle.close()
        print("✓ Desconectado")

    except Exception as e:
        print(f"\n✗ Error de conexión: {e}")
        print("\nVerifica:")
        print("  - FC conectado por USB/telemetría")
        print("  - Puerto serie correcto (COM3, /dev/ttyUSB0, etc.)")
        print("  - Velocidad de bauds correcta (default: 57600)")
        print("  - SITL ejecutándose en 127.0.0.1:14550")
        sys.exit(1)

if __name__ == '__main__':
    main()
