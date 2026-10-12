# Week 1: AI Prompting Guide & Comprehension Protocol

As an APEX recruit, you must learn to direct AI models (ChatGPT, Claude, Antigravity) with surgical precision. Follow these prompts and self-tests.

---

## 1. Prompt Templates for Week 1

### Prompt 1: Understanding Node Architecture
> "I am a beginner in ROS 2 Humble. Explain the lifecycle of an `rclpy` node. Specifically, what does `rclpy.spin()` actually do under the hood with callbacks, and what happens if I place a blocking `time.sleep(5)` inside a subscriber callback?"

### Prompt 2: Scaffolding the Watchdog
> "Write a ROS 2 Humble Python node named `SafetyWatchdogNode`.
> Requirements:
> 1. Subscribe to `/rover/telemetry` with type `std_msgs/msg/String`.
> 2. Track the timestamp of the last received message.
> 3. Run a timer at 10 Hz checking if the duration since the last message exceeds a configurable parameter `timeout_seconds` (default: 0.5s).
> 4. If timed out, log an ERROR warning: 'CRITICAL: Telemetry Heartbeat Lost! Triggering E-STOP'.
> 5. When messages resume, log an INFO message: 'Telemetry Restored'.
> Please annotate each section with comments explaining ROS 2 concepts."

### Prompt 3: Diagnosing QoS Issues
> "My ROS 2 publisher is broadcasting to `/vehicle/status` using `QoSProfile(reliability=ReliabilityPolicy.BEST_EFFORT)`. My subscriber uses `QoSProfile(reliability=ReliabilityPolicy.RELIABLE)`. Why does `ros2 topic echo` show data, but my subscriber callback is never invoked? Explain ROS 2 QoS compatibility rules."

---

## 2. Anti-Patterns (Do NOT Do This!)

❌ **Bad**: "Make a ROS2 project for a rover."  
*(Result: Generates unmaintainable, outdated ROS 1 code or bloated generic files).*

❌ **Bad**: "Fix this error: code crashed."  
*(Result: AI guesses blindly and breaks working configurations).*

✅ **Good**: "Here is my `package.xml`, my `setup.py`, and the error from `colcon build`. Why is the entry point unrecognized?"

---

## 3. Self-Check Comprehension Gate

Before submitting your Week 1 project, ensure you can answer:
1. What is the difference between `ros2 run` and running the Python file directly via `python3 my_node.py`?
2. Why is `--symlink-install` crucial during development?
3. Where does ROS 2 store registered entry points?
4. What happens when two nodes on the same network have the exact same node name?
