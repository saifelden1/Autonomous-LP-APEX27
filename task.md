# Week 5 Task: Perception Pipeline Exploration & 3D Feature Visualization

## 🎯 Objective
Gain practical exposure to the perception pipeline: run an automated cone/landmark detector that converts camera images into 3D RViz markers, and inspect the topic contracts required for SLAM.

---

## 🛠️ Step-by-Step Instructions

### Step 1: Navigate to Workspace
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Launch the Perception Pipeline
```bash
ros2 launch apex_perception perception_pipeline.launch.py
```
*Starts the synthetic camera feed and the cone detection node.*

### Step 3: Inspect Outputs
1. View the annotated camera feed:
   ```bash
   ros2 run rqt_image_view rqt_image_view /perception/debug_image
   ```
   *Notice the green bounding boxes tracking the blue and yellow cones.*

2. Inspect the 3D Marker topic:
   ```bash
   ros2 topic echo /perception/cone_markers
   ```

---

## ✅ Pass / Fail Verification Deliverable

Submit a screenshot showing:
1. `rqt_image_view` displaying the annotated cone detection camera feed.
2. Terminal output showing `ros2 topic echo /perception/cone_markers` reporting marker coordinate positions.
