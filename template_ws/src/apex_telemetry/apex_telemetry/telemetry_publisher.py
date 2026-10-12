#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 1: Telemetry Publisher
Role: Broadcasts periodic vehicle health status over ROS 2 topic bus.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TelemetryPublisherNode(Node):
    """
    Node that simulates vehicle telemetry (battery voltage, sequence ID, status).
    """

    def __init__(self):
        super().__init__('telemetry_publisher_node')

        # Declare publishing parameters
        self.declare_parameter('publish_rate_hz', 10.0)
        rate = self.get_parameter('publish_rate_hz').get_parameter_value().double_value

        # Create publisher on /vehicle/telemetry
        self.publisher_ = self.create_publisher(String, '/vehicle/telemetry', 10)

        # Create timer callback
        timer_period = 1.0 / rate if rate > 0 else 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.seq_id = 0
        self.get_logger().info(f'Telemetry Publisher started at {rate} Hz.')

    def timer_callback(self):
        """
        Publishes telemetry frame periodically.
        """
        msg = String()
        # Simulated battery voltage fluctuating between 24.5V and 25.5V
        simulated_voltage = 25.0 + 0.1 * (self.seq_id % 5)
        
        # Telemetry payload
        msg.data = f"seq={self.seq_id},voltage={simulated_voltage:.2f}V,status=HEALTHY"
        self.publisher_.publish(msg)
        self.get_logger().debug(f'Published: "{msg.data}"')

        self.seq_id += 1


def main(args=None):
    rclpy.init(args=args)
    node = TelemetryPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Telemetry Publisher stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
