# Week 6 Task: Autonomous Navigation & Path Tracking Exposure

## 🎯 Objective
Gain practical exposure to autonomous navigation: run a Pure Pursuit path follower in simulation, observe how it computes curvature from `/plan` and `/odom` to drive the vehicle autonomously along a course, and inspect the topic contracts.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Launch Autonomous Navigation
```bash
ros2 launch apex_navigation capstone_autonomous_nav.launch.py
```
*Starts the reference path publisher and the Pure Pursuit controller.*

### Step 3: Inspect Real-Time Output
In a second terminal:
```bash
# Monitor the velocity commands driving the vehicle
ros2 topic echo /cmd_vel
```
*Notice how angular.z continuously adjusts left and right to keep the vehicle locked on the path.*

---

## ✅ Pass / Fail Verification Deliverable

Submit a screenshot showing:
1. Terminal output showing `ros2 topic echo /cmd_vel` outputting continuous velocity commands.
2. Terminal output showing the path publisher and controller running cleanly without errors.
