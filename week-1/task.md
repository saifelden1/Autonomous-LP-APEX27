# Week 1 Project: Rover/Car Telemetry Heartbeat & Safety Watchdog

## 🎯 Objective
In both Formula Student AI and European Rover Challenge, continuous vehicle health telemetry is safety-critical. If the vehicle loses telemetry or the onboard central computer freezes, a safety watchdog must instantly detect communication loss and command an emergency stop.

You will build a package called `apex_telemetry` containing two collaborating nodes:
1. `telemetry_publisher`: Simulates vehicle status (battery voltage, motor temperature, heartbeat tick) at a fixed rate (10 Hz).
2. `safety_watchdog`: Monitors incoming telemetry. If no heartbeat is received within `timeout_sec` (configurable parameter, default 0.5s), it triggers an emergency alarm on `/safety/emergency_stop`.

---

## 📐 System Architecture

```
+--------------------------------------+
|         telemetry_publisher          |
|  - Rate: 10 Hz                       |
|  - Topic: /vehicle/telemetry         |
|  - Type:  std_msgs/msg/String        |
+--------------------------------------+
                   |
                   | JSON or formatted string: "seq=12,volt=24.2,temp=41.5"
                   v
+--------------------------------------+
|           safety_watchdog            |
|  - Parameter: timeout_sec (0.5s)     |
|  - Subscribes: /vehicle/telemetry    |
|  - Publishes:  /safety/estop_trigger |
|    Type:       std_msgs/msg/Bool     |
+--------------------------------------+
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Initialize Workspace & Package
Navigate to `week-1/template_ws` or your workspace:
```bash
cd template_ws/src
# Verify package structure exists
ls apex_telemetry
```

### Step 2: Implement `telemetry_publisher.py`
* Node name: `telemetry_publisher_node`
* Publish to: `/vehicle/telemetry` (`std_msgs/msg/String`)
* Timer frequency: `10.0` Hz (period: `0.1` seconds)
* Content format: `seq: <count> | voltage: <24.0 - 26.0 V> | status: OK`

### Step 3: Implement `safety_watchdog.py`
* Node name: `safety_watchdog_node`
* Declare parameter: `timeout_sec` (default: `0.5`)
* Subscribe to: `/vehicle/telemetry`
* Publish to: `/safety/estop_trigger` (`std_msgs/msg/Bool`)
* Watchdog timer: Check at `20` Hz (`0.05s`). If `current_time - last_msg_time > timeout_sec`, publish `Bool(data=True)` and log a throttled ERROR. When healthy, publish `Bool(data=False)`.

### Step 4: Register Entry Points in `setup.py`
Make sure `setup.py` has:
```python
entry_points={
    'console_scripts': [
        'telemetry_publisher = apex_telemetry.telemetry_publisher:main',
        'safety_watchdog = apex_telemetry.safety_watchdog:main',
    ],
},
```

---

## ✅ Pass / Fail Verification Checklist

Open three terminals to execute this verification test:

**Terminal 1 (Publisher):**
```bash
source install/setup.bash
ros2 run apex_telemetry telemetry_publisher
```

**Terminal 2 (Watchdog):**
```bash
source install/setup.bash
ros2 run apex_telemetry safety_watchdog --ros-args -p timeout_sec:=0.5
```

**Terminal 3 (Echo E-Stop Topic):**
```bash
source install/setup.bash
ros2 topic echo /safety/estop_trigger
```

### Verification Criteria:
1. When both nodes are running: `/safety/estop_trigger` outputs `data: false`.
2. Kill Terminal 1 (`Ctrl+C`): Within **0.5 seconds**, Terminal 2 must log an ERROR and `/safety/estop_trigger` must immediately switch to `data: true`.
3. Restart Terminal 1: Watchdog must log that connection is restored, and `/safety/estop_trigger` returns to `false`.

Record a 30-to-60 second video demonstrating these 3 steps for your PR submission!
