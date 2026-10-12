#!/usr/bin/env python3
"""
Launch file for Week 6 Capstone: Starts Path Publisher and Pure Pursuit Controller.
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    path_node = Node(
        package='apex_navigation',
        executable='path_publisher',
        name='path_publisher',
        output='screen'
    )

    controller_node = Node(
        package='apex_navigation',
        executable='pure_pursuit_controller',
        name='pure_pursuit_controller',
        output='screen',
        parameters=[{
            'lookahead_distance': 1.0,
            'target_velocity': 0.8,
            'goal_tolerance': 0.4
        }]
    )

    return LaunchDescription([
        path_node,
        controller_node
    ])
