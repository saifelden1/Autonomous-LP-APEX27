# Week 3: Gazebo Simulation, Sensor Physics & World Creation

Welcome to Week 3! Now that we have a 3D robot model, we step into **Physics Simulation**. In this module, you learn how simulated worlds are built and how physical sensors are modeled.

---

## 1. What is Gazebo?

While RViz only renders what ROS 2 tells it to display, **Gazebo** is a real-world physics engine:
* It simulates **mass, gravity, momentum, and friction**.
* It simulates **collisions** between solid objects.
* It simulates **photons and lasers** bouncing off obstacles to generate realistic sensor streams.

---

## 2. Robotics Sensor Types Explained

Autonomous vehicles rely on a suite of complementary sensors:

| Sensor Type | Physical Working Principle | Formula AI & ERC Relevance | ROS 2 Message Type |
| :--- | :--- | :--- | :--- |
| **2D LiDAR** | Emits rotating laser pulses; measures time-of-flight distance. | Fast 360° obstacle detection and 2D track boundary scanning. | `sensor_msgs/msg/LaserScan` |
| **RGB Camera** | Collects light through lenses onto a CMOS sensor grid. | Color cone detection (Yellow/Blue) and ArUco marker tracking. | `sensor_msgs/msg/Image` |
| **IMU (Inertial Unit)** | Micro-electromechanical (MEMS) gyroscopes & accelerometers. | High-frequency angular yaw rate and vehicle acceleration. | `sensor_msgs/msg/Imu` |
| **Wheel Encoders** | Hall-effect sensors counting wheel shaft rotations. | Dead-reckoning odometry velocity calculation. | `nav_msgs/msg/Odometry` |

---

## 3. Creating a Custom Gazebo World (`.world`)

A Gazebo world is defined in an XML-based **SDF (Simulation Description Format)** file. A minimal world requires:
1. Physics engine settings (`<physics>`).
2. A ground plane (`<include><uri>model://ground_plane</uri></include>`).
3. Sunlight illumination (`<include><uri>model://sun</uri></include>`).
4. Custom arena walls and obstacles (`<model name="wall_1">`).

---

## ⚠️ Top 3 AI Hallucination Traps for Week 3

When asking AI (ChatGPT/Claude) for Gazebo worlds and plugins, watch out for these 3 common hallucinations:

1. **Deprecated Gazebo Classic vs Gazebo Sim Tags**: AI constantly confuses Gazebo Classic (plugins ending in `.so`, like `libgazebo_ros_ray_sensor.so`) with modern Ignition/Gz Sim (using system plugins `<plugin filename="ignition-gazebo-sensors-system">`). Using the wrong syntax causes Gazebo to ignore the plugin completely without any error message!
2. **Missing SDF Sunlight & Ground**: When asked to generate a `.world` file, AI frequently forgets the `<include><uri>model://sun</uri></include>` and `<include><uri>model://ground_plane</uri></include>` tags. The result is a completely pitch-black screen where spawned robots fall into an infinite abyss.
3. **Massless Links in Physics Simulation**: In RViz, links do not need mass. In Gazebo, any link connected via a non-fixed joint or equipped with collision geometry must have a positive `<mass>` and valid moments of inertia. If mass is zero, Gazebo will crash on startup with a physics solver division-by-zero error.
