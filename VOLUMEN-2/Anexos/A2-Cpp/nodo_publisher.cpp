/*
 * nodo_publisher.cpp — Nodo ROS2 publicador de telemetría de dron
 *
 * Este es un ejemplo mínimo de nodo ROS2 en C++ que:
 * 1. Publica datos de telemetría (altitud, velocidad, batería)
 * 2. Usa un timer para publicar periódicamente (500 ms)
 * 3. Demuestra sintaxis C++ esencial para ROS2
 *
 * Compilación:
 *   cd ~/ros2_ws && colcon build --packages-select drone_telemetry
 *
 * Ejecución:
 *   source install/setup.bash
 *   ros2 run drone_telemetry nodo_publisher
 *
 * Escuchar en otra terminal:
 *   ros2 topic echo /telemetria/altitud
 *   ros2 topic echo /telemetria/bateria
 *   ros2 topic echo /telemetria/velocidad
 *
 * Conceptos clave (del Anexo A2):
 * - Clase que hereda de rclcpp::Node
 * - Publisher<T> para enviar mensajes tipados
 * - Timer periódico con std::bind
 * - Logging con RCLCPP_INFO
 */

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"
#include <cmath>

class NodoPublicadorTelemetria : public rclcpp::Node {
public:
    NodoPublicadorTelemetria() : Node("telemetria_publisher"), contador_(0) {
        /*
         * Crear publishers para tres tópicos:
         * - /telemetria/altitud    (metros)
         * - /telemetria/bateria    (porcentaje 0-100)
         * - /telemetria/velocidad  (m/s)
         *
         * Parámetro 10: buffer de historiador (queue size)
         */
        pub_altitud_ = create_publisher<std_msgs::msg::Float64>(
            "/telemetria/altitud", 10);
        pub_bateria_ = create_publisher<std_msgs::msg::Float64>(
            "/telemetria/bateria", 10);
        pub_velocidad_ = create_publisher<std_msgs::msg::Float64>(
            "/telemetria/velocidad", 10);

        /*
         * Timer periódico: ejecuta callback cada 500 ms.
         * std::bind vincula el método a la instancia de la clase.
         */
        timer_ = create_wall_timer(
            std::chrono::milliseconds(500),
            std::bind(&NodoPublicadorTelemetria::callback_publicar, this));

        RCLCPP_INFO(get_logger(),
                    "✅ Nodo publicador iniciado — tópicos: /telemetria/*");
    }

private:
    void callback_publicar() {
        /*
         * Simular telemetría variante (en producción: leer de Pixhawk).
         * Patrones: altitud sube y baja, batería disminuye, velocidad oscila.
         */
        contador_++;

        // Simular altitud variante (0-30 metros, patrón sinusoidal)
        double altitud = 10.0 + 8.0 * std::sin(contador_ * 0.1);

        // Simular batería (comienza 100%, decrece lentamente)
        double bateria = 100.0 - (contador_ * 0.1);
        bateria = (bateria < 0) ? 0 : bateria;

        // Simular velocidad (0-5 m/s, patrón triangular)
        double velocidad = 2.5 + 1.5 * std::sin(contador_ * 0.05);

        // Crear mensajes
        auto msg_alt = std_msgs::msg::Float64();
        msg_alt.data = altitud;

        auto msg_bat = std_msgs::msg::Float64();
        msg_bat.data = bateria;

        auto msg_vel = std_msgs::msg::Float64();
        msg_vel.data = velocidad;

        // Publicar
        pub_altitud_->publish(msg_alt);
        pub_bateria_->publish(msg_bat);
        pub_velocidad_->publish(msg_vel);

        // Log cada 4 ciclos (cada 2 segundos)
        if (contador_ % 4 == 0) {
            RCLCPP_INFO(
                get_logger(),
                "📡 Altitud: %.2f m | Batería: %.1f%% | Velocidad: %.2f m/s",
                altitud, bateria, velocidad);
        }
    }

    // Miembros privados
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr pub_altitud_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr pub_bateria_;
    rclcpp::Publisher<std_msgs::msg::Float64>::SharedPtr pub_velocidad_;
    rclcpp::TimerBase::SharedPtr timer_;
    int contador_;
};

int main(int argc, char* argv[]) {
    /*
     * Inicializar ROS2: debe ser lo primero.
     * Argumentos: argc, argv (permite pasar parámetros por línea).
     */
    rclcpp::init(argc, argv);

    /*
     * Crear instancia del nodo y pasarla a spin().
     * spin() bloquea hasta que se señale shutdown.
     * std::make_shared: crea puntero compartido (patrón C++11).
     */
    auto nodo = std::make_shared<NodoPublicadorTelemetria>();
    rclcpp::spin(nodo);

    /* Shutdown: limpia recursos y detiene el nodo. */
    rclcpp::shutdown();
    return 0;
}
