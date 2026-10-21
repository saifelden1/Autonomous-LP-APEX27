# Week 4 Task: Rover Deployment, RViz Sensor Stream & rqt_graph

## 🎯 Objective
Deploy the 4-wheel robot model into the custom Gazebo simulation arena, drive it with keyboard teleoperation, visualize live laser scans and camera feeds in RViz2, and verify the live topic pipeline with `rqt_graph`.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Teleop Concepts (1.5 hrs)
1. Watch the curated simulation and teleop tutorials:
   * [Driving Around in Gazebo & Visualizing in RViz](https://www.youtube.com/watch?v=3iXk5hY5M7g)
   * [ROS 2 Teleop Twist Keyboard & /cmd_vel](https://www.youtube.com/watch?v=8qO5sF1Y1c4)
   * [Connecting Sensors in Gazebo to RViz2](https://www.youtube.com/watch?v=7uV8hG9zM3c)
   * [Change the Default Gazebo Camera View](https://youtu.be/fiRRzJV1YIw)
2. Understand the simulation-to-visualization bridge:
   * `teleop_twist_keyboard` -> `/cmd_vel` -> Gazebo rover controller.
   * Gazebo -> `/scan` (LaserScan), `/camera/image_raw` (Image), `/odom` -> RViz2 displays.

---

### Day 2 (Wed) — AI-Assisted Launch Integration (2.0 hrs)
1. Navigate to workspace:
   ```bash
   cd /workspace/week-4/template_ws
   ```
2. Inspect `src/apex_simulation/launch/spawn_and_rviz.launch.py`:
   * Starts Gazebo arena with `apex_arena.world`.
   * Spawns the 4-wheel rover URDF model at origin `(x=0, y=0, z=0.1)`.
   * Launches RViz2 with pre-configured sensor displays.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for unified launch pipelines.
4. Watch out for AI Trap #1: Always verify that RViz Fixed Frame is set to `odom`!
5. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```

---

### Day 3 (Fri) — Drive Rover & Verify Sensor Streams (1.5 hrs)
1. **Launch Gazebo and RViz together**:
   ```bash
   ros2 launch apex_simulation spawn_and_rviz.launch.py
   ```
2. **Drive the vehicle via teleoperation**:
   In a second terminal:
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```
   *Drive the vehicle toward arena walls using keys `i`, `j`, `l`.*

3. **Verify live sensor feeds in RViz**:
   * **LaserScan**: Subscribed to `/scan` (Notice laser points bouncing off arena walls!).
   * **Camera**: Subscribed to `/camera/image_raw` showing real-time camera view.

4. **Inspect the active node graph**:
   In a third terminal:
   ```bash
   ros2 run rqt_graph rqt_graph
   ```

---

### Day 4 (Sat) — Submission & Defense Prep (1.0 hr)
1. Capture required verification evidence:
   * Side-by-side screenshot or video showing Gazebo rover driving and RViz live `/scan` laser points reflecting off walls.
   * `rqt_graph` diagram showing full communication pipeline.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push your working branch:
   ```bash
   git add week-4/
   git commit -m "feat(week-4): complete Gazebo-RViz simulation bridge and teleop verification"
   git push -u origin your-name/week-4-simulation-rviz-bridge
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 defense questions in Section 4 of your report for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] Gazebo and RViz launch simultaneously via `spawn_and_rviz.launch.py`.
- [ ] Rover responds to keyboard teleop commands on `/cmd_vel`.
- [ ] Side-by-side screenshot of Gazebo and RViz showing live laser reflection points.
- [ ] Screenshot of `rqt_graph` showing connected teleop, Gazebo, and RViz nodes.
- [ ] [Template_Report.md](Template_Report.md) completed with debugging log and defense prep answers.
