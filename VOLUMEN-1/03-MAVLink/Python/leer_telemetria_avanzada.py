#!/usr/bin/env python3
"""
leer_telemetria_avanzada.py - Lectura de telemetría avanzada con exportación a CSV

Este script demuestra cómo:
1. Leer múltiples datos de telemetría
2. Exportar datos a archivo CSV para análisis posterior
3. Calcular derivadas (velocidad vertical, aceleración)
4. Generar reporte en tiempo real

Datos registrados:
    - Posición: Latitud, Longitud, Altitud (GPS)
    - Velocidad: Velocidad aérea, velocidad vertical
    - Orientación: Roll, Pitch, Yaw
    - Batería: Voltaje, Corriente, Porcentaje
    - Sistema: Modo, Armado, Satélites GPS

Requisitos:
    pip install dronekit

Uso:
    python3 leer_telemetria_avanzada.py --connect 127.0.0.1:14550 --duracion 30

Parámetros:
    --connect: Dirección de conexión (default: 127.0.0.1:14550)
    --duracion: Tiempo de grabación en segundos (default: 30)
    --archivo: Nombre del archivo CSV (default: telemetria.csv)

Salida:
    - telemetria.csv: Datos tabulados para análisis en Excel/Python
    - Estadísticas en consola

Autor: DroneAcademy.edu
Licencia: MIT
"""

from dronekit import connect
import argparse
import time
import sys
import csv
import os

