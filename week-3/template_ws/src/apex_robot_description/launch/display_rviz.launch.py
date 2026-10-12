#!/usr/bin/env python3
"""
Launch file to display the APEX robot model in RViz2 with dynamic TF broadcasting.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('apex_robot_description')
    xacro_file = os.path.join(pkg_share, 'urdf', 'apex_chassis.urdf.xacro')

    # Convert Xacro to URDF representation
    robot_description = Command(['xacro ', xacro_file])

    # Node: robot_state_publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # Node: dynamic TF broadcaster
    odom_tf_node = Node(
        package='apex_robot_description',
        executable='odom_tf_broadcaster',
        name='odom_tf_broadcaster',
        output='screen'
    )

    # Node: rviz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', '/opt/ros/humble/share/rviz2/default.rviz'] if False else []
    )

    return LaunchDescription([
        robot_state_publisher_node,
        odom_tf_node,
        rviz_node
    ])
