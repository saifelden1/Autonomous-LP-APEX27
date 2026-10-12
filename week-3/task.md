# Week 3 Task: Custom Gazebo Arena & World Creation

## 🎯 Objective
Create a custom Gazebo simulation arena (`apex_arena.world`) with enclosing boundary walls and test obstacles, and launch it using a ROS 2 launch file.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
```

### Step 2: Inspect World File
Open `src/apex_gazebo_worlds/worlds/apex_arena.world`. Notice the structure:
* Physics time-step: 0.001s (1 kHz physics rate).
* Ground plane and sun light.
* 4 boundary walls defining a 10m x 10m test arena.
* Obstacle pillars placed inside the arena.

### Step 3: Build and Launch World
```bash
colcon build --symlink-install
source install/setup.bash
ros2 launch apex_gazebo_worlds world.launch.py
```

---

## ✅ Pass / Fail Verification Deliverable

Submit a screenshot showing the Gazebo simulation window running with the custom `apex_arena.world` loaded, showing the walls, ground plane, and obstacle blocks.
