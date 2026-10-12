#!/usr/bin/env python3
"""
Launch file to start Gazebo with the custom APEX arena world.
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('apex_gazebo_worlds')
    gazebo_ros_share = get_package_share_directory('gazebo_ros')

    world_file = os.path.join(pkg_share, 'worlds', 'apex_arena.world')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_share, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_file}.items()
    )

    return LaunchDescription([gazebo])
