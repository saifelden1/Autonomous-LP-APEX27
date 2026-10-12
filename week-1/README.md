# Week 1: Linux CLI, ROS 2 Architecture & Node Primitives

Welcome to Week 1! This week starts from **absolute zero**. Even if you have never opened a Linux terminal or compiled a robotics package, this guide will walk you through the core foundations.

---

## 1. Zero-to-One Linux Terminal Primitives

Robotics software runs on Linux (Ubuntu). Before writing ROS 2 code, you must know these terminal commands:

| Command | Purpose | Example |
| :--- | :--- | :--- |
| `pwd` | Print working directory (Where am I?) | `pwd` |
| `cd <path>` | Change directory | `cd ~/ros2_ws` |
| `ls -la` | List files including hidden (`.` and `..`) | `ls -la` |
| `mkdir -p <dir>` | Create directory and parents | `mkdir -p ~/ros2_ws/src` |
| `source <file>` | Load environment variables into current terminal | `source /opt/ros/humble/setup.bash` |
| `export VAR=val` | Set an environment variable | `export ROS_DOMAIN_ID=42` |

---

## 2. What is ROS 2? The Computation Graph

ROS 2 (Robot Operating System) is **not** an operating system like Windows or Linux. It is a **middleware framework** that allows independent programs (called **Nodes**) to talk to each other across processes and computers.

```
+--------------------------------+                  +-------------------------------+
|         Publisher Node         |                  |        Subscriber Node        |
|  (e.g., telemetry_publisher)   |                  |    (e.g., safety_watchdog)    |
|                                |                  |                               |
|        [ Timer Callback ]      |                  |     [ Subscription Callback ] |
|                 |              |                  |                 ^             |
|                 v              |                  |                 |             |
|      publishes to /telemetry   |  ==== DDS ====   |  listens on /telemetry        |
+--------------------------------+     Network      +-------------------------------+
                                        Bus
```

### Key Concepts:
1. **Node**: An executable process with a dedicated role (e.g., reading camera data, steering wheels, monitoring battery).
2. **Topic**: A named communication bus (e.g., `/vehicle/telemetry`).
3. **Message Type**: A strict data contract (e.g., `std_msgs/msg/String`, `builtin_interfaces/msg/Time`).
4. **Publisher**: A node that broadcasts messages over a topic.
5. **Subscriber**: A node that registers interest in a topic and triggers a **callback function** whenever a new message arrives.
6. **DDS (Data Distribution Service)**: The underlying network protocol that handles automatic node discovery.

---

## 3. Quality of Service (QoS) Profiles

In autonomous racing (Formula AI) and planetary rovers (ERC 27), network conditions vary wildly:
* **Reliability**:
  * `Reliable`: Guarantees delivery (like TCP). Used for state machine transitions, E-Stops, and mission commands.
  * `BestEffort`: Drops late packets if network is congested (like UDP). Used for high-frequency sensor streams (LiDAR, camera images, wheel encoder ticks).
* **Durability**:
  * `Volatile`: Late-joining subscribers only receive future messages.
  * `TransientLocal`: Late-joining subscribers receive the last known message (great for map data).

> [!WARNING] QoS Incompatibility Silent Failure
> If a publisher is configured with `BestEffort` and a subscriber demands `Reliable`, ROS 2 will **silently fail to connect them**. No error will be printed, but zero messages will be received!

---

## 4. Dissecting a Minimal Python ROS 2 Node

Here is the clean structure of an idiomatic ROS 2 node using `rclpy`:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher') # 1. Initialize node with a unique name
        
        # 2. Create a publisher: Topic name, Message type, Queue depth
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # 3. Create a timer running at 2 Hz (every 0.5 seconds)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Apex Telemetry Ping: {self.count}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.count += 1

def main(args=None):
    rclpy.init(args=args)          # Initialize ROS 2 communication
    node = MinimalPublisher()      # Instantiate node
    rclpy.spin(node)               # Keep node alive and process callbacks
    node.destroy_node()            # Clean shutdown
    rclpy.shutdown()
```

---

## 5. Building with Colcon & The Workspace Structure

A ROS 2 workspace consists of four directories:
```
ros2_ws/
├── src/        <-- Where your source code packages live (tracked by Git)
├── build/      <-- Intermediate compiler / build artifacts (ignored)
├── install/    <-- Executables, libraries, and launch scripts ready to run
└── log/        <-- Build and runtime logs
```

To build and run:
```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
ros2 run apex_telemetry telemetry_publisher
```
