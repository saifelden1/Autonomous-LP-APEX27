# Week 4: Model Deployment in Gazebo & Sensor Streaming into RViz

Welcome to Week 4! This week brings everything together: you deploy your robot model into the Gazebo arena, drive it with teleoperation, stream live sensors into RViz, and inspect the computational graph with `rqt_graph`.

---

## 1. The Simulation-to-Visualization Bridge

Here is the exact data pipeline running between Gazebo, ROS 2, and RViz:

```
+-------------------------------------------------------------+
|                         GAZEBO SIM                          |
|  - Simulates 3D physical arena & robot dynamics             |
|  - Listens to:    /cmd_vel (Drives robot wheels)            |
|  - Publishes:     /scan (sensor_msgs/LaserScan)             |
|                   /camera/image_raw (sensor_msgs/Image)     |
|                   /odom (nav_msgs/Odometry)                 |
+-------------------------------------------------------------+
                                │
                                ▼  ROS 2 Middleware Topics
+-------------------------------------------------------------+
|                            RVIZ2                            |
|  - Fixed Frame:   odom                                      |
|  - RobotModel:    Renders 3D chassis & rotating wheels      |
|  - LaserScan:     Displays 360° laser reflection points     |
|  - Image:         Displays live front camera view           |
|  - TF Display:    Visualizes coordinate axes in real time   |
+-------------------------------------------------------------+
```

---

## 2. Teleoperation: Driving with `/cmd_vel`

You can manually drive the simulated robot using the standard keyboard teleoperation tool:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Use `i` (forward), `,` (backward), `j` (turn left), `l` (turn right), and `k` (stop).

---

## 3. Inspecting the Computational Graph with `rqt_graph`

To verify which nodes are actively communicating:
```bash
ros2 run rqt_graph rqt_graph
```
You will see `teleop_twist_keyboard` connected to `gazebo`, and `gazebo` broadcasting `/scan`, `/camera/image_raw`, and `/tf` to `rviz2`.

---

## ⚠️ Top 3 AI Hallucination Traps for Week 4

When asking AI (ChatGPT/Claude) for simulation launch files and RViz configs, watch out for these 3 common hallucinations:

1. **RViz Fixed Frame Disconnection**: AI frequently forgets to specify the `Fixed Frame` in RViz launch instructions or sets it to an unbroadcasted frame (e.g. `map` when no SLAM node is running). If Fixed Frame is wrong, RViz displays a global status error `Transform [sender] to [fixed_frame] does not exist` and sensor displays turn red. Always set Fixed Frame to `odom` or `base_link`.
2. **Sensor QoS Mismatch Silence**: High-frequency Gazebo sensor plugins publish using `BestEffort` (UDP-style) QoS. If an AI generates a Python subscriber using default `Reliable` QoS, ROS 2 will silently refuse to pass messages. Always configure sensor subscribers with `rclpy.qos.qos_profile_sensor_data`.
3. **Ghost Node Namespace Conflicts**: AI often adds random namespaces like `/my_robot/` to plugins but forgets to apply them to teleop or RViz. As a result, the robot listens on `/my_robot/cmd_vel` while teleop publishes to `/cmd_vel`, leaving the robot completely unresponsive.
