# Week 3: Kinematics, URDF/Xacro 3D Modeling & TF2 Coordinate Frames

In Weeks 1 & 2, you mastered the computational layer. Now we enter **3D spatial robotics**: Where is the vehicle in the world? Where is the camera mounted relative to the front axle? How does the vehicle move through space?

---

## 1. Coordinate Frames & ROS REP-105 Standard

Every autonomous robot must adhere to the **REP-105 coordinate standard**. If coordinate frames are inverted or disconnected, SLAM, Nav2, and perception will fail completely.

```
       map (Global World Frame - SLAM / GPS)
        │
        ▼ (Dynamic transform: corrected by SLAM / RTAB-Map)
       odom (Smooth Local Odometry Frame - Continuous, no jumps)
        │
        ▼ (Dynamic transform: published by wheel encoders + IMU / EKF)
    base_link (Center of vehicle chassis / Kinematic center)
        │
   ┌────┴───────────────────────────┬───────────────────────────┐
   ▼                                ▼                           ▼
left_wheel_link               right_wheel_link              camera_link
(Continuous joint)            (Continuous joint)                 │
                                                                 ▼
                                                    camera_optical_frame
                                                 (Z forward, X right, Y down)
```

### Critical Rules:
1. **Never Duplicate TF Publishers**: Each frame in the tree can only have **one parent**.
2. **Optical vs Body Frames**: Cameras use the optical standard ($Z$ forward, $X$ right, $Y$ down), while mobile robots use standard body frames ($X$ forward, $Y$ left, $Z$ up).

---

## 2. URDF & Xacro: Modeling 3D Robots

* **URDF (Unified Robot Description Format)**: An XML file describing robot links (bodies) and joints (connections).
* **Xacro (XML Macros)**: Adds variables, mathematical formulas, and reusable components to URDF so you don't copy-paste XML blocks.

### The Three Pillars of a `<link>`:
```xml
<link name="chassis">
  <!-- 1. Visual: How it looks in RViz/Gazebo (colors, CAD meshes) -->
  <visual>
    <geometry>
      <box size="0.6 0.4 0.2"/>
    </geometry>
    <material name="apex_orange">
      <color rgba="1.0 0.4 0.0 1.0"/>
    </material>
  </visual>

  <!-- 2. Collision: Simplified geometry used by physics engines for collision detection -->
  <collision>
    <geometry>
      <box size="0.6 0.4 0.2"/>
    </geometry>
  </collision>

  <!-- 3. Inertial: Mass and moments of inertia (required for physics simulation) -->
  <inertial>
    <mass value="15.0"/>
    <inertia ixx="0.25" ixy="0.0" ixz="0.0" iyy="0.45" iyz="0.0" izz="0.65"/>
  </inertial>
</link>
```

---

## 3. Dynamic vs Static Transforms in TF2

* **Static Transforms**: Relationships that never move (e.g., `base_link ➔ lidar_link` or `base_link ➔ camera_link`). Broadcasted once by `tf2_ros.StaticTransformBroadcaster`.
* **Dynamic Transforms**: Relationships that change continuously as the vehicle moves (e.g., `odom ➔ base_link`). Broadcasted at 20–50 Hz by `tf2_ros.TransformBroadcaster`.

---

## 4. Visualizing in RViz2

RViz (ROS Visualization) allows you to inspect sensor rays, transforms, point clouds, and robot models in real-time.

```bash
# Sourcing and launching RViz display
ros2 launch apex_robot_description display_rviz.launch.py
```
Inside RViz:
1. Set **Fixed Frame** to `odom` or `base_link`.
2. Add the **RobotModel** display.
3. Add the **TF** display to inspect frame axes (Red = X, Green = Y, Blue = Z).
