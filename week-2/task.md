# Week 2 Task: 4-Wheel Robot Model & RViz TF Inspection

## 🎯 Objective
Assemble a 4-wheeled autonomous vehicle model in URDF/Xacro, configure its links and continuous joints according to REP-105 standards, and inspect its TF tree visually in RViz2 using `joint_state_publisher_gui`.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Model Concepts (1.5 hrs)
1. Watch the curated Automatic Addison tutorials:
   * [Coordinate Frame Basics & Right Hand Rule](https://youtu.com/oxr8df96tWk)
   * [Create & Visualize Mobile Robot with URDF](https://youtu.be/XtS8mCcffrs)
   * [URDF Display Launch Files](https://youtu.be/2ri0Ouc67W0)
   * [Customizing Robot Parameters in RViz](https://youtu.be/AkekfmNAUkk)
2. Study REP-105 standard coordinate conventions:
   * `base_footprint` (ground projection) -> `base_link` (vehicle center) -> wheels & sensors (`lidar_link`, `camera_link`).

---

### Day 2 (Wed) — AI-Assisted URDF Assembly (2.0 hrs)
1. Navigate to workspace:
   ```bash
   cd /workspace/week-2/template_ws
   ```
2. Inspect `src/apex_robot_description/urdf/apex_chassis.urdf.xacro`:
   * Main `chassis` link with visual, collision, and inertial properties.
   * 4 wheels (front-left, front-right, rear-left, rear-right) connected with continuous joints.
   * Mounted sensor links: `lidar_link` and `camera_link`.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for URDF macros.
4. Watch out for AI Trap #2: Cylinder wheel orientations require `<origin rpy="1.5708 0 0"/>` so wheels don't slide on flat ends!
5. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```

---

### Day 3 (Fri) — Launch RViz & Articulate Joints (1.5 hrs)
1. **Launch the robot visualizer**:
   ```bash
   ros2 launch apex_robot_description display_rviz.launch.py
   ```
   *RViz2 opens showing the 3D rover model with coordinate axes (RGB = XYZ).*
   *`joint_state_publisher_gui` opens with sliders for the 4 wheel joints.*

2. **Articulate joints**:
   * Move the wheel sliders and verify that the wheels rotate smoothly in RViz.

3. **Generate the TF coordinate tree**:
   In a second terminal:
   ```bash
   ros2 run tf2_tools view_frames
   ```
   *Generates `frames.pdf` documenting the unbroken tree hierarchy.*

---

### Day 4 (Sat) — Submission & Defense Prep (1.0 hr)
1. Capture required verification evidence:
   * RViz2 screenshot showing the vehicle model and coordinate axes.
   * Side-by-side screenshot of `joint_state_publisher_gui` moving the wheels.
   * Generated `frames.pdf` diagram.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push your working branch:
   ```bash
   git add week-2/
   git commit -m "feat(week-2): complete 4-wheel rover URDF model and RViz TF inspection"
   git push -u origin your-name/week-2-urdf-tf-rviz
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 defense questions in Section 4 of your report for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] Model launches cleanly via `ros2 launch apex_robot_description display_rviz.launch.py`.
- [ ] Screenshot of RViz2 vehicle model side-by-side with `joint_state_publisher_gui`.
- [ ] Generated `frames.pdf` attached showing unbroken TF tree from `base_link`.
- [ ] [Template_Report.md](Template_Report.md) completed with debugging log and defense prep answers.
