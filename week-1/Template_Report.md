# Week 1 Documentation & ROS 2 Telemetry Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-1-ros2-basics]  

---

## 1. Node Architecture & Topic Configuration

| Parameter | Implemented Specification |
| :--- | :--- |
| **Package Name** | `apex_telemetry` |
| **Publisher Node Name** | `telemetry_publisher_node` |
| **Subscriber Node Name** | `telemetry_listener_node` |
| **Telemetry Topic** | `/vehicle/telemetry` |
| **Message Type** | `std_msgs/msg/String` |
| **Publishing Frequency** | [e.g. 2 Hz or 10 Hz] |
| **Launch File Name** | `launch/telemetry.launch.py` |

---

## 2. Verification Screenshots & Terminal Evidence

### 2.1 Colcon Build Output
Paste the build output showing zero compilation errors:
```bash
colcon build --symlink-install
```
*Output snippet:*
```text
[Paste terminal text here]
```

### 2.2 Live Telemetry Terminal Log
Paste terminal snippet showing listener receiving telemetry messages:
```text
[Paste listener terminal log here]
```

### 2.3 Rqt_Graph Verification Screenshot
Embed or link your `rqt_graph` screenshot showing publisher connected to subscriber:
`![Week 1 rqt_graph Verification](rqt_graph_telemetry.png)`

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue / Bug Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: Package 'apex_telemetry' doesn't have executable* | *Forgot to add entry point in setup.py console_scripts* | *Added executable entry point into setup.py and re-ran colcon build* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **Why is it dangerous to place a blocking `time.sleep(1)` inside a ROS 2 subscription callback? What should you use instead?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **What does the `--symlink-install` flag do in `colcon build`, and why is it useful during Python node development?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **In the vehicle telemetry pipeline (Formula AI or Mars Rover), why do we separate sensors into independent nodes communicating over topics rather than writing one giant Python script?**  
   [Write a 2-3 sentence explanation to practice your defense]
