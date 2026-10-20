# Week 2: Robot Modeling (URDF/Xacro), TF Tree & RViz Visualization

Welcome to Week 2! This week is all about **robot geometry and coordinate frames**. You will learn how to describe physical robots in code and inspect them visually in RViz.

---

## 1. What is URDF & Xacro?

* **URDF (Unified Robot Description Format)**: An XML standard describing rigid bodies (**Links**) and the mechanical pivots connecting them (**Joints**).
* **Xacro (XML Macros)**: Adds variables, math, and reusable templates to URDF so you don't repeat XML blocks.

```
+-----------------------------------------------------------+
|                          chassis                          |
|                     (Root Body Link)                      |
+-----------------------------------------------------------+
        │                                           │
  (Continuous Joint)                          (Continuous Joint)
        │                                           │
        ▼                                           ▼
+-----------------------+                   +-----------------------+
|  front_left_wheel     |                   |  front_right_wheel    |
+-----------------------+                   +-----------------------+
```

### Key Elements of a `<link>`:
1. `<visual>`: Shape, dimensions, and colors for rendering in RViz.
2. `<collision>`: Simplified bounding shapes used by physics simulators for collision checks.
3. `<inertial>`: Mass and moments of inertia.

---

## 2. The TF2 Coordinate Tree & REP-105 Standard

Every sensor and wheel has its own coordinate frame. The **TF2 library** keeps track of where each frame is relative to `base_link` (the center of the vehicle):

```
base_link (Center of vehicle)
 ├── chassis
 ├── front_left_wheel
 ├── front_right_wheel
 ├── lidar_link
 └── camera_link
```

Tools to inspect frames:
```bash
# View live coordinates between two frames
ros2 run tf2_ros tf2_echo base_link lidar_link

# Generate a visual PDF map of the whole tree
ros2 run tf2_tools view_frames
```

---

## 3. Visualizing in RViz2 with GUI Controls

We use two standard nodes to display the robot:
* `robot_state_publisher`: Reads the URDF XML and broadcasts the 3D transforms.
* `joint_state_publisher_gui`: A GUI window with slider bars that let you manually turn the wheels to test joint movement.

---

## 4. Curated Open-Source Video Resources

* **Coordinate Frames in ROS 2**: [Coordinate Frame Basics and Right Hand Rule (Automatic Addison)](https://youtu.be/oxr8df96tWk)
* **Mobile Robot Modeling with URDF**: [Create and Visualize a Mobile Robot with URDF (Automatic Addison)](https://youtu.be/XtS8mCcffrs)
* **URDF Launch Files**: [Create Launch Files to Display URDF Files (Automatic Addison)](https://youtu.be/2ri0Ouc67W0)
* **RViz Robot Parameters**: [Customize Your Robot with Parameters in RViz (Automatic Addison)](https://youtu.be/AkekfmNAUkk)
* **Full Robotics Series Playlist**: [Automatic Addison ROS 2 Series](https://www.youtube.com/playlist?list=PLNWNEEf8BvG64FVZT4IdieI1PuYnHkUrt)

---

## ⚠️ Top 3 AI Hallucination Traps for Week 2

When asking AI (ChatGPT/Claude) for URDF and TF code, watch out for these 3 common hallucinations:

1. **Swapping Parent and Child Frames**: AI frequently swaps `<parent>` and `<child>` tags inside joints (e.g. setting `camera_link` as the parent of `chassis`). This breaks the tree hierarchy because each link can only have **one** parent.
2. **The Cylinder Orientation Bug**: In URDF, cylinders are aligned along the **Z-axis** by default. To make a cylinder function as a vehicle wheel spinning along the Y-axis, an explicit roll rotation `<origin rpy="1.5708 0 0"/>` is required. AI frequently forgets this, creating wheels that slide on their flat faces!
3. **Invalid Zero Quaternions**: When generating orientation code, AI sometimes defaults quaternion orientation to `(x=0, y=0, z=0, w=0)`. A valid quaternion must always be normalized to length 1.0 (an identity quaternion is `w=1.0, x=0, y=0, z=0`). A zero quaternion will crash RViz transform processing.

---

## 📋 Week 2 Assignment & Deliverables

Follow the step-by-step instructions in [task.md](task.md) and record your results in [Template_Report.md](Template_Report.md) for your Saturday PR submission.
