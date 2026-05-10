#!/usr/bin/env python3
"""Navegación a Puntos de Interés (POI) con Nav2 — Capítulo 4: ROS2.

Vuela a una lista de coordenadas (x, y, z) secuencialmente usando Nav2.
"""

import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
import geometry_msgs.msg as geometry_msgs
from rclpy.duration import Duration


class NavigadorPOI(Node):
    def __init__(self):
        super().__init__('navegador_poi')
        self.navigator = BasicNavigator()

    def volar_a_punto(self, x, y, z):
        """Vuela a coordenada (x, y, z)"""

        # Esperar a que Nav2 esté listo
        self.navigator.waitUntilNav2Active()
        self.get_logger().info('Nav2 activo')

        # Crear objetivo
        goal_pose = geometry_msgs.PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.get_clock().now().to_msg()
        goal_pose.pose.position.x = float(x)
        goal_pose.pose.position.y = float(y)
        goal_pose.pose.position.z = float(z)
        goal_pose.pose.orientation.w = 1.0

        self.get_logger().info(
            f'Navegando a: ({x}, {y}, {z})'
        )

        # Enviar objetivo
        self.navigator.goToPose(goal_pose)

        # Monitorear progreso
        i = 0
        while not self.navigator.isTaskComplete():
            i += 1
            feedback = self.navigator.getFeedback()
            if feedback:
                self.get_logger().info(
                    f'Progreso: {i} ciclos, distancia: '
                    f'{feedback.distance_remaining:.2f} m'
                )

            # Timeout: 30 segundos
            if Duration(seconds=i * 0.1) > Duration(seconds=30):
                self.navigator.cancelTask()
                self.get_logger().warn('Timeout alcanzado')
                break

        # Resultado
        result = self.navigator.getResult()
        if result:
            self.get_logger().info('Navegación completada OK')
        else:
            self.get_logger().error('Navegación falló')

    def volar_a_multiples_puntos(self, puntos):
        """Vuela a múltiples puntos secuencialmente.

        Args:
            puntos: Lista de tuplas (x, y, z)
        """
        for i, (x, y, z) in enumerate(puntos):
            self.get_logger().info(
                f'Punto {i + 1}/{len(puntos)}'
            )
            self.volar_a_punto(x, y, z)


def main(args=None):
    rclpy.init(args=args)
    nodo = NavigadorPOI()

    # Definir puntos de interés (POI)
    pois = [
        (10.0, 0.0, 5.0),    # POI 1
        (10.0, 10.0, 5.0),   # POI 2
        (0.0, 10.0, 5.0),    # POI 3
        (0.0, 0.0, 5.0),     # POI 4 (vuelta al inicio)
    ]

    nodo.volar_a_multiples_puntos(pois)

    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
