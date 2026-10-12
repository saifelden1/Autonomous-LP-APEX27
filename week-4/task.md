# Week 4 Project: Gazebo Arena Spawn & Automatic Laser Emergency Braking Node

## 🎯 Objective
In both Formula Student AI and ERC 27, autonomous vehicles are strictly required to have an active **Autonomous Emergency Braking (AEB)** system that prevents catastrophic collision with obstacles, barriers, or people.

In this project, you will:
1. Augment your vehicle Xacro with Gazebo plugins for **differential drive** and a **2D LiDAR scanner**.
2. Create `laser_emergency_brake`: A safety multiplexer node that listens to manual or autonomous velocity requests on `/teleop_cmd_vel` and scans the environment via `/scan`.
3. If an obstacle enters the critical front sector within `brake_distance` (default 0.75m), the node **overrides** the drive command, sends `linear.x = 0.0`, and engages the brake.
4. Launch Gazebo with a test obstacle box placed 3 meters in front of the vehicle, command it to drive full throttle forward, and verify the AEB prevents collision!

---

## 📐 System Data Flow

```
                      +-----------------------------+
                      |     teleop_twist_keyboard   |
                      |  publishes /teleop_cmd_vel  |
                      +-----------------------------+
                                     │
                                     ▼
+---------------------+     +-----------------------------+     +-------------------+
|     Gazebo Sim      |     |    laser_emergency_brake    |     |    Gazebo Sim     |
| publishes: /scan    |────>|  (Monitors front cone)       |────>| listens: /cmd_vel |
| (sensor_msgs/Laser) |     |  - If clear: pass-through   |     | (Robot drives/stops)
+---------------------+     |  - If close: FORCE ZERO VEL |     +-------------------+
                            +-----------------------------+
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Add Plugins to Robot Description
Open `apex_robot_description/urdf/apex_chassis.urdf.xacro` (or check `week-4/template_ws/src/apex_simulation/urdf/apex_sim_chassis.urdf.xacro`). Ensure:
* `libgazebo_ros_diff_drive.so` is bound to wheel joints.
* `libgazebo_ros_ray_sensor.so` publishes to topic `/scan`.

### Step 2: Implement `laser_emergency_brake.py`
* File: `apex_simulation/apex_simulation/laser_emergency_brake.py`
* Subscriptions:
  * `/scan` (`sensor_msgs/msg/LaserScan`)
  * `/teleop_cmd_vel` (`geometry_msgs/msg/Twist`)
* Publication:
  * `/cmd_vel` (`geometry_msgs/msg/Twist`)
* Parameter: `brake_distance` (default: `0.75` meters), `front_angle_deg` (default: `30.0` degrees).
* Logic:
  * In the scan callback, find the minimum range within $[-\text{front\_angle\_deg}, +\text{front\_angle\_deg}]$.
  * In the cmd_vel callback: If `min_front_range < brake_distance`, log warning and publish `Twist(linear.x=0, angular.z=0)`. Otherwise, forward incoming `teleop_cmd_vel`.

### Step 3: Launch Gazebo Simulation
* Launch file: `apex_simulation/launch/gazebo_sim.launch.py`.

---

## ✅ Pass / Fail Verification Checklist

Launch the simulation and safety node:
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch apex_simulation gazebo_sim.launch.py
```

In a second terminal, command the robot to drive directly forward toward the obstacle at 1.0 m/s:
```bash
ros2 topic pub /teleop_cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0, y: 0.0, z: 0.0}}"
```

### Verification Criteria:
1. The robot starts accelerating forward towards the wall/obstacle in Gazebo.
2. When the robot reaches 0.75m distance from the obstacle:
   * The terminal immediately prints: `[WARN]: OBSTACLE DETECTED AT X.XXm! EMERGENCY BRAKE ENGAGED!`
   * The vehicle comes to an immediate, complete stop before touching the obstacle.
   * Distance between bumper and wall never reaches 0.0m (zero collision).

Record a 30-to-60 second video showing the vehicle approaching the obstacle and stopping cleanly in Gazebo!
