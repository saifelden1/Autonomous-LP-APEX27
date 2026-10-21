# Week 5 Documentation & Perception Pipeline Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-5-perception-slam]  

---

## 1. Perception & Detection Pipeline Specifications

| Parameter | Implemented Specification |
| :--- | :--- |
| **Input Camera Topic** | `/camera/image_raw` |
| **Debug Image Topic** | `/perception/debug_image` |
| **Marker Output Topic**| `/perception/cone_markers` |
| **Marker Message Type**| `visualization_msgs/msg/MarkerArray` |
| **Target Colors** | Yellow cones (right track) & Blue cones (left track) / ArUco markers |
| **Color Space Used** | HSV (Hue, Saturation, Value) |

---

## 2. Verification Screenshots & Terminal Evidence

### 2.1 Annotated Camera Feed (`rqt_image_view`)
Embed or link your screenshot showing bounding boxes around detected cones:
`![Week 5 Bounding Boxes](perception_bounding_boxes.png)`

### 2.2 3D Marker Echo Output
Paste the terminal output snippet showing marker coordinate positions:
```text
[Paste ros2 topic echo /perception/cone_markers snippet here]
```

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: Detected markers appeared sideways in RViz* | *Robot body vs optical camera frame coordinate mismatch* | *Applied standard optical frame rotation to camera link* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **Why does autonomous vehicle perception commonly convert camera images from RGB to HSV color space before performing thresholding?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **In SLAM, why is the `map -> odom` transform broadcasted dynamically by the SLAM node rather than using a static transform?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **What is sensor fusion (e.g. Extended Kalman Filter), and why do we fuse wheel encoders with an IMU rather than relying solely on wheel odometry?**  
   [Write a 2-3 sentence explanation to practice your defense]
