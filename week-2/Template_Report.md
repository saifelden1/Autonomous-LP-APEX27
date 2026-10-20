# Week 2 Documentation & URDF/TF Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-2-urdf-tf-rviz]  

---

## 1. Robot Kinematics & Link Specifications

| Link / Joint Name | Type | Parent Link | Child Link | Purpose / Sensor |
| :--- | :--- | :--- | :--- | :--- |
| `base_link` | Link | None (Root) | — | Geometric center of vehicle body |
| `chassis_joint` | Fixed | `base_link` | `chassis` | Main chassis structural body |
| `front_left_wheel_joint` | Continuous | `chassis` | `front_left_wheel` | Front-left driving wheel |
| `front_right_wheel_joint`| Continuous | `chassis` | `front_right_wheel`| Front-right driving wheel |
| `lidar_joint` | Fixed | `chassis` | `lidar_link` | 2D/3D LiDAR sensor mount |
| `camera_joint` | Fixed | `chassis` | `camera_link` | Monocular / Stereo camera mount |

---

## 2. Verification Screenshots & TF Evidence

### 2.1 RViz2 Model & Joint GUI Screenshot
Embed or link your screenshot showing RViz2 with coordinate frames active and `joint_state_publisher_gui`:
`![Week 2 RViz2 Inspection](rviz_robot_model.png)`

### 2.2 TF Tree Evidence
Attach the generated TF tree diagram:
`[TF Tree PDF](frames.pdf)`

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: Wheel slid on flat face instead of rolling* | *Cylinder aligned along Z-axis by default in URDF* | *Added `<origin rpy="1.5708 0 0"/>` to orient cylinder along Y-axis* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **According to REP-105 standard, why do autonomous mobile robots have both a `base_footprint` and a `base_link` frame?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **Why must link cylinders have explicit roll rotation (`rpy="1.5708 0 0"`) when modeled as wheels?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **In Formula AI and Mars Rover systems, why is it critical that all sensor links (LiDAR, Camera, IMU) maintain rigid transforms linked back to `base_link`?**  
   [Write a 2-3 sentence explanation to practice your defense]
