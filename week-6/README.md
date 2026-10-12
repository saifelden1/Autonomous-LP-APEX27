# Week 6: Path Planning & Control Fundamentals (Theoretical & Practical Exposure)

Welcome to Week 6! In this final module, you explore the brains of autonomous movement: **Path Planning and Motion Control**.

---

## 1. The Autonomous Navigation Stack (Nav2) Architecture

Once a vehicle knows where it is on a map (via SLAM), it needs to safely navigate from Point A to Point B:

```
                  Goal Pose (/goal_pose)
                           │
                           ▼
+─────────────────────────────────────────────────────────────+
|                       GLOBAL PLANNER                        |
|  - Uses Global Costmap (Static /map + inflated obstacles)   |
|  - Algorithm: A*, Dijkstra, or Smac Hybrid A*               |
|  - Output: /plan (nav_msgs/msg/Path)                        |
+─────────────────────────────────────────────────────────────+
                           │
                           ▼
+─────────────────────────────────────────────────────────────+
|                      LOCAL CONTROLLER                       |
|  - Uses Local Costmap (Rolling sensor window around robot)  |
|  - Algorithm: Pure Pursuit, DWA, or MPPI                    |
|  - Follows the global path while dodging dynamic obstacles  |
|  - Output: /cmd_vel (geometry_msgs/msg/Twist)               |
+─────────────────────────────────────────────────────────────+
                           │
                           ▼
+─────────────────────────────────────────────────────────────+
|                       VEHICLE MOTORS                        |
|  - Gazebo Simulation / Physical Motor Controllers           |
+─────────────────────────────────────────────────────────────+
```

---

## 2. Global Planning vs Local Control: Key Differences

| Feature | Global Planner | Local Controller |
| :--- | :--- | :--- |
| **Role** | Long-term macro route | Short-term reactive steering |
| **Map Used** | Entire world map (`/map`) | Real-time 3-meter sensor window |
| **Update Rate** | 1 Hz to 5 Hz | 20 Hz to 50 Hz |
| **Typical Algorithms** | A*, Dijkstra, Smac Hybrid A* | Pure Pursuit, MPPI, TEB, DWA |
| **Output** | `nav_msgs/msg/Path` (List of waypoints) | `geometry_msgs/msg/Twist` (`/cmd_vel`) |

---

## 3. Pure Pursuit Path Tracking: The Geometric Core

Pure Pursuit is the standard path tracking algorithm used in mobile robotics and Formula Student:
1. Find a target point on the path at lookahead distance $L_d$ ahead of the vehicle.
2. Calculate heading error $\alpha$ to the target point.
3. Compute circular steering curvature: $\kappa = \frac{2 \sin(\alpha)}{L_d}$.
4. Command linear velocity $v$ and steering angular rate $\omega = v \cdot \kappa$.

---

## 4. Hardware Actuators, Sensors & Topic Contracts

```
INPUT SENSORS & GOALS:
├── /map                (nav_msgs/OccupancyGrid)   - Global environmental map
├── /odom               (nav_msgs/Odometry)        - Robot position & velocity
├── /scan               (sensor_msgs/LaserScan)    - Obstacle proximity
└── /goal_pose          (geometry_msgs/PoseStamped)- Requested navigation target

INTERMEDIATE TRAJECTORY:
└── /plan               (nav_msgs/Path)            - Planned sequence of waypoints

OUTPUT ACTUATION:
└── /cmd_vel            (geometry_msgs/Twist)      - Commanded linear & angular velocity
```

---

## ⚠️ Top 3 AI Hallucination Traps for Week 6

When asking AI (ChatGPT/Claude) for navigation and control code, watch out for these 3 common hallucinations:

1. **Unbounded Angular Velocity Spin**: AI frequently writes Pure Pursuit formulas without bounding `cmd.angular.z`. If the robot starts at a sharp angle to the path, the calculated curvature explodes, causing the vehicle to spin violently in place. Always clamp angular velocity (e.g. `cmd.angular.z = max(min(w, 1.5), -1.5)`).
2. **Angle Discontinuity Bug ($\pm\pi$ wrap)**: When calculating heading error $\alpha = \text{target\_angle} - \text{vehicle\_yaw}$, AI often forgets to normalize $\alpha$ into $[-\pi, \pi]$. When crossing the boundary between $+180^\circ$ and $-180^\circ$, the raw difference jumps to $\approx 360^\circ$, causing the vehicle to jerk suddenly in the wrong direction.
3. **Costmap Inflation Radius Mismatch**: In Nav2 parameter configurations, AI often suggests setting `inflation_radius` smaller than the vehicle's physical collision radius. In simulation, the planner plots routes cutting tightly through corners, causing the wheels or bumper to scrape against walls.
