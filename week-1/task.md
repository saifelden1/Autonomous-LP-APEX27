# Week 1 Task: Telemetry Publisher, Subscriber & Launch File

## 🎯 Objective
Learn how ROS 2 nodes communicate by creating a simple publisher and subscriber pair with an automated launch file, then inspect the live connection using `rqt_graph`.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
```

### Step 2: Implement Nodes
* `telemetry_publisher.py`: Publishes `Apex Rover Ping: <counter>` to `/vehicle/telemetry` at 2 Hz (every 0.5s).
* `telemetry_listener.py`: Subscribes to `/vehicle/telemetry` and logs `Received: [msg]` to the console.

### Step 3: Implement Launch File
* File: `launch/telemetry.launch.py`
* Starts both the publisher and listener nodes in one command.

### Step 4: Build and Source
```bash
colcon build --symlink-install
source install/setup.bash
```

---

## ✅ Pass / Fail Verification Deliverable

1. **Launch the Nodes**:
   ```bash
   ros2 launch apex_telemetry telemetry.launch.py
   ```
   *Terminal should show the listener actively printing messages received from the publisher.*

2. **Inspect the Graph**:
   In a second terminal:
   ```bash
   ros2 run rqt_graph rqt_graph
   ```

Take a screenshot showing the terminal output alongside the `rqt_graph` window showing the arrow from the publisher node to the subscriber node via `/vehicle/telemetry`.
