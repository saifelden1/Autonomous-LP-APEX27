# Week 4: AI Prompting Guide & Comprehension Protocol

Working with Gazebo plugins requires careful XML syntax and array indexing when parsing LiDAR ranges.

---

## 1. Prompt Templates for Week 4

### Prompt 1: Parsing Front LiDAR Sector in Python
> "Write a python function for a ROS 2 subscriber callback receiving `sensor_msgs/msg/LaserScan`.
> Extract only the ranges within an angular field of view of $\pm 25^\circ$ directly in front of the robot.
> Filter out `inf`, `NaN`, and readings below `range_min`.
> Return the minimum distance observed in that front sector."

### Prompt 2: Writing an Emergency Brake Node
> "Write a ROS 2 Humble node named `LaserEmergencyBrakeNode`.
> Inputs:
> - Subscribes to `/scan` (`sensor_msgs/msg/LaserScan`)
> - Subscribes to `/teleop_cmd_vel` (`geometry_msgs/msg/Twist`)
> Output:
> - Publishes to `/cmd_vel` (`geometry_msgs/msg/Twist`)
> Behavior:
> - If the minimum distance in the front $40^\circ$ sector drops below parameter `brake_distance` (default 0.75m), publish zero velocity (stop) and log a warning.
> - Otherwise, pass through the velocity command from `/teleop_cmd_vel` to `/cmd_vel`."

### Prompt 3: Debugging Gazebo Model Spawning
> "When launching Gazebo with `ros2 run gazebo_ros spawn_entity.py`, the terminal hangs or outputs:
> `[spawn_entity.py]: Service /spawn_entity unavailable. Was Gazebo started with gazebo_ros_init?`
> Explain how to ensure Gazebo is launched with the ROS 2 factory plugin and correct arguments in a Python launch file."

---

## 2. Common Gazebo Traps

* **Missing Inertial Tags**: If any link with collision geometry lacks an `<inertial>` block in URDF, Gazebo will either crash or spawn the robot into infinite freefall.
* **Massless Wheels**: Wheels with zero mass cannot generate friction contact pairs with the ground plane, causing the robot to slip or sink.
* **Plugin Library Names**: In ROS 2 Humble/Classic Gazebo, plugins end with `.so` (e.g. `libgazebo_ros_diff_drive.so`).
