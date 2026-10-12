#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 6: Path Publisher
Role: Generates and periodically broadcasts a reference path (nav_msgs/Path) for the vehicle to follow.
"""

import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped


class PathPublisherNode(Node):
    """
    Publishes a smooth reference trajectory (S-curve) on /plan at 1 Hz.
    """

    def __init__(self):
        super().__init__('path_publisher_node')

        self.path_pub = self.create_publisher(Path, '/plan', 10)
        self.timer = self.create_timer(1.0, self.publish_path)
        self.get_logger().info('Path Publisher initialized on /plan.')

    def publish_path(self):
        path = Path()
        path.header.stamp = self.get_clock().now().to_msg()
        path.header.frame_id = 'odom'

        # Generate S-curve path from x = 0 to x = 12 meters
        num_points = 60
        for i in range(num_points):
            x = (i / float(num_points)) * 12.0
            y = 2.0 * math.sin(x * 0.5)

            pose = PoseStamped()
            pose.header.stamp = path.header.stamp
            pose.header.frame_id = 'odom'
            pose.pose.position.x = float(x)
            pose.pose.position.y = float(y)
            pose.pose.position.z = 0.0

            # Compute local tangential heading for orientation
            dy_dx = math.cos(x * 0.5)
            yaw = math.atan(dy_dx)
            pose.pose.orientation.z = math.sin(yaw / 2.0)
            pose.pose.orientation.w = math.cos(yaw / 2.0)

            path.poses.append(pose)

        self.path_pub.publish(path)


def main(args=None):
    rclpy.init(args=args)
    node = PathPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
