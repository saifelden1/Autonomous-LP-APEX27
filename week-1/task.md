# Week 1 Task: Telemetry Publisher, Subscriber & Launch File

## 🎯 Objective
Learn how ROS 2 nodes communicate by creating a telemetry publisher and subscriber pair orchestrated with a Python launch file, then verify the live connection using `rqt_graph`.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Conceptualize (1.5 hrs)
1. Watch the core open-source tutorials:
   * [ROS 2 Basics: Nodes, Topics & Pub/Sub](https://www.youtube.com/watch?v=0aPbWsyS3j0) (Articulated Robotics - 22 min)
   * [Writing Pub/Sub in Python](https://www.youtube.com/watch?v=cM_63A5o1-4) (Robotics Back-End - 14 min)
   * [ROS 2 Python Launch Files](https://www.youtube.com/watch?v=H7435f49uXg) (Robotics Back-End - 12 min)
2. Understand the vehicle communication graph:
   * `telemetry_publisher` broadcasts vehicle health (battery voltage, sequence) to `/vehicle/telemetry`.
   * `telemetry_listener` subscribes to `/vehicle/telemetry` and logs data to console.

---

### Day 2 (Wed) — AI-Assisted Implementation (2.0 hrs)
1. Open your terminal inside the Docker container or Ubuntu:
   ```bash
   cd /workspace/week-1/template_ws
   ```
2. Review the starter package in `src/apex_telemetry/`:
   * `apex_telemetry/telemetry_publisher.py`: Generates simulated battery telemetry.
   * `apex_telemetry/telemetry_listener.py`: Receives and logs incoming telemetry.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for node enhancements.
4. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```
   *(Ensure build completes with 0 errors!)*

---

### Day 3 (Fri) — Launch & rqt_graph Inspection (1.5 hrs)
1. **Launch both nodes with a single command**:
   ```bash
   ros2 launch apex_telemetry telemetry.launch.py
   ```
   *Terminal should show the listener actively printing messages received from the publisher.*

2. **Inspect the live graph in a second terminal**:
   ```bash
   ros2 run rqt_graph rqt_graph
   ```
   *Verify that you see an arrow connecting `/telemetry_publisher` to `/telemetry_listener` through topic `/vehicle/telemetry`.*

3. *(Optional Bonus)*: In `src/apex_telemetry/apex_telemetry/safety_watchdog.py`, test the watchdog safety monitor that triggers an E-Stop if telemetry stops!

---

### Day 4 (Sat) — Submission & Oral Defense Prep (1.0 hr)
1. Capture 2 required screenshots:
   * Terminal output showing listener printing telemetry messages.
   * `rqt_graph` window showing the connected nodes.
2. Fill out all sections in [Template_Report.md](Template_Report.md).
3. Commit and push your personal branch:
   ```bash
   git add week-1/
   git commit -m "feat(week-1): complete telemetry nodes, launch file, and report"
   git push -u origin your-name/week-1-ros2-basics
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 defense questions in Section 4 of your report for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] Nodes launch cleanly via `ros2 launch apex_telemetry telemetry.launch.py`.
- [ ] Screenshot of `rqt_graph` attached showing connected nodes.
- [ ] Screenshot of listener terminal output attached.
- [ ] [Template_Report.md](Template_Report.md) completed with debugging log and defense prep answers.
