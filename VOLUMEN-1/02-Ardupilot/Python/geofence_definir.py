#!/usr/bin/env python3
"""
geofence_definir.py - Definir límites virtuales (geofence) para el dron

Este script demuestra cómo:
1. Definir una zona rectangular (geofence)
2. Configurar parámetros de geofence en el FC
3. Verificar que el dron respeta límites en QGroundControl

El geofence es un perímetro virtual. Si el dron intenta salir:
  - Modo LOITER: Regresa a límite automáticamente
  - Modo GUIDED: Detiene movimiento
  - Todos modos: Activa failsafe si se configura

Requisitos:
    pip install dronekit pymavlink

Uso:
    python3 geofence_definir.py --connect 127.0.0.1:14550

Parámetros clave:
    FENCE_ENABLE=1            (activar geofence)
    FENCE_TYPE=1              (1=circunferencia, 2=polígono)
    FENCE_RADIUS=100          (radio en metros para tipo círculo)
    FENCE_ACTION=1            (0=report, 1=loiter, 2=guided, 3=rtl)

Autor: DroneAcademy.edu
Licencia: MIT
"""

from dronekit import connect
from pymavlink.dialects.v10 import mavutil
import argparse
import time
import sys

def leer_parametro(vehicle, nombre):
    """Lee un parámetro del FC."""
    vehicle.parameters[nombre]
    return vehicle.parameters.get(nombre)


def establecer_parametro(vehicle, nombre, valor):
    """Establece un parámetro en el FC."""
    print(f"  Configurando {nombre} = {valor}")
    vehicle.parameters[nombre] = valor

    # Esperar confirmación
    timeout = time.time() + 5
    while vehicle.parameters[nombre] != valor:
        if time.time() > timeout:
            print(f"    ✗ Timeout configurando {nombre}")
            return False
        time.sleep(0.1)

    print(f"    ✓ {nombre} confirmado")
    return True


def main():
    parser = argparse.ArgumentParser(description='Definir geofence (límites virtuales)')
    parser.add_argument('--connect', default='127.0.0.1:14550',
                        help='Cadena de conexión')
    parser.add_argument('--radio', type=float, default=100,
                        help='Radio de geofence en metros (default: 100)')
    parser.add_argument('--tipo', type=int, default=1,
                        help='Tipo: 1=círculo (default), 2=polígono')
    parser.add_argument('--accion', type=int, default=1,
                        help='Acción: 0=report, 1=loiter, 2=guided, 3=RTL')

    args = parser.parse_args()

    print("="*60)
    print("GEOFENCE (LÍMITES VIRTUALES)")
    print("="*60)
    print(f"\nConectando a: {args.connect}")

    try:
        # Conectar
        vehicle = connect(args.connect, wait_ready=True)
        print("✓ Conectado")

        # Esperar HOME
        print("\nEsperando ubicación HOME (GPS)...")
        while vehicle.home_location is None:
            print("  Aguardando GPS fix...")
            time.sleep(1)

        home_lat = vehicle.home_location.lat
        home_lon = vehicle.home_location.lon
        print(f"✓ HOME: ({home_lat:.6f}, {home_lon:.6f})")

        # Leer parámetros actuales
        print("\nParámetros actuales de geofence:")
        print("-" * 60)
        fence_enabled = leer_parametro(vehicle, 'FENCE_ENABLE')
        fence_type = leer_parametro(vehicle, 'FENCE_TYPE')
        fence_radius = leer_parametro(vehicle, 'FENCE_RADIUS')
        fence_action = leer_parametro(vehicle, 'FENCE_ACTION')

        print(f"FENCE_ENABLE:  {fence_enabled} (0=desactivado, 1=activo)")
        print(f"FENCE_TYPE:    {fence_type} (1=círculo, 2=polígono)")
        print(f"FENCE_RADIUS:  {fence_radius}m (para tipo círculo)")
        print(f"FENCE_ACTION:  {fence_action} (0=report, 1=loiter, 2=guided, 3=RTL)")

        # Configurar geofence
        print("\nConfigurando nuevo geofence...")
        print("-" * 60)

        # Deshabilitar primero
        establecer_parametro(vehicle, 'FENCE_ENABLE', 0)
        time.sleep(1)

        # Configurar parámetros
        establecer_parametro(vehicle, 'FENCE_TYPE', args.tipo)
        establecer_parametro(vehicle, 'FENCE_RADIUS', args.radio)
        establecer_parametro(vehicle, 'FENCE_ACTION', args.accion)

        # Habilitar
        establecer_parametro(vehicle, 'FENCE_ENABLE', 1)

        print("\n✓ Geofence configurado exitosamente")
        print(f"  - Radio: {args.radio}m desde HOME")
        print(f"  - Acción: ", end='')
        if args.accion == 0:
            print("Reportar (report only)")
        elif args.accion == 1:
            print("Loiter (circundar en límite)")
        elif args.accion == 2:
            print("Guided (detener movimiento)")
        else:
            print("RTL (regreso a home)")

        print("\n" + "="*60)
        print("VERIFICACION EN QGC")
        print("="*60)
        print("""
En QGroundControl, deberías ver:
1. Un círculo rojo en el mapa (centro = HOME, radio = {} metros)
2. El dron NO puede salir de este círculo
3. Si intenta: {} acción

Para probar:
1. Arma el dron
2. Ve a ALT_HOLD o LOITER
3. Intenta pilotarlo fuera del círculo con RC
4. Verá cómo el dron se detiene/loitera en el límite
5. En logs verás mensajes "FENCE_BREACH"
""".format(args.radio, ["report", "loiter", "detener", "RTL"][args.accion]))

        # Monitorear por 30 segundos
        print("Monitoreando estado del geofence (30 segundos)...")
        print("-" * 60)

        start_time = time.time()
        while time.time() - start_time < 30:
            elapsed = int(time.time() - start_time)
            fence_enabled = leer_parametro(vehicle, 'FENCE_ENABLE')
            fence_radius = leer_parametro(vehicle, 'FENCE_RADIUS')

            # Verificar si el dron está dentro de límites (calculado aproximadamente)
            if vehicle.location.global_frame.lat is not None:
                # Cálculo muy simplificado de distancia
                lat_diff = abs(vehicle.location.global_frame.lat - home_lat)
                lon_diff = abs(vehicle.location.global_frame.lon - home_lon)
                distancia_aprox = (lat_diff + lon_diff) * 111000  # metros muy aprox

                estado = "DENTRO" if distancia_aprox < args.radio else "AFUERA"
                print(f"{elapsed}s: Geofence={'ACTIVO' if fence_enabled else 'INACTIVO'} | "
                      f"Radio={fence_radius}m | Estado={estado}")
            else:
                print(f"{elapsed}s: Geofence={'ACTIVO' if fence_enabled else 'INACTIVO'} | "
                      f"Aguardando GPS...")

            time.sleep(2)

        print("-" * 60)
        print("✓ Monitoreo completado")

        vehicle.close()
        print("✓ Desconectado")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
