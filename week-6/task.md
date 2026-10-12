# Week 6 Capstone Project: Autonomous Waypoint & Slalom Challenge

## 🎯 Objective
In this Capstone challenge, you will implement a **Pure Pursuit Path Tracker** and deploy it to guide the simulated APEX vehicle through a complete multi-waypoint course autonomously.

Package: `apex_navigation`
Nodes:
1. `path_publisher`: Publishes a smooth S-curve track (`nav_msgs/msg/Path`) on `/plan`.
2. `pure_pursuit_controller`:
   * Subscribes to `/plan` and `/odometry/filtered` (or Gazebo `/odom`).
   * Computes the lookahead goal point $(g_x, g_y)$ at distance $L_d$.
   * Computes curvature $\kappa$ and outputs driving commands on `/cmd_vel`.
   * Automatically stops the robot when the end of the path is reached.
3. Launch file: `capstone_autonomous_nav.launch.py` starting the robot in Gazebo, the path visualizer, and the controller.

---

## 📐 System Pipeline

```
+------------------------------------+
|           path_publisher           |
|  publishes: /plan (nav_msgs/Path)  |
+------------------------------------+
                  │
                  ▼
+------------------------------------+
|      pure_pursuit_controller       |
|  - Inputs: /plan & /wheel/odom     |
|  - Math:   kappa = 2*sin(alpha)/Ld |
|  - Output: /cmd_vel                |
+------------------------------------+
                  │
                  ▼
+------------------------------------+
|       Gazebo Robot Simulation      |
|  Vehicle autonomously steers &     |
|  completes the course!             |
+------------------------------------+
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Inspect the Navigation Package
Navigate to `week-6/template_ws`:
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Implement `pure_pursuit_controller.py`
* File: `apex_navigation/apex_navigation/pure_pursuit_controller.py`
* Parameters:
  * `lookahead_distance`: default `1.0` meters
  * `target_velocity`: default `0.8` m/s
  * `goal_tolerance`: default `0.3` meters
* Subscriptions:
  * `/plan` (`nav_msgs/msg/Path`)
  * `/wheel/odom` (`nav_msgs/msg/Odometry`)
* Publication:
  * `/cmd_vel` (`geometry_msgs/msg/Twist`)
* Core Logic:
  1. Extract current $(x, y, \theta)$ from odometry.
  2. Find the target waypoint on the path at distance $L_d \ge 1.0\text{m}$.
  3. Calculate heading angle: $\alpha = \text{atan2}(g_y - y, g_x - x) - \theta$.
  4. Normalize $\alpha$ to $[-\pi, \pi]$ using `math.atan2(math.sin(alpha), math.cos(alpha))`.
  5. Calculate angular velocity: $\omega = \frac{2 \cdot v \cdot \sin(\alpha)}{L_d}$.
  6. When distance to the final path point $< 0.3$m, publish zero velocity and log: `CAPSTONE COMPLETE! Target reached.`

### Step 3: Run the Capstone
```bash
ros2 launch apex_navigation capstone_autonomous_nav.launch.py
```

---

## ✅ Pass / Fail Verification Checklist

Launch the capstone simulation:
```bash
source install/setup.bash
ros2 launch apex_navigation capstone_autonomous_nav.launch.py
```

### Verification Criteria:
1. The robot starts at origin $(0, 0)$.
2. RViz displays the green path trajectory winding through the terrain.
3. The robot begins driving autonomously, following the curves of the path with smooth steering.
4. The cross-track error (distance between vehicle center and path) never exceeds 0.4 meters.
5. The robot stops smoothly at the final waypoint and prints `CAPSTONE COMPLETE!`.

Record a full 60-second video of the rover completing the course in RViz and Gazebo for your final PR!
