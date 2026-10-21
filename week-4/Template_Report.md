# Week 4 Documentation & Simulation Bridge Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-4-simulation-rviz-bridge]  

---

## 1. Simulation Pipeline & Topic Specifications

| Subsystem | Topic Name | Message Interface Type | Publishing Node | Subscribing Node |
| :--- | :--- | :--- | :--- | :--- |
| **Teleoperation** | `/cmd_vel` | `geometry_msgs/msg/Twist` | `teleop_twist_keyboard` | `gazebo` (diff_drive) |
| **LaserScan** | `/scan` | `sensor_msgs/msg/LaserScan` | `gazebo` (ray_sensor) | `rviz2` |
| **Camera View** | `/camera/image_raw` | `sensor_msgs/msg/Image` | `gazebo` (camera_sensor)| `rviz2` |
| **Odometry** | `/odom` | `nav_msgs/msg/Odometry` | `gazebo` (diff_drive) | `rviz2` / TF Broadcaster |

---

## 2. Verification Screenshots & Graph Evidence

### 2.1 Side-by-Side Driving & LaserScan Screenshot
Embed or link your screenshot showing the rover moving in Gazebo while RViz displays live `/scan` laser reflections:
`![Week 4 Driving Verification](gazebo_rviz_driving.png)`

### 2.2 Rqt_Graph Pipeline Verification
Embed or link your `rqt_graph` diagram showing all connected nodes:
`![Week 4 rqt_graph](rqt_graph_simulation.png)`

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: RViz showed transform error for LaserScan* | *Fixed Frame was set to map instead of odom* | *Changed RViz Global Options Fixed Frame to odom* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **Why does RViz report `Transform does not exist` if the Fixed Frame is set to `map` during this lab? What node is responsible for creating the `map` frame?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **What is the difference between `/cmd_vel` linear velocity ($x$) and angular velocity ($z$), and how do they map to individual wheel speeds on a differential drive chassis?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **In autonomous racing (Formula AI) and rover planetary exploration, why do engineers use RViz to inspect sensor data streams rather than looking solely at the Gazebo 3D camera view?**  
   [Write a 2-3 sentence explanation to practice your defense]
