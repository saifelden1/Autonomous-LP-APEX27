#!/usr/bin/env python3
"""
Launch file for Week 2: Starts Mission Coordinator with launch arguments.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    default_speed_arg = DeclareLaunchArgument(
        'default_speed',
        default_value='1.5',
        description='Default vehicle traversal speed in m/s'
    )

    mission_node = Node(
        package='apex_mission_pkg',
        executable='mission_coordinator',
        name='mission_coordinator',
        output='screen',
        parameters=[{
            'default_speed': LaunchConfiguration('default_speed'),
        }]
    )

    return LaunchDescription([
        default_speed_arg,
        mission_node
    ])
