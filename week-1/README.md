# Week 1: ROS 2 Architecture, Nodes, Pub/Sub & Launch Files

Welcome to Week 1! This week introduces the core building blocks of ROS 2 (Robot Operating System).

---

## 1. ROS 2 Computational Graph & Architecture

ROS 2 organizes software into independent processes called **Nodes** that communicate over a network layer called **DDS**:
* **Node**: A program that performs a single task (e.g., reading a sensor, controlling a steering motor).
* **Topic**: A named channel where data is published and subscribed to.
* **Message**: The data format sent over a topic (e.g. `std_msgs/msg/String`, `geometry_msgs/msg/Twist`).

```
+---------------------------+                      +---------------------------+
|    Publisher Node         |                      |    Subscriber Node        |
| (e.g. telemetry_publisher)|                      |  (e.g. telemetry_listener)|
|                           |                      |                           |
|   Timer Callback (10 Hz)  |                      |   Subscription Callback   |
|            │              |                      |             ▲             |
|            ▼              |                      |             │             |
|      publishes to         | ═════ Topic ═══════> |        listens on         |
|   /vehicle/telemetry      |                      |    /vehicle/telemetry     |
+---------------------------+                      +---------------------------+
```

---

## 2. Compiling with Colcon & Workspace Setup

A standard ROS 2 workspace structure:
```
ros2_ws/
├── src/        <-- Where packages and Python source code live
├── build/      <-- Intermediate build files
├── install/    <-- Executables and launch files ready to run
└── log/        <-- Build and execution logs
```

Essential commands:
```bash
# Build package with symlinks (Python changes take effect immediately)
colcon build --symlink-install

# Source your workspace overlay
source install/setup.bash

# Inspect active node connections visually
ros2 run rqt_graph rqt_graph
```

---

## 3. Writing a Python Launch File

Instead of opening two separate terminals to start a publisher and subscriber, a **Launch File** starts both together:
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='apex_telemetry', executable='telemetry_publisher', name='publisher'),
        Node(package='apex_telemetry', executable='telemetry_listener', name='listener', output='screen'),
    ])
```

---

## 4. Curated Open-Source Video Resources

* **Nodes, Topics & Pub/Sub**: [ROS 2 Basics (Articulated Robotics)](https://www.youtube.com/watch?v=0aPbWsyS3j0) (22 mins)
* **Python Node Implementation**: [Writing Simple Pub/Sub in Python (Robotics Back-End)](https://www.youtube.com/watch?v=cM_63A5o1-4) (14 mins)
* **Python Launch Files**: [ROS 2 Launch Files in Python (Robotics Back-End)](https://www.youtube.com/watch?v=H7435f49uXg) (12 mins)

---

## ⚠️ Top 3 AI Hallucination Traps for Week 1

When asking AI (ChatGPT/Claude) for ROS 2 code, watch out for these 3 common hallucinations:

1. **ROS 1 vs ROS 2 Mix-up**: AI frequently outputs deprecated ROS 1 commands like `roscore`, `rosrun`, `rostopic echo`, or imports `import rospy`. ROS 2 uses `rclpy`, `ros2 run`, and has no `roscore`!
2. **Blocking `time.sleep()` in Callbacks**: AI will often place `time.sleep(1)` inside a subscription callback. In ROS 2's default single-threaded executor, this freezes the entire node and blocks all other topics and timers. Always use ROS 2 timers (`create_timer`) instead.
3. **Ghost Entry Points in `setup.py`**: AI creates a Python node file but forgets to declare the entry point script in `setup.py` or omits `<depend>` tags in `package.xml`. Your code will compile, but `ros2 run` will report `Package 'xyz' doesn't have the executable`.

---

## 📋 Week 1 Assignment & Deliverables

Follow the step-by-step instructions in [task.md](task.md) and record your results in [Template_Report.md](Template_Report.md) for your Saturday PR submission.

