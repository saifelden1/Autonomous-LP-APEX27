# Week 5 Task: Perception Pipeline Exploration & 3D Feature Visualization

## 🎯 Objective
Gain practical exposure to the perception pipeline: run an automated cone/landmark detector that converts camera images into 3D RViz markers, inspect the topic contracts required for SLAM, and study sensor fusion localization.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Watch & Perception Concepts (1.5 hrs)
1. Watch the curated sensor fusion, SLAM, and Nav2 tutorials:
   * [1. Exploring Common Sensors for Nav2](https://youtu.be/VSzkBNJegS4)
   * [2. Coordinate Transformations for Navigation](https://youtu.be/eDyHFa1LmpQ)
   * [3. Sensor Fusion & Localization](https://youtu.be/XOQTF38lmtE)
   * [4. Building a Map with SLAM](https://youtu.be/VoX5AwTfHuQ)
   * [5. Installing Nav2](https://youtu.be/gyskLlvX3oI)
   * *(Supplemental)*: [Sensor Fusion & Tracking Playlist (MATLAB)](https://youtube.com/playlist?list=PLn8PRpmsu08ryYoBpEKzoMOveSTyS-h4a&si=B75o2uHrgnkkt5sC)
2. Understand the perception dataflow:
   * Raw camera image -> OpenCV HSV segmentation -> Contour detection -> 3D `MarkerArray` on `/perception/cone_markers`.

---

### Day 2 (Wed) — AI-Assisted Perception Pipeline (2.0 hrs)
1. Navigate to workspace:
   ```bash
   cd /workspace/week-5/template_ws
   ```
2. Inspect `src/apex_perception/`:
   * `cone_detector_node.py`: Subscribes to camera frames and extracts yellow/blue cone centroids.
   * `launch/perception_pipeline.launch.py`: Starts camera simulator and detection pipeline.
3. Consult [ai_prompting_guide.md](ai_prompting_guide.md) to practice prompting AI for vision filters.
4. Watch out for AI Trap #2: Ensure camera optical coordinate transforms are applied so markers do not appear sideways!
5. Build the workspace:
   ```bash
   colcon build --symlink-install
   source install/setup.bash
   ```

---

### Day 3 (Fri) — Launch Pipeline & Inspect 3D Markers (1.5 hrs)
1. **Launch perception pipeline**:
   ```bash
   ros2 launch apex_perception perception_pipeline.launch.py
   ```
2. **View annotated camera stream**:
   In a second terminal:
   ```bash
   ros2 run rqt_image_view rqt_image_view /perception/debug_image
   ```
   *Notice the bounding boxes tracking yellow and blue cones in real time.*

3. **Inspect 3D marker coordinates**:
   In a third terminal:
   ```bash
   ros2 topic echo /perception/cone_markers
   ```
   *Observe metric coordinates (X, Y, Z) published relative to the vehicle frame.*

---

### Day 4 (Sat) — Submission & Defense Prep (1.0 hr)
1. Capture required verification evidence:
   * Screenshot of `rqt_image_view` displaying the annotated detection camera feed.
   * Terminal output showing `ros2 topic echo /perception/cone_markers`.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push your working branch:
   ```bash
   git add week-5/
   git commit -m "feat(week-5): complete perception landmark detection pipeline and verification"
   git push -u origin your-name/week-5-perception-slam
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 defense questions in Section 4 of your report for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Workspace compiles cleanly with `colcon build --symlink-install`.
- [ ] Perception pipeline launches cleanly via `perception_pipeline.launch.py`.
- [ ] Screenshot of `rqt_image_view` showing active bounding boxes on track cones.
- [ ] Terminal snippet of `/perception/cone_markers` reporting 3D metric coordinates.
- [ ] [Template_Report.md](Template_Report.md) completed with debugging log and defense prep answers.
