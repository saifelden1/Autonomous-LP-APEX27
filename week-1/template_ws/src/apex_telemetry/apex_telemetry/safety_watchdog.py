#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 1: Safety Watchdog
Role: Monitors telemetry heartbeat. If telemetry drops, commands E-Stop.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool


class SafetyWatchdogNode(Node):
    """
    Monitors incoming telemetry and triggers emergency stop if messages stop arriving.
    """

    def __init__(self):
        super().__init__('safety_watchdog_node')

        # Declare configurable timeout parameter
        self.declare_parameter('timeout_sec', 0.5)
        self.timeout_sec = (
            self.get_parameter('timeout_sec').get_parameter_value().double_value
        )

        # Create subscriber to telemetry
        self.subscription = self.create_subscription(
            String,
            '/vehicle/telemetry',
            self.telemetry_callback,
            10
        )

        # Create publisher for E-Stop trigger
        self.estop_pub = self.create_publisher(
            Bool,
            '/safety/estop_trigger',
            10
        )

        # Record timestamp of last received packet (clock time)
        self.last_heartbeat_time = self.get_clock().now()
        self.estop_active = False

        # Run watchdog monitor timer at 20 Hz (every 50 ms)
        self.watchdog_timer = self.create_timer(0.05, self.check_heartbeat)

        self.get_logger().info(
            f'Safety Watchdog initialized with timeout = {self.timeout_sec} seconds.'
        )

    def telemetry_callback(self, msg: String):
        """
        Invoked each time a new telemetry message is received.
        """
        self.last_heartbeat_time = self.get_clock().now()

        # If we were previously in E-Stop state and telemetry is restored
        if self.estop_active:
            self.estop_active = False
            self.get_logger().info('Telemetry restored. Resetting E-STOP.')
            estop_msg = Bool()
            estop_msg.data = False
            self.estop_pub.publish(estop_msg)

    def check_heartbeat(self):
        """
        Periodic watchdog inspection: compares current time to last received heartbeat.
        """
        now = self.get_clock().now()
        elapsed_sec = (now - self.last_heartbeat_time).nanoseconds / 1e9

        estop_msg = Bool()

        if elapsed_sec > self.timeout_sec:
            if not self.estop_active:
                self.estop_active = True
                self.get_logger().error(
                    f'CRITICAL: Telemetry timeout ({elapsed_sec:.2f}s > {self.timeout_sec}s)! TRIGGERING E-STOP!'
                )
            estop_msg.data = True
        else:
            estop_msg.data = False

        # Publish current state
        self.estop_pub.publish(estop_msg)


def main(args=None):
    rclpy.init(args=args)
    node = SafetyWatchdogNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Safety Watchdog stopped by user.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
