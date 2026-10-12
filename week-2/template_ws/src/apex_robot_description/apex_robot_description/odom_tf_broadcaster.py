#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 3: Odom TF Broadcaster
Role: Computes simulated vehicle trajectory and broadcasts dynamic odom -> base_link transform.
"""

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class OdomTFBroadcasterNode(Node):
    """
    Broadcasts dynamic transforms from odom to base_link simulating circular movement.
    """

    def __init__(self):
        super().__init__('odom_tf_broadcaster_node')

        self.tf_broadcaster = TransformBroadcaster(self)

        # Configurable trajectory parameters
        self.declare_parameter('radius', 1.5)
        self.declare_parameter('angular_speed', 0.5)

        self.radius = self.get_parameter('radius').get_parameter_value().double_value
        self.angular_speed = (
            self.get_parameter('angular_speed').get_parameter_value().double_value
        )

        self.start_time = self.get_clock().now()

        # Broadcast at 30 Hz
        self.timer = self.create_timer(1.0 / 30.0, self.broadcast_transform)
        self.get_logger().info('Odom TF Broadcaster active at 30 Hz.')

    def broadcast_transform(self):
        now = self.get_clock().now()
        t = (now - self.start_time).nanoseconds / 1e9

        # Circular trajectory equations
        theta = self.angular_speed * t
        x = self.radius * math.cos(theta) - self.radius
        y = self.radius * math.sin(theta)
        heading = theta + (math.pi / 2.0)

        # Planar yaw to quaternion conversion (Z-axis rotation only)
        qz = math.sin(heading / 2.0)
        qw = math.cos(heading / 2.0)

        t_msg = TransformStamped()
        t_msg.header.stamp = now.to_msg()
        t_msg.header.frame_id = 'odom'
        t_msg.child_frame_id = 'base_link'

        t_msg.transform.translation.x = x
        t_msg.transform.translation.y = y
        t_msg.transform.translation.z = 0.0

        t_msg.transform.rotation.x = 0.0
        t_msg.transform.rotation.y = 0.0
        t_msg.transform.rotation.z = qz
        t_msg.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(t_msg)


def main(args=None):
    rclpy.init(args=args)
    node = OdomTFBroadcasterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Odom TF Broadcaster stopped.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
