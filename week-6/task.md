# Week 6 Task: Autonomous Navigation & Path Tracking Exposure (Capstone)

## 🎯 Objective
Gain practical exposure to autonomous navigation: run a Pure Pursuit path follower in simulation, observe how it computes curvature from `/plan` and `/odom` to drive the vehicle autonomously along a course, and inspect the Nav2 Simple Commander API.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Planning Concepts (1.5 hrs)
1. Watch the curated navigation, path planning, and controller tutorials:
   * [1. Path Planning with A* and RRT](https://youtu.be/QR3U1dgc5RE)
   * [2. Autonomous Navigation Using ROS 2](https://youtu.be/YzTMROP4qos)
   * [3. Simple Commander API in Python](https://youtu.be/gKoXrrj2klg)
   * [4. Autonomous Docking with AprilTags](https://youtu.be/tFE75bP-ASo)
   * *(Supplemental)*: [Automatic Addison Series Playlist](https://www.youtube.com/playlist?list=PLNWNEEf8BvG64FVZT4IdieI1PuYnHkUrt)
2. Study the Pure Pursuit control equations:
   * Lookahead distance $L_d$, heading error $\alpha$, curvature $\kappa = \frac{2\sin(\alpha)}{L_d}$, $\omega = v \cdot \kappa$.

---

### Day 2 (Wed) — AI-Assisted Controller Implementation (2.0 hrs)
1. Navigate to workspace:
   ```bash
   cd /workspace/week-6/template_ws
   ```
2. Inspect `src/apex_navigation/`:
   * `pure_pursuit_controller.py`: Subscribes to `/plan` and `/odom` and publishes `/cmd_vel`.
   * `path_publisher.py`: Generates a closed-loop reference path around the arena.
   * `launch/capstone_autonomous_nav.launch.py`: Starts full autonomous navigation stack.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for controller tuning.
4. Watch out for AI Trap #1: Ensure angular velocity `cmd.angular.z` is clamped to prevent uncontrolled vehicle spinning!
5. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```

---

### Day 3 (Fri) — Launch Autonomous Navigation & Tune Parameters (1.5 hrs)
1. **Launch the Capstone autonomous run**:
   ```bash
   ros2 launch apex_navigation capstone_autonomous_nav.launch.py
   ```
2. **Monitor real-time velocity commands**:
   In a second terminal:
   ```bash
   ros2 topic echo /cmd_vel
   ```
   *Notice how angular.z continuously steers left and right to keep the rover locked to the path.*

3. **Verify obstacle clearance and trajectory tracking**:
   * Observe the simulated vehicle navigate around the course without colliding with boundaries.

---

### Day 4 (Sat) — Capstone Report Submission & Defense Prep (1.0 hr)
1. Capture required verification evidence:
   * Terminal output showing `ros2 topic echo /cmd_vel` outputting active steering commands.
   * Screenshot of simulation showing the vehicle successfully navigating the waypoint course.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push your working branch:
   ```bash
   git add week-6/
   git commit -m "feat(week-6): complete Capstone autonomous navigation and Pure Pursuit control"
   git push -u origin your-name/week-6-planning-control
   ```
4. Open your final Capstone Pull Request on GitHub by Saturday 11:59 PM.
5. Review the comprehensive defense questions in Section 4 for your final onboarding graduation interview.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] Autonomous navigation launches cleanly via `capstone_autonomous_nav.launch.py`.
- [ ] Rover autonomously navigates the waypoint track without hitting arena walls.
- [ ] Terminal snippet of `/cmd_vel` showing dynamic linear and angular velocity values.
- [ ] [Template_Report.md](Template_Report.md) completed with controller parameters and defense prep answers.
