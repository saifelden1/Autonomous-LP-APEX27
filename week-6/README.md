# Week 6: State Estimation, Path Planning & Pure Pursuit (Capstone)

Welcome to the **Capstone Week**! You now combine state estimation, kinematics, and control into a complete closed-loop autonomous driving system.

---

## 1. The Autonomous Navigation Stack Architecture

```
+---------------------------------------------------------------------------------+
|                                 SENSING & ESTIMATION                            |
|                                                                                 |
|   [ Wheel Encoders ] ──> /wheel/odom                                            |
|                                     \                                           |
|                                      ───> [ robot_localization EKF ]            |
|                                     /     publishes: /odometry/filtered         |
|   [ 6-DoF IMU ]      ──> /imu/data                                              |
+---------------------------------------------------------------------------------+
                                         │
                                         ▼
+---------------------------------------------------------------------------------+
|                                 GLOBAL PLANNING                                 |
|                                                                                 |
|   [ Target Waypoints ] ──> [ Path Planner Node ]                                |
|                            publishes: /plan (nav_msgs/msg/Path)                 |
+---------------------------------------------------------------------------------+
                                         │
                                         ▼
+---------------------------------------------------------------------------------+
|                             LOCAL PATH TRACKING                                 |
|                                                                                 |
|   [ Pure Pursuit Controller Node ]                                              |
|   - Inputs:  /plan + /odometry/filtered                                         |
|   - Compute: Lookahead target, curvature kappa = 2*sin(alpha)/Ld                |
|   - Output:  /cmd_vel (geometry_msgs/msg/Twist)                                 |
+---------------------------------------------------------------------------------+
                                         │
                                         ▼
+---------------------------------------------------------------------------------+
|                            VEHICLE MOTOR CONTROLLER                             |
|                            (Gazebo Sim / Physical Rover)                        |
+---------------------------------------------------------------------------------+
```

---

## 2. Sensor Fusion with Extended Kalman Filter (EKF)

Why can't we just rely on wheel encoders?
* In Formula AI: High acceleration and braking causes wheel slip.
* In ERC Mars Yard: Sandy terrain and rocks cause severe slip.

An EKF (implemented in ROS 2 via `robot_localization`) fuses:
* High-frequency angular velocity from the **IMU** ($\omega_z$).
* Linear velocity from **wheel odometry** ($v_x$).
* Outputs smooth, drift-resistant `/odometry/filtered`.

---

## 3. The Pure Pursuit Tracking Algorithm

Pure Pursuit is the golden standard geometric path-tracking algorithm used across Formula Student Driverless and robotics.

```
                  Target Waypoint (gx, gy)
                         ●
                        /│
                       / │
           Lookahead  /  │
             L_d     /   │
                    /    │
                   / α   │
      Rover (x, y)▲──────┘
         (heading)
```

### Pure Pursuit Mathematics:
1. Find the path waypoint that is at distance $L_d$ (lookahead distance) ahead of the vehicle.
2. Calculate heading error $\alpha$ between vehicle orientation and the vector to the target point:
   $$\alpha = \text{atan2}(g_y - y, g_x - x) - \theta$$
3. Calculate circular arc curvature $\kappa$:
   $$\kappa = \frac{2 \sin(\alpha)}{L_d}$$
4. Calculate angular velocity command:
   $$\omega = v \cdot \kappa$$
5. Publish velocity:
   $$\text{linear.x} = v, \quad \text{angular.z} = \omega$$

If the vehicle drifts off the path, Pure Pursuit automatically steers harder to pull it back onto the line.
