#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 1: Telemetry Launch File
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='apex_telemetry',
            executable='telemetry_publisher',
            name='telemetry_publisher',
            output='screen'
        ),
        Node(
            package='apex_telemetry',
            executable='telemetry_listener',
            name='telemetry_listener',
            output='screen'
        )
    ])