def main():
    parser = argparse.ArgumentParser(description='Leer y registrar telemetría avanzada')
    parser.add_argument('--connect', default='127.0.0.1:14550',
                        help='Cadena de conexión')
    parser.add_argument('--duracion', type=int, default=30,
                        help='Duración de grabación en segundos (default: 30)')
    parser.add_argument('--archivo', default='telemetria.csv',
                        help='Archivo CSV de salida')

    args = parser.parse_args()

    print("="*60)
    print("LECTURA DE TELEMETRIA AVANZADA")
    print("="*60)
    print(f"\nConectando a: {args.connect}")

    try:
        # Conectar
        vehicle = connect(args.connect, wait_ready=True)
        print("✓ Conectado")

        # Esperar HOME
        print("Esperando ubicación HOME...")
        while vehicle.home_location is None:
            print("  Aguardando GPS fix...")
            time.sleep(1)

        home_lat = vehicle.home_location.lat
        home_lon = vehicle.home_location.lon
        print(f"✓ HOME: ({home_lat:.6f}, {home_lon:.6f})")

        # Crear archivo CSV
        print(f"\nGrabando telemetría en: {args.archivo}")
        print("-" * 60)

        with open(args.archivo, 'w', newline='') as csvfile:
            # Definir encabezados
            fieldnames = [
                'tiempo(s)', 'lat', 'lon', 'alt(m)', 'altitud_relativa(m)',
                'velocidad_aerea(m/s)', 'velocidad_vertical(m/s)',
                'roll(deg)', 'pitch(deg)', 'yaw(deg)',
                'voltaje_bat(V)', 'corriente(A)', 'porcentaje_bat(%)',
                'modo', 'armado', 'satelites_gps', 'vdop'
            ]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Grabación
            start_time = time.time()
            anterior_alt = 0
            anterior_tiempo = 0

            print(f"{'Tiempo':<8} {'Alt':<8} {'V_aire':<8} {'V_vert':<8} "
                  f"{'Roll':<8} {'Pitch':<8} {'Yaw':<8} {'Batería':<10}")
            print("-" * 70)

            while time.time() - start_time < args.duracion:
                elapsed = time.time() - start_time
                actual_tiempo = elapsed

                # Recolectar datos
                try:
                    lat = vehicle.location.global_frame.lat or 0
                    lon = vehicle.location.global_frame.lon or 0
                    alt_gps = vehicle.location.global_frame.alt or 0
                    alt_rel = vehicle.location.global_relative_frame.alt or 0
                    airspeed = vehicle.airspeed or 0
                    groundspeed = vehicle.groundspeed or 0

                    # Calcular velocidad vertical (derivada de altitud)
                    if anterior_tiempo > 0:
                        delta_t = actual_tiempo - anterior_tiempo
                        velocidad_vert = (alt_rel - anterior_alt) / delta_t if delta_t > 0 else 0
                    else:
                        velocidad_vert = 0

                    # Actitudes
                    roll = vehicle.attitude.roll * 180 / 3.14159
                    pitch = vehicle.attitude.pitch * 180 / 3.14159
                    yaw = vehicle.attitude.yaw * 180 / 3.14159

                    # Batería
                    voltaje = vehicle.battery.voltage or 0
                    corriente = vehicle.battery.current or 0
                    porcentaje = vehicle.battery.level or 0

                    # Sistema
                    modo = vehicle.mode.name
                    armado = 1 if vehicle.armed else 0
                    satelites = vehicle.gps_0.satellites_visible or 0
                    vdop = vehicle.gps_0.vdop or 0

                    # Guardar fila
                    writer.writerow({
                        'tiempo(s)': f"{elapsed:.1f}",
                        'lat': f"{lat:.6f}",
                        'lon': f"{lon:.6f}",
                        'alt(m)': f"{alt_gps:.1f}",
                        'altitud_relativa(m)': f"{alt_rel:.1f}",
                        'velocidad_aerea(m/s)': f"{airspeed:.1f}",
                        'velocidad_vertical(m/s)': f"{velocidad_vert:.1f}",
                        'roll(deg)': f"{roll:.1f}",
                        'pitch(deg)': f"{pitch:.1f}",
                        'yaw(deg)': f"{yaw:.1f}",
                        'voltaje_bat(V)': f"{voltaje:.2f}",
                        'corriente(A)': f"{corriente:.1f}",
                        'porcentaje_bat(%)': f"{porcentaje:.0f}",
                        'modo': modo,
                        'armado': armado,
                        'satelites_gps': satelites,
                        'vdop': f"{vdop:.1f}"
                    })

                    # Mostrar en consola
                    print(f"{elapsed:<8.1f} {alt_rel:<8.1f} {airspeed:<8.1f} "
                          f"{velocidad_vert:<8.2f} {roll:<8.1f} {pitch:<8.1f} "
                          f"{yaw:<8.1f} {voltaje:.1f}V")

                    # Guardar para próxima iteración
                    anterior_alt = alt_rel
                    anterior_tiempo = actual_tiempo

                except Exception as e:
                    print(f"  Error leyendo datos: {e}")

                time.sleep(1)

        print("-" * 70)
        print(f"\n✓ Archivo '{args.archivo}' creado exitosamente")

        # Estadísticas
        print("\nEstadísticas capturadas:")
        print("-" * 60)

        if os.path.exists(args.archivo):
            with open(args.archivo, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                rows = list(reader)

                if rows:
                    # Análisis simple
                    altitudes = [float(row['altitud_relativa(m)']) for row in rows]
                    voltajes = [float(row['voltaje_bat(V)']) for row in rows]
                    velocidades = [float(row['velocidad_aerea(m/s)']) for row in rows]

                    print(f"Registros capturados: {len(rows)}")
                    print(f"Duración: {rows[-1]['tiempo(s)']} segundos")
                    print(f"Altitud (min/max/promedio): {min(altitudes):.1f}m / "
                          f"{max(altitudes):.1f}m / {sum(altitudes)/len(altitudes):.1f}m")
                    print(f"Batería (min): {min(voltajes):.2f}V")
                    print(f"Velocidad aérea (max): {max(velocidades):.1f}m/s")

        print("\n" + "="*60)
        print("Análisis:")
        print("  - Abre {} en Excel/Google Sheets para ver gráficas".format(args.archivo))
        print("  - Crea gráficas: Altitud vs Tiempo, Batería vs Tiempo, etc.")
        print("  - Exporta para análisis en MATLAB/Python/R")

        vehicle.close()
        print("\n✓ Desconectado")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
