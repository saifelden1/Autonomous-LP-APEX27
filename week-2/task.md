# Week 2 Task: 4-Wheel Robot Model & RViz TF Inspection

## 🎯 Objective
Assemble a 4-wheeled autonomous vehicle model in URDF/Xacro and inspect its links, joints, and TF tree visually in RViz2 using `joint_state_publisher_gui`.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
```

### Step 2: Review Robot Model
Open `src/apex_robot_description/urdf/apex_chassis.urdf.xacro`. Verify the model includes:
* `chassis` link (main body).
* 4 wheels (front-left, front-right, rear-left, rear-right) connected with continuous joints.
* `lidar_link` mounted on top.
* `camera_link` mounted on front bumper.

### Step 3: Build and Launch
```bash
colcon build --symlink-install
source install/setup.bash
ros2 launch apex_robot_description display_rviz.launch.py
```

### Step 4: Interact & Verify
1. RViz2 opens displaying the 3D vehicle model with red/green/blue coordinate frame axes.
2. The `joint_state_publisher_gui` window opens with sliders for the 4 wheel joints. Move the sliders and observe the wheels rotate in RViz.
3. In a second terminal, generate the TF tree diagram:
   ```bash
   ros2 run tf2_tools view_frames
   ```

---

## ✅ Pass / Fail Verification Deliverable

Submit a screenshot showing:
1. RViz2 displaying the 4-wheeled robot with wheel frames visible.
2. The `joint_state_publisher_gui` window side-by-side with RViz.
