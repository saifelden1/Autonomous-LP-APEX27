# Week 3 Project: 4-Wheel Autonomous Chassis in RViz & Dynamic TF2 Broadcaster

## 🎯 Objective
In this project, you will build a complete 3D robot model from scratch and broadcast dynamic coordinate frames:
1. `apex_robot_description`: An `ament_python` package containing:
   * `urdf/apex_chassis.urdf.xacro`: Complete vehicle model with 4 wheels (front left, front right, rear left, rear right), sensor mount mast, LiDAR link, and camera link.
   * `apex_robot_description/odom_tf_broadcaster.py`: A Python node that calculates circular odometry and broadcasts dynamic `odom ➔ base_link` transforms using TF2.
   * `launch/display_rviz.launch.py`: A launch file that parses Xacro, starts `robot_state_publisher`, the dynamic TF broadcaster, and loads RViz2 pre-configured.

---

## 📐 Required TF2 Coordinate Tree

When your launch file is running, running `ros2 run tf2_tools view_frames` must generate a PDF diagram matching this structure:

```
odom (Fixed World Origin)
 └── base_link (Robot Kinematic Origin)
      ├── chassis (Physical vehicle body)
      │    ├── front_left_wheel (continuous joint)
      │    ├── front_right_wheel (continuous joint)
      │    ├── rear_left_wheel (continuous joint)
      │    └── rear_right_wheel (continuous joint)
      ├── lidar_link (mounted 0.3m above chassis)
      └── camera_link (mounted at front bumper)
           └── camera_optical_frame (Z forward optical orientation)
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Complete the Xacro Model
* File: `apex_robot_description/urdf/apex_chassis.urdf.xacro`
* Verify properties:
  * Wheel radius: `0.1` m, width: `0.05` m
  * Chassis length: `0.6` m, width: `0.4` m, height: `0.15` m
  * Lidar link located at $(x=0.15, y=0.0, z=0.25)$ relative to `base_link`.
  * Camera link located at front $(x=0.30, y=0.0, z=0.10)$.

### Step 2: Implement Dynamic TF2 Broadcaster
* File: `apex_robot_description/apex_robot_description/odom_tf_broadcaster.py`
* Node name: `odom_tf_broadcaster_node`
* Publish rate: `30` Hz
* Trajectory math:
  * Simulate circular trajectory of radius $R = 1.5$ m at angular velocity $\omega = 0.5$ rad/s:
    * $x(t) = R \cdot \cos(\omega \cdot t) - R$
    * $y(t) = R \cdot \sin(\omega \cdot t)$
    * $\theta(t) = \omega \cdot t + \frac{\pi}{2}$
  * Compute quaternion: $q_z = \sin(\theta / 2)$, $q_w = \cos(\theta / 2)$, $q_x = 0$, $q_y = 0$.
  * Broadcast `TransformStamped` from `odom` to `base_link`.

### Step 3: Configure Launch File
* File: `apex_robot_description/launch/display_rviz.launch.py`
* Must parse Xacro using `Command(['xacro ', xacro_file])` and pass to `robot_state_publisher`.
* Launch RViz2 and `odom_tf_broadcaster`.

---

## ✅ Pass / Fail Verification Checklist

Launch the complete display pipeline:
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch apex_robot_description display_rviz.launch.py
```

### Verification Criteria:
1. RViz opens without any red frame errors.
2. In RViz, with **Fixed Frame** set to `odom`, you can see the 4-wheeled robot smoothly driving in a continuous circle!
3. Run the frame verification command in a second terminal:
   ```bash
   ros2 run tf2_ros tf2_echo odom base_link
   ```
   Terminal output shows continuously updating translation $(x, y)$ and rotation.
4. Run TF frames tool:
   ```bash
   ros2 run tf2_tools view_frames
   ```
   Verify `frames.pdf` shows a single connected tree rooted at `odom`.

Record a 30-to-60 second video showing the moving vehicle in RViz alongside the `tf2_echo` terminal!
