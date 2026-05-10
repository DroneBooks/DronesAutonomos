#!/usr/bin/env python3
"""Nodo publicador ROS2 simple — Capítulo 4: ROS2.

Publica un mensaje de texto en el tópico 'mensaje' cada segundo.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinPublicador(Node):
    def __init__(self):
        super().__init__('mi_publicador')

        # Crear publicador en tópico 'mensaje'
        self.publisher_ = self.create_publisher(
            String,
            'mensaje',  # Nombre del tópico
            10          # Profundidad de cola
        )

        # Crear timer para enviar cada 1 segundo
        self.timer_period = 1.0
        self.timer = self.create_timer(
            self.timer_period,
            self.timer_callback
        )

        # Contador para demostración
        self.contador = 0

    def timer_callback(self):
        """Función llamada cada 1 segundo"""
        msg = String()
        msg.data = f'Mensaje #{self.contador}'

        # Publicar mensaje
        self.publisher_.publish(msg)

        # Loguear
        self.get_logger().info(f'Publicando: {msg.data}')

        self.contador += 1


def main(args=None):
    # Inicializar ROS2
    rclpy.init(args=args)

    # Crear nodo
    nodo = MinPublicador()

    # Ejecutar continuamente
    rclpy.spin(nodo)

    # Cleanup
    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
