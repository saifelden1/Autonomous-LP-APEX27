# Week 4 Task: Rover Deployment, RViz Sensor Stream & rqt_graph

## 🎯 Objective
Deploy the 4-wheel robot model into the custom Gazebo simulation arena, drive it with teleoperation, visualize live laser scans and camera feeds in RViz2, and capture the active architecture in `rqt_graph`.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Launch Gazebo & RViz Together
```bash
ros2 launch apex_simulation spawn_and_rviz.launch.py
```
*Both Gazebo (with the robot inside the arena) and RViz2 will launch simultaneously.*

### Step 3: Drive the Robot via Teleop
In a second terminal:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
Drive the vehicle toward an arena wall using keys `i`, `j`, `l`.

### Step 4: Verify Live Sensor Displays in RViz
* In RViz2, set **Fixed Frame** to `odom`.
* Add a **LaserScan** display subscribed to topic `/scan` (Set size to 0.05). Notice the laser reflection points hit the arena walls as you drive!
* Add an **Image** display subscribed to `/camera/image_raw`.

### Step 5: Inspect Graph
In a third terminal:
```bash
ros2 run rqt_graph rqt_graph
```

---

## ✅ Pass / Fail Verification Deliverable

Submit two screenshots (or a 30-second screen capture):
1. **Side-by-Side View**: Gazebo window showing the robot driving next to the RViz window showing live `/scan` laser points reflecting off the walls.
2. **`rqt_graph` View**: Window showing the active communication nodes and topic connections.
