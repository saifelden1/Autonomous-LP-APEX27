# ROS 2 Command Line Interface (CLI) Quick Reference

Essential commands for daily development in ROS 2 Humble / Jazzy.

---

## 1. Workspace & Build

```bash
# Source ROS 2 system underlay
source /opt/ros/humble/setup.bash

# Build entire workspace with symlinks (edits to Python files apply without rebuilding)
colcon build --symlink-install

# Build a single package only
colcon build --symlink-install --packages-select <package_name>

# Source workspace overlay (run in every new terminal)
source install/setup.bash
```

---

## 2. Running Nodes & Launch Files

```bash
# Run a single executable node
ros2 run <package_name> <executable_name>

# Run a launch file (Python, XML, or YAML)
ros2 launch <package_name> <launch_file_name>.launch.py

# Run a launch file with parameter override
ros2 launch <package_name> <launch_file>.launch.py max_speed:=1.5
```

---

## 3. Topics & Messages

```bash
# List all active topics
ros2 topic list

# Echo live topic data to terminal
ros2 topic echo <topic_name>

# View publish rate (Hz)
ros2 topic hz <topic_name>

# Check topic type and publisher/subscriber count
ros2 topic info <topic_name>

# Check QoS compatibility details
ros2 topic info --verbose <topic_name>

# Publish a single test message from terminal
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}"
```

---

## 4. Services & Actions

```bash
# List all active services
ros2 service list

# Call a service from terminal
ros2 service call /reset_odom std_srvs/srv/Empty {}

# List all active action servers
ros2 action list

# Send an action goal from CLI
ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{pose: {header: {frame_id: 'map'}}}"
```

---

## 5. TF2 Transforms & Diagnostics

```bash
# Generate graphical PDF of the transform tree
ros2 run tf2_tools view_frames

# Check transform between parent and child in real-time
ros2 run tf2_ros tf2_echo odom base_link

# Check active node computation graph
ros2 run rqt_graph rqt_graph
```
