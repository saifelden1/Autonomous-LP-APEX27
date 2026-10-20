# Week 3 Task: Custom Gazebo Arena & World Creation

## 🎯 Objective
Create a custom Gazebo simulation arena (`apex_arena.world`) with enclosing boundary walls, ground friction, and test obstacle pillars, and launch it using a ROS 2 launch file at a stable 1 kHz physics rate.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Physics Concepts (1.5 hrs)
1. Watch the curated Automatic Addison Gazebo tutorials:
   * [How to Simulate a Mobile Robot in Gazebo](https://youtu.be/wZV1PoZ4fyk)
   * [How to Change the Default Gazebo Camera View](https://youtu.be/fiRRzJV1YIw)
   * [Full Automatic Addison Robotics Series](https://www.youtube.com/playlist?list=PLNWNEEf8BvG64FVZT4IdieI1PuYnHkUrt)
2. Study SDF physics properties:
   * Real-time update rate (1000 Hz) and max step size (0.001s).
   * Sun lighting, ground plane physics friction, and boundary wall models.

---

### Day 2 (Wed) — AI-Assisted World Construction (2.0 hrs)
1. Navigate to workspace:
   ```bash
   cd /workspace/week-3/template_ws
   ```
2. Inspect `src/apex_gazebo_worlds/worlds/apex_arena.world`:
   * 10m x 10m enclosed arena with 4 perimeter walls.
   * Internal obstacle blocks and lighting elements.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for custom world objects.
4. Watch out for AI Trap #2: Missing `<include><uri>model://sun</uri></include>` causes a black screen where objects fall infinitely!
5. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```

---

### Day 3 (Fri) — Launch Gazebo World & Inspect Physics (1.5 hrs)
1. **Launch the custom arena**:
   ```bash
   ros2 launch apex_gazebo_worlds world.launch.py
   ```
   *Gazebo simulation window opens with the 10m x 10m arena, walls, and obstacle blocks loaded.*

2. **Verify physics stability**:
   * Inspect the bottom status bar in Gazebo:
     * **Real Time Factor (RTF)**: Should be stable between ~0.85 and 1.00.
     * **Sim Time**: Advances smoothly without freezing.

---

### Day 4 (Sat) — Submission & Defense Prep (1.0 hr)
1. Capture required verification evidence:
   * High-resolution screenshot of Gazebo running `apex_arena.world`.
   * Terminal output showing launch logs without plugin load errors.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push your working branch:
   ```bash
   git add week-3/
   git commit -m "feat(week-3): complete Gazebo arena world, physics configuration, and report"
   git push -u origin your-name/week-3-gazebo-sensors-world
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 defense questions in Section 4 of your report for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] World launches cleanly via `ros2 launch apex_gazebo_worlds world.launch.py`.
- [ ] Screenshot of Gazebo running `apex_arena.world` with boundary walls and obstacles.
- [ ] Physics simulation runs stably with Real Time Factor ~1.0.
- [ ] [Template_Report.md](Template_Report.md) completed with debugging log and defense prep answers.
