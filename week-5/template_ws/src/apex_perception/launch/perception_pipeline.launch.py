#!/usr/bin/env python3
"""
Launch file for Week 5: Starts Synthetic Camera and Cone Detector together.
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    camera_node = Node(
        package='apex_perception',
        executable='synthetic_camera_publisher',
        name='synthetic_camera_publisher',
        output='screen'
    )

    detector_node = Node(
        package='apex_perception',
        executable='cone_detector',
        name='cone_detector',
        output='screen'
    )

    return LaunchDescription([
        camera_node,
        detector_node
    ])
