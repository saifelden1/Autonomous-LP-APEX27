#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 1: Telemetry Listener
Role: Subscribes to vehicle telemetry and prints messages to console.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class TelemetryListenerNode(Node):
    def __init__(self):
        super().__init__('telemetry_listener_node')
        self.subscription = self.create_subscription(
            String,
            '/vehicle/telemetry',
            self.listener_callback,
            10
        )
        self.get_logger().info('Telemetry Listener started. Waiting for messages...')

    def listener_callback(self, msg: String):
        self.get_logger().info(f'Received telemetry: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = TelemetryListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
