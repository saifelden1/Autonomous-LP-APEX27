# Week 5: Perception & SLAM Fundamentals (Theoretical & Practical Exposure)

Welcome to Week 5! This module provides a fast, structured, and practical overview of **Perception & SLAM** (Simultaneous Localization And Mapping).

---

## 1. What is SLAM? (The Chicken-and-Egg Problem)

To navigate autonomously, a robot must answer two questions simultaneously:
1. *Where am I?* (**Localization**)
2. *What does the world look like?* (**Mapping**)

Without a map, the robot cannot localize; without knowing where it is, it cannot build a map. **SLAM algorithms** solve both in real-time.

```
+---------------------------------------------------------------------------------+
|                                 SLAM ALGORITHM                                  |
|                                                                                 |
|   Inputs:                                                                       |
|   - Sensor Scans:  /scan (LaserScan) or /camera/depth/points (PointCloud2)      |
|   - Odometry:      /odom (Wheel odometry + IMU)                                 |
|                                                                                 |
|   Outputs:                                                                      |
|   - 2D/3D Map:     /map (nav_msgs/OccupancyGrid)                                |
|   - Correction TF: map ➔ odom (Compensates for wheel drift)                     |
+---------------------------------------------------------------------------------+
```

---

## 2. SLAM Types: 2D LiDAR vs 3D Visual SLAM

| Method | Typical ROS 2 Package | Primary Sensors | Pros & Cons |
| :--- | :--- | :--- | :--- |
| **2D LiDAR SLAM** | `slam_toolbox`, `cartographer` | 2D LiDAR + Odometry | Fast, low compute, highly reliable on flat surfaces. Cannot see height obstacles. |
| **3D Visual / RGB-D SLAM** | `rtabmap_ros`, `orb_slam3` | Stereo / Depth Camera + IMU | Rich 3D maps and visual loop closure. High compute cost, sensitive to lighting changes. |

---

## 3. Perception: Feature Extraction in Competition

* **Formula Student AI Track**: High-speed track boundary detection:
  * Detects **Yellow cones** (right boundary) and **Blue cones** (left boundary) using HSV color segmentation or lightweight neural networks (YOLOv8-tiny).
  * Estimates 3D metric distances $(X, Y)$ relative to the car bumper.
* **ERC 27 Track**: Mars Yard landmark and hazard tracking:
  * Detects **ArUco fiducials** (4x4 matrix barcodes) for pinpoint target localization.
  * Clusters 3D terrain point clouds into traversable ground vs untraversable rocks.

---

## 4. Hardware Actuators, Sensors & ROS 2 Topic Contracts

```
SENSORS (Inputs):
├── /scan                    (sensor_msgs/LaserScan)       - 2D distance slices
├── /camera/color/image_raw  (sensor_msgs/Image)           - RGB pixel matrices
├── /camera/depth/points     (sensor_msgs/PointCloud2)   - 3D spatial coordinate points
├── /imu/data                (sensor_msgs/Imu)             - Angular velocity & acceleration
└── /odom                    (nav_msgs/Odometry)           - Wheel encoder dead-reckoning

ACTUATORS (Outputs):
└── /cmd_vel                 (geometry_msgs/Twist)         - Linear & angular velocity commands
```

---

## ⚠️ Top 3 AI Hallucination Traps for Week 5

When asking AI (ChatGPT/Claude) for SLAM and perception pipelines, watch out for these 3 common hallucinations:

1. **Duplicate `map ➔ odom` TF Broadcaster**: AI often suggests writing a custom TF node or static transform publisher for `map ➔ odom`. In any standard SLAM system, the `map ➔ odom` transform is dynamically computed and broadcasted **exclusively by the SLAM node** (`slam_toolbox` or `rtabmap`). Having a second publisher causes RViz to flicker uncontrollably between two competing world origins!
2. **Body vs Optical Camera Coordinate Inversion**: In ROS, robot bodies follow standard engineering coordinates ($X$ forward, $Y$ left, $Z$ up), but camera optical algorithms expect the optical standard ($Z$ forward, $X$ right, $Y$ down). If AI omits the optical frame transform joint, detected 3D objects and point clouds will appear sideways or upside down.
3. **Invalid Occupancy Grid Values**: When asked to create or manipulate `/map` messages in Python, AI often outputs integer values outside the valid range. In ROS 2, `nav_msgs/msg/OccupancyGrid` data must strictly be: `-1` (Unknown), `0` (Completely Free), or `1` to `100` (Probability of Obstacle). Using `255` or negative values other than `-1` results in completely invisible maps in RViz.
