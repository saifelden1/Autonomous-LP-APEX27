# Week 2: Custom Interfaces, Services, Actions & Launch Files

In Week 1, you learned how nodes pass data continuously using topics. However, autonomous vehicles need more than just one-way streams:
* When a vehicle starts a race or Mars Yard traverse, it needs a **Mission Goal** that reports progress and can be canceled (**Actions**).
* When a human hits an emergency stop or requests a sensor reset, it needs an immediate acknowledgment (**Services**).
* When changing driving parameters across 10 nodes at once, it needs **Launch Files** and **Parameters**.

---

## 1. Custom ROS 2 Interfaces (.msg, .srv, .action)

ROS 2 communicates using strictly typed data structures. When built-in messages (`std_msgs`, `geometry_msgs`) are not enough, we define custom interfaces.

```
apex_mission_interfaces/
├── msg/
│   └── RoverStatus.msg       # Custom data fields
├── srv/
│   └── TriggerEStop.srv      # Request ---> Response
└── action/
    └── MissionTraverse.action # Goal ---> Feedback ... Feedback ---> Result
```

### Anatomy of an Action Definition (`.action`)
Actions are split into three parts separated by `---`:
```text
# 1. Goal (What the client requests)
geometry_msgs/Point[] target_waypoints
float32 target_speed

---
# 2. Result (Returned when the goal finishes or cancels)
bool success
float32 total_time_sec
int32 waypoints_completed

---
# 3. Feedback (Sent continuously during execution)
int32 current_waypoint_index
float32 distance_to_next_waypoint
string current_state
```

---

## 2. Topic vs Service vs Action: When to Use What?

| Pattern | Type | Communication Model | Formula AI / ERC Example |
| :--- | :--- | :--- | :--- |
| **Topic** | Unidirectional, 1-to-many | Continuous stream without response | LiDAR point clouds, Camera frames, `/cmd_vel` |
| **Service** | Bidirectional, 1-to-1 | Instant Request/Response (blocking or async) | Calibrate IMU, Reset odometry, Toggle headlights |
| **Action** | Bidirectional, 1-to-1 | Long-running goal with periodic feedback & cancel | Drive 20-meter cone slalom, Traverse to Mars crater |

---

## 3. ROS 2 Parameters & Dynamic Reconfiguration

Parameters are node-level configuration values. Instead of hardcoding numbers inside Python code:
```python
# Declare parameter with default value
self.declare_parameter('max_velocity', 2.5)

# Read parameter value
max_vel = self.get_parameter('max_velocity').get_parameter_value().double_value
```

Parameters can be loaded from a YAML configuration file or overridden via the command line:
```bash
ros2 run apex_mission_pkg mission_server --ros-args -p max_velocity:=3.0
```

---

## 4. Python Launch Systems (`launch.py`)

In production robotics, you never open 15 terminal windows to start 15 nodes. You write a **Launch File** that launches nodes with parameters, namespaces, and arguments together.

Example `mission.launch.py`:
```python
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('max_speed', default_value='2.0'),
        
        Node(
            package='apex_mission_pkg',
            executable='mission_server',
            name='mission_coordinator',
            output='screen',
            parameters=[{'max_velocity': LaunchConfiguration('max_speed')}]
        )
    ])
```
