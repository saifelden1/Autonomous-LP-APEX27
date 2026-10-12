#!/usr/bin/env python3
"""
Launch file to display the APEX robot model in RViz2 with joint_state_publisher_gui.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    pkg_share = get_package_share_directory('apex_robot_description')
    xacro_file = os.path.join(pkg_share, 'urdf', 'apex_chassis.urdf.xacro')

    robot_description = Command(['xacro ', xacro_file])

    # 1. Robot State Publisher (publishes TF tree from robot_description and joint_states)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # 2. Joint State Publisher GUI (slider interface to rotate joints manually)
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # 3. RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
