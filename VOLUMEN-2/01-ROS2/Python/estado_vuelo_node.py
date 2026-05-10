#!/usr/bin/env python3
"""Monitor de estado de vuelo — Capítulo 4: ROS2.

Se suscribe a cuatro tópicos MAVROS simultáneamente (estado, GPS, batería, IMU)
y publica un resumen en JSON en /drone/estado_vuelo cada 2 segundos.
"""

import json
from math import sqrt

import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State
from sensor_msgs.msg import NavSatFix, BatteryState, Imu
from std_msgs.msg import String


class EstadoVueloNode(Node):

    def __init__(self):
        super().__init__('estado_vuelo')

        self._estado = {
            'conectado': False,
            'armado': False,
            'modo': 'DESCONOCIDO',
            'lat': 0.0,
            'lon': 0.0,
            'alt_m': 0.0,
            'bateria_pct': 0.0,
            'bateria_v': 0.0,
            'aceleracion_m_s2': 0.0,
        }

        # Cuatro suscriptores MAVROS
        self.create_subscription(
            State, '/mavros/state', self._cb_state, 10)
        self.create_subscription(
            NavSatFix, '/mavros/global_position/global',
            self._cb_gps, 10)
        self.create_subscription(
            BatteryState, '/mavros/battery',
            self._cb_battery, 10)
        self.create_subscription(
            Imu, '/mavros/imu/data', self._cb_imu, 10)

        # Publicador de resumen en JSON
        self._pub = self.create_publisher(String,
            '/drone/estado_vuelo', 10)

        # Publicar cada 2 segundos
        self.create_timer(2.0, self._publicar_resumen)
        self.get_logger().info('EstadoVuelo iniciado...')

    def _cb_state(self, msg):
        self._estado['conectado'] = msg.connected
        self._estado['armado']    = msg.armed
        self._estado['modo']      = msg.mode

    def _cb_gps(self, msg):
        self._estado['lat']   = round(msg.latitude, 6)
        self._estado['lon']   = round(msg.longitude, 6)
        self._estado['alt_m'] = round(msg.altitude, 1)

    def _cb_battery(self, msg):
        self._estado['bateria_v']   = round(msg.voltage, 2)
        pct = msg.percentage
        self._estado['bateria_pct'] = round(pct * 100, 1) \
            if pct == pct else -1.0

    def _cb_imu(self, msg):
        ax, ay, az = (msg.linear_acceleration.x,
                      msg.linear_acceleration.y,
                      msg.linear_acceleration.z)
        self._estado['aceleracion_m_s2'] = round(
            sqrt(ax**2 + ay**2 + az**2), 2)

    def _publicar_resumen(self):
        msg = String()
        msg.data = json.dumps(self._estado, ensure_ascii=False)
        self._pub.publish(msg)

        e = self._estado
        self.get_logger().info(
            f"{'ARMADO' if e['armado'] else 'DESARMADO'} | "
            f"Modo:{e['modo']} | Alt:{e['alt_m']}m | "
            f"Bat:{e['bateria_pct']}%"
        )

        if e['bateria_pct'] != -1.0 and e['bateria_pct'] < 20.0:
            self.get_logger().warn(
                f"BATERIA BAJA: {e['bateria_pct']}%")


def main(args=None):
    rclpy.init(args=args)
    nodo = EstadoVueloNode()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
