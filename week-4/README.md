# Week 4: Gazebo Simulation, Sensor Plugins & Closed-Loop Control

In Week 3, you saw your vehicle in RViz. However, RViz is merely a visualizer—it has no gravity, no wheel friction, no inertia, and no collisions. 

This week, we bridge our robot into **Gazebo**, a realistic 3D rigid-body physics simulator.

---

## 1. RViz vs Gazebo: The Fundamental Difference

| Feature | RViz2 | Gazebo Sim |
| :--- | :--- | :--- |
| **Role** | **Visualization tool** (What the robot thinks it sees) | **World simulator** (The ground truth physical world) |
| **Physics** | None (Visual only) | Rigid-body dynamics, mass, friction, gravity |
| **Sensors** | Displays received sensor topics | Simulates photons, laser reflections, noise, and IMU drift |
| **Actuation** | Cannot drive unless TF is broadcasted | Drives wheels when torque / velocity commands arrive |

---

## 2. Gazebo Plugins: Bringing Hardware to Life

To make Gazebo talk to ROS 2, we attach `<gazebo>` plugin tags inside our Xacro model.

### 1. Differential / Skid-Steer Drive Plugin
Simulates the wheel motors and listens to `/cmd_vel` (`geometry_msgs/msg/Twist`):
```xml
<gazebo>
  <plugin name="diff_drive" filename="libgazebo_ros_diff_drive.so">
    <ros>
      <namespace>/</namespace>
      <remapping>cmd_vel:=cmd_vel</remapping>
      <remapping>odom:=wheel/odom</remapping>
    </ros>
    <left_joint>rear_left_wheel_joint</left_joint>
    <right_joint>rear_right_wheel_joint</right_joint>
    <wheel_separation>0.46</wheel_separation>
    <wheel_diameter>0.20</wheel_diameter>
    <publish_odom>true</publish_odom>
    <publish_odom_tf>false</publish_odom_tf> <!-- Handled by EKF in real rovers! -->
  </plugin>
</gazebo>
```

### 2. 2D LiDAR Ray Sensor Plugin
Simulates a rotating laser scanner and publishes `sensor_msgs/msg/LaserScan` on `/scan`:
```xml
<gazebo reference="lidar_link">
  <sensor name="lidar" type="ray">
    <always_on>true</always_on>
    <update_rate>10.0</update_rate>
    <ray>
      <scan>
        <horizontal>
          <samples>360</samples>
          <min_angle>-3.14159</min_angle>
          <max_angle>3.14159</max_angle>
        </horizontal>
      </scan>
      <range>
        <min>0.12</min>
        <max>10.0</max>
      </range>
    </ray>
    <plugin name="lidar_plugin" filename="libgazebo_ros_ray_sensor.so">
      <ros>
        <remapping>~/out:=scan</remapping>
      </ros>
      <output_type>sensor_msgs/LaserScan</output_type>
      <frame_name>lidar_link</frame_name>
    </plugin>
  </sensor>
</gazebo>
```

---

## 3. Dissecting `sensor_msgs/msg/LaserScan`

When `/scan` is received in Python:
* `msg.angle_min` and `msg.angle_max`: Angular coverage ($-\pi$ to $+\pi$).
* `msg.angle_increment`: Angular step between beam readings (e.g., $1^\circ \approx 0.0174$ rad).
* `msg.ranges`: An array of float distances in meters (index 0 corresponds to `angle_min`).

To inspect only the **front cone** ($\pm 30^\circ$):
```python
# Convert angle to array index
center_idx = len(msg.ranges) // 2
half_window = int(math.radians(30) / msg.angle_increment)
front_ranges = msg.ranges[center_idx - half_window : center_idx + half_window]
```
