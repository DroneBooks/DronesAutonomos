#!/usr/bin/env python3
"""Control de dron vía ROS2 + MAVROS — Capítulo 4: ROS2.

Se suscribe al estado del dron y publica setpoints de posición.
Cambia a modo GUIDED y arma el dron tras un breve retardo.
"""

import rclpy
from rclpy.node import Node
from mavros_msgs.msg import State
from mavros_msgs.srv import CommandBool, SetMode
from geometry_msgs.msg import PoseStamped


class ControladorDron(Node):
    def __init__(self):
        super().__init__('controlador_dron')

        # Suscribirse al estado del dron
        self.state_sub = self.create_subscription(
            State,
            '/mavros/state',
            self.state_callback,
            10
        )

        # Publicador de posición objetivo
        self.local_pos_pub = self.create_publisher(
            PoseStamped,
            '/mavros/setpoint_position/local',
            10
        )

        # Clientes para servicios
        self.arming_client = self.create_client(
            CommandBool,
            '/mavros/cmd/arming'
        )

        self.set_mode_client = self.create_client(
            SetMode,
            '/mavros/set_mode'
        )

        # Variables de estado
        self.current_state = State()
        self.contador = 0

        # Timer para enviar comandos
        self.timer = self.create_timer(0.1, self.timer_callback)

    def state_callback(self, msg):
        """Recibe estado actual del dron"""
        self.current_state = msg

        if msg.armed:
            self.get_logger().info('Dron ARMADO')
        else:
            self.get_logger().info('Dron DESARMADO')

    def timer_callback(self):
        """Envía posición objetivo"""
        if not self.current_state.connected:
            self.get_logger().warn('FC no conectado')
            return

        # Crear objetivo de posición
        pose = PoseStamped()
        pose.header.stamp = self.get_clock().now().to_msg()
        pose.header.frame_id = 'map'
        pose.pose.position.x = 0.0
        pose.pose.position.y = 0.0
        pose.pose.position.z = 1.0  # 1 metro de altura

        self.local_pos_pub.publish(pose)

        # Primer intento: cambiar modo a GUIDED
        if self.contador == 10:
            self.set_mode_request(0, 'GUIDED')

        # Segundo intento: armar el dron
        if self.contador == 20:
            self.arm_dron()

        self.contador += 1

    def arm_dron(self):
        """Arma el dron"""
        request = CommandBool.Request()
        request.value = True

        future = self.arming_client.call_async(request)
        self.get_logger().info('Armando dron...')

    def set_mode_request(self, custom_mode, mode_name):
        """Cambia modo de vuelo"""
        request = SetMode.Request()
        request.custom_mode = mode_name

        future = self.set_mode_client.call_async(request)
        self.get_logger().info(f'Cambiando a modo: {mode_name}')


def main(args=None):
    rclpy.init(args=args)
    nodo = ControladorDron()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
