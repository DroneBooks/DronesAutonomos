/*
 * nodo_subscriber.cpp — Nodo ROS2 suscriptor de telemetría de dron
 *
 * Este es un ejemplo de nodo ROS2 en C++ que:
 * 1. Se suscribe a tópicos de telemetría
 * 2. Recibe mensajes y los procesa en callbacks
 * 3. Implementa lógica de control simple
 *
 * Compilación:
 *   cd ~/ros2_ws && colcon build --packages-select drone_telemetry
 *
 * Ejecución (ejecuta primero nodo_publisher en otra terminal):
 *   source install/setup.bash
 *   ros2 run drone_telemetry nodo_subscriber
 *
 * Conceptos clave (del Anexo A2):
 * - Suscripción con create_subscription<T>
 * - Callbacks (std::function) que procesan mensajes
 * - Referencias const para evitar copias innecesarias
 * - Lógica de control basada en datos de entrada
 */

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float64.hpp"

class NodoSuscriptorTelemetria : public rclcpp::Node {
public:
    NodoSuscriptorTelemetria() : Node("telemetria_subscriber"),
                                  altitud_actual_(0.0),
                                  bateria_actual_(100.0),
                                  velocidad_actual_(0.0) {
        /*
         * Suscribirse a tópicos de telemetría.
         * Parámetro 10: queue size (máximo de mensajes pendientes).
         *
         * Usar std::bind para vincular método callback a instancia.
         * Signature: void callback(const std_msgs::msg::Float64::SharedPtr msg)
         */
        sub_altitud_ = create_subscription<std_msgs::msg::Float64>(
            "/telemetria/altitud", 10,
            std::bind(&NodoSuscriptorTelemetria::callback_altitud, this,
                      std::placeholders::_1));

        sub_bateria_ = create_subscription<std_msgs::msg::Float64>(
            "/telemetria/bateria", 10,
            std::bind(&NodoSuscriptorTelemetria::callback_bateria, this,
                      std::placeholders::_1));

        sub_velocidad_ = create_subscription<std_msgs::msg::Float64>(
            "/telemetria/velocidad", 10,
            std::bind(&NodoSuscriptorTelemetria::callback_velocidad, this,
                      std::placeholders::_1));

        RCLCPP_INFO(get_logger(),
                    "✅ Nodo suscriptor iniciado — escuchando /telemetria/*");
    }

private:
    /*
     * Callback para altitud.
     * Se ejecuta CADA VEZ que llega un mensaje en /telemetria/altitud.
     *
     * const auto&: referencia const (evita copia innecesaria).
     * SharedPtr: puntero inteligente (RAII, auto-destrucción).
     */
    void callback_altitud(const std_msgs::msg::Float64::SharedPtr msg) {
        altitud_actual_ = msg->data;

        // Lógica de control: alertar si altitud es baja
        if (altitud_actual_ < 2.0) {
            RCLCPP_WARN(get_logger(),
                        "⚠️  ALERTA: Altitud muy baja: %.2f m", altitud_actual_);
        }
    }

    /*
     * Callback para batería.
     * Lógica: avisar si batería está bajo crítico (< 15%).
     */
    void callback_bateria(const std_msgs::msg::Float64::SharedPtr msg) {
        bateria_actual_ = msg->data;

        if (bateria_actual_ < 15.0) {
            RCLCPP_ERROR(
                get_logger(),
                "🔴 CRÍTICO: Batería muy baja: %.1f%% — RETURN TO HOME",
                bateria_actual_);
        } else if (bateria_actual_ < 30.0) {
            RCLCPP_WARN(get_logger(),
                        "🟠 AVISO: Batería baja: %.1f%%", bateria_actual_);
        }
    }

    /*
     * Callback para velocidad.
     * Implementar limitación de velocidad máxima.
     */
    void callback_velocidad(const std_msgs::msg::Float64::SharedPtr msg) {
        velocidad_actual_ = msg->data;

        const double MAX_VELOCIDAD = 15.0;  // m/s
        if (velocidad_actual_ > MAX_VELOCIDAD) {
            RCLCPP_WARN(get_logger(),
                        "⚠️  Velocidad excede límite: %.2f m/s (máx: %.1f)",
                        velocidad_actual_, MAX_VELOCIDAD);
        }
    }

public:
    /*
     * Getter para acceder a datos actuales (útil en otros nodos).
     * Nota: en multi-threading, esto necesitaría un mutex para seguridad.
     */
    double get_altitud() const { return altitud_actual_; }
    double get_bateria() const { return bateria_actual_; }
    double get_velocidad() const { return velocidad_actual_; }

    /*
     * Método de ejemplo: lógica de decisión basada en telemetría.
     * Retorna true si el dron es seguro para volar.
     */
    bool es_seguro_volar() const {
        return (bateria_actual_ > 20.0) &&  // Batería suficiente
               (altitud_actual_ >= 0.5);    // No en suelo
    }

private:
    // Subscriptores
    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr sub_altitud_;
    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr sub_bateria_;
    rclcpp::Subscription<std_msgs::msg::Float64>::SharedPtr sub_velocidad_;

    // Variables miembro: estado actual
    double altitud_actual_;
    double bateria_actual_;
    double velocidad_actual_;
};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);
    auto nodo = std::make_shared<NodoSuscriptorTelemetria>();
    rclcpp::spin(nodo);
    rclcpp::shutdown();
    return 0;
}
