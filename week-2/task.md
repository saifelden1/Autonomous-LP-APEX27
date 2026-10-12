# Week 2 Project: Autonomous Mission State Machine & E-Stop Action Server

## 🎯 Objective
In this project, you will build an autonomous mission execution framework consisting of:
1. `apex_mission_interfaces`: An `ament_cmake` package defining:
   * Action: `MissionTraverse.action` (simulates traversing a sequence of waypoints).
   * Service: `TriggerEStop.srv` (immediate emergency brake service).
2. `apex_mission_pkg`: An `ament_python` package containing:
   * `mission_coordinator`: An Action Server that iterates through target waypoints, publishes distance feedback at 5 Hz, checks for E-Stop cancellation, and returns completion status.
   * `emergency_stop_client`: A service node to immediately trigger an abort.
   * `mission.launch.py`: A unified launch file starting the entire stack with configurable velocity parameters.

---

## 📐 Interface Definitions

### 1. `apex_mission_interfaces/action/MissionTraverse.action`
```text
# Goal
int32 waypoint_count
float32 traverse_speed
---
# Result
bool success
float32 total_time_sec
string final_state
---
# Feedback
int32 current_waypoint
float32 progress_percent
string status_message
```

### 2. `apex_mission_interfaces/srv/TriggerEStop.srv`
```text
string reason
---
bool success
string confirmation
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Build the Interfaces Package First
In ROS 2, you must build interface packages before building nodes that import them:
```bash
cd template_ws
colcon build --symlink-install --packages-select apex_mission_interfaces
source install/setup.bash
# Verify the interface exists:
ros2 interface show apex_mission_interfaces/action/MissionTraverse
ros2 interface show apex_mission_interfaces/srv/TriggerEStop
```

### Step 2: Implement the Action Server
* File: `apex_mission_pkg/apex_mission_pkg/mission_coordinator.py`
* When an action goal arrives with `waypoint_count=5`:
  * Loop from waypoint `1` to `5`.
  * For each waypoint, simulate traversal (sleep 1.0s or use a non-blocking step).
  * Continuously publish feedback: `current_waypoint`, `progress_percent`.
  * **Crucial**: Check `goal_handle.is_cancel_requested`. If true, set state to `CANCELED` and return result immediately!
* Register a service server `/mission/emergency_stop` (`TriggerEStop`). When triggered, set a flag that cancels any running action goal.

### Step 3: Implement Launch File
* File: `apex_mission_pkg/launch/mission.launch.py`
* Launch `mission_coordinator` with parameter `default_speed:=1.5`.

---

## ✅ Pass / Fail Verification Checklist

### Test A: Normal Mission Execution
**Terminal 1 (Launch):**
```bash
source install/setup.bash
ros2 launch apex_mission_pkg mission.launch.py
```

**Terminal 2 (Send Goal):**
```bash
source install/setup.bash
ros2 action send_goal --feedback /mission/traverse apex_mission_interfaces/action/MissionTraverse "{waypoint_count: 5, traverse_speed: 2.0}"
```
* **Pass Criteria**: Terminal 2 displays live feedback increments (20%, 40%, 60%, 80%, 100%) and terminates with `success: true`.

### Test B: Emergency Stop Mid-Mission
1. Start the mission goal again with `waypoint_count: 10`.
2. In Terminal 3, trigger E-Stop while progress is at ~30%:
```bash
ros2 service call /mission/emergency_stop apex_mission_interfaces/srv/TriggerEStop "{reason: 'Obstacle detected by track marshal'}"
```
* **Pass Criteria**: Terminal 2 must instantly report goal aborted/canceled. The node must not crash or hang.
