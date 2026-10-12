#!/usr/bin/env python3
"""
Launch file to start Gazebo, spawn the robot with sensors, and open RViz2.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description():
    sim_pkg_share = get_package_share_directory('apex_simulation')
    gazebo_ros_share = get_package_share_directory('gazebo_ros')

    xacro_file = os.path.join(sim_pkg_share, 'urdf', 'apex_sim_chassis.urdf.xacro')
    robot_description = Command(['xacro ', xacro_file])

    # 1. Gazebo Server & Client (empty world)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_share, 'launch', 'gazebo.launch.py')
        )
    )

    # 2. Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    # 3. Spawn Entity into Gazebo
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'apex_rover', '-z', '0.2'],
        output='screen'
    )

    # 4. RViz2
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity,
        rviz
    ])
