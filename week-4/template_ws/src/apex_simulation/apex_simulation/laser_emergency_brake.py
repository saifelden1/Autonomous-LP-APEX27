#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 4: Laser Emergency Braking (AEB)
Role: Multiplexes /teleop_cmd_vel to /cmd_vel with automatic front laser obstacle braking.
"""

import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class LaserEmergencyBrakeNode(Node):
    """
    Monitors 2D laser scan in the front sector. If obstacle is closer than threshold,
    suppresses velocity commands and brings vehicle to an emergency halt.
    """

    def __init__(self):
        super().__init__('laser_emergency_brake_node')

        # Configurable parameters
        self.declare_parameter('brake_distance', 0.75)
        self.declare_parameter('front_angle_deg', 30.0)

        self.brake_distance = (
            self.get_parameter('brake_distance').get_parameter_value().double_value
        )
        self.front_angle_deg = (
            self.get_parameter('front_angle_deg').get_parameter_value().double_value
        )

        # Minimum distance detected in front sector
        self.closest_obstacle_m = float('inf')
        self.brake_engaged = False

        # Subscriptions
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )
        self.teleop_sub = self.create_subscription(
            Twist,
            '/teleop_cmd_vel',
            self.teleop_callback,
            10
        )

        # Output publisher to vehicle motor plugin
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info(
            f'Laser Emergency Brake active: threshold = {self.brake_distance}m, sector = ±{self.front_angle_deg}°.'
        )

    def scan_callback(self, scan_msg: LaserScan):
        """
        Parses LiDAR ranges in the forward angular cone.
        """
        front_angle_rad = math.radians(self.front_angle_deg)
        min_range = float('inf')

        for i, dist in enumerate(scan_msg.ranges):
            # Calculate beam angle
            angle = scan_msg.angle_min + i * scan_msg.angle_increment

            # Only inspect rays within ±front_angle_deg
            if -front_angle_rad <= angle <= front_angle_rad:
                if scan_msg.range_min <= dist <= scan_msg.range_max:
                    if dist < min_range:
                        min_range = dist

        self.closest_obstacle_m = min_range

    def teleop_callback(self, teleop_cmd: Twist):
        """
        Forwards command if path is clear; overrides to zero if obstacle detected.
        """
        cmd_out = Twist()

        # If driving forward and obstacle is dangerously close
        if teleop_cmd.linear.x > 0.0 and self.closest_obstacle_m < self.brake_distance:
            if not self.brake_engaged:
                self.brake_engaged = True
                self.get_logger().warn(
                    f'EMERGENCY BRAKE ENGAGED! Obstacle at {self.closest_obstacle_m:.2f}m (< {self.brake_distance}m)!'
                )
            cmd_out.linear.x = 0.0
            cmd_out.angular.z = 0.0
        else:
            if self.brake_engaged and self.closest_obstacle_m >= self.brake_distance:
                self.brake_engaged = False
                self.get_logger().info('Obstacle cleared. Emergency brake disengaged.')
            cmd_out = teleop_cmd

        self.cmd_vel_pub.publish(cmd_out)


def main(args=None):
    rclpy.init(args=args)
    node = LaserEmergencyBrakeNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Laser Emergency Brake stopped.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
