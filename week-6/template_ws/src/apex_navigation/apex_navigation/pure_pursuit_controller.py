#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 6: Pure Pursuit Controller
Role: Implements geometric path tracking from /plan and vehicle odometry to /cmd_vel.
"""

import math
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import Twist


class PurePursuitControllerNode(Node):
    """
    Subscribes to target path and odometry, tracks path using Pure Pursuit algorithm,
    and publishes velocity commands to /cmd_vel.
    """

    def __init__(self):
        super().__init__('pure_pursuit_controller_node')

        # Configurable controller parameters
        self.declare_parameter('lookahead_distance', 1.0)
        self.declare_parameter('target_velocity', 0.8)
        self.declare_parameter('goal_tolerance', 0.4)

        self.lookahead_dist = (
            self.get_parameter('lookahead_distance').get_parameter_value().double_value
        )
        self.target_vel = (
            self.get_parameter('target_velocity').get_parameter_value().double_value
        )
        self.goal_tolerance = (
            self.get_parameter('goal_tolerance').get_parameter_value().double_value
        )

        # Vehicle state
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0
        self.odom_received = False

        # Path storage
        self.current_path = []

        # Subscriptions
        self.path_sub = self.create_subscription(Path, '/plan', self.path_callback, 10)
        self.odom_sub = self.create_subscription(
            Odometry, '/wheel/odom', self.odom_callback, 10
        )

        # Publisher to motor controller
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Control loop at 20 Hz (50 ms)
        self.timer = self.create_timer(0.05, self.control_loop)
        self.get_logger().info(
            f'Pure Pursuit Controller active: Ld = {self.lookahead_dist}m, Speed = {self.target_vel}m/s.'
        )

    def path_callback(self, msg: Path):
        self.current_path = [
            (pose.pose.position.x, pose.pose.position.y) for pose in msg.poses
        ]

    def odom_callback(self, msg: Odometry):
        self.odom_received = True
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y

        # Convert quaternion to yaw angle
        qz = msg.pose.pose.orientation.z
        qw = msg.pose.pose.orientation.w
        self.current_yaw = 2.0 * math.atan2(qz, qw)

    def control_loop(self):
        if not self.odom_received or not self.current_path:
            return

        cmd = Twist()

        # Check distance to final goal waypoint
        final_x, final_y = self.current_path[-1]
        dist_to_goal = math.hypot(final_x - self.current_x, final_y - self.current_y)

        if dist_to_goal < self.goal_tolerance:
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0
            self.cmd_pub.publish(cmd)
            self.get_logger().info('CAPSTONE COMPLETE! Target waypoint course finished.', once=True)
            return

        # Find lookahead target point
        target_pt = None
        for px, py in self.current_path:
            d = math.hypot(px - self.current_x, py - self.current_y)
            if d >= self.lookahead_dist:
                target_pt = (px, py)
                break

        if target_pt is None:
            target_pt = self.current_path[-1]

        # Calculate angle alpha between vehicle heading and target point
        gx, gy = target_pt
        target_angle = math.atan2(gy - self.current_y, gx - self.current_x)
        alpha = target_angle - self.current_yaw

        # Normalize alpha to [-pi, pi]
        alpha = math.atan2(math.sin(alpha), math.cos(alpha))

        # Pure Pursuit curvature: kappa = 2 * sin(alpha) / Ld
        actual_ld = max(math.hypot(gx - self.current_x, gy - self.current_y), 0.1)
        curvature = 2.0 * math.sin(alpha) / actual_ld

        # Compute commands
        cmd.linear.x = float(self.target_vel)
        cmd.angular.z = float(self.target_vel * curvature)

        # Bound maximum angular velocity to prevent aggressive spins
        cmd.angular.z = max(min(cmd.angular.z, 1.5), -1.5)

        self.cmd_pub.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = PurePursuitControllerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
