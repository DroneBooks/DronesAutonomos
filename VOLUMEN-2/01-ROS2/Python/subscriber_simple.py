#!/usr/bin/env python3
"""Nodo suscriptor ROS2 simple — Capítulo 4: ROS2.

Se suscribe al tópico 'mensaje' y loguea cada mensaje recibido.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MiSuscriptor(Node):
    def __init__(self):
        super().__init__('mi_suscriptor')

        # Suscribirse al tópico 'mensaje'
        self.subscription = self.create_subscription(
            String,
            'mensaje',
            self.listener_callback,
            10  # Profundidad de cola
        )
        self.subscription  # Prevenir warning

    def listener_callback(self, msg):
        """Llamada cuando llega un nuevo mensaje"""
        self.get_logger().info(f'Recibido: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    nodo = MiSuscriptor()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
