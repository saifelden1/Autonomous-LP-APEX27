# Week 6 Documentation & Capstone Navigation Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-6-planning-control]  

---

## 1. Controller Parameters & Trajectory Specifications

| Parameter | Implemented Value | Units | Purpose / Engineering Effect |
| :--- | :--- | :--- | :--- |
| **Lookahead Distance ($L_d$)** | [e.g. 1.2] | meters | Higher = smoother path, cuts corners; Lower = tighter tracking, prone to oscillation |
| **Target Linear Speed ($v$)** | [e.g. 0.8] | m/s | Forward cruising speed along trajectory |
| **Max Angular Velocity ($\omega_{max}$)**| [e.g. 1.5] | rad/s | Safety clamp preventing uncontrolled spinning |
| **Reference Path Topic** | `/plan` | — | Target trajectory waypoints (`nav_msgs/Path`) |
| **Vehicle Feedback Topic** | `/odom` | — | Current vehicle pose & speed (`nav_msgs/Odometry`) |
| **Output Actuation Topic** | `/cmd_vel` | — | Velocity steering command (`geometry_msgs/Twist`) |

---

## 2. Verification Evidence & Controller Logs

### 2.1 Autonomous Navigation Screenshot / Video Link
Embed or link your verification evidence of the autonomous run around the arena:
`![Week 6 Autonomous Run](capstone_autonomous_navigation.png)`  
`[Demo Video Link](https://...)`

### 2.2 Live Velocity Steering Output (`/cmd_vel`)
Paste a terminal log snippet of `ros2 topic echo /cmd_vel` while cornering:
```text
[Paste /cmd_vel terminal logs here]
```

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: Vehicle spun violently in place at path start* | *Unclamped angular curvature caused huge angular.z* | *Clamped angular velocity to +/- 1.5 rad/s* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Final Onboarding Technical Defense Preparation

Be ready to explain the following questions in your final 15-minute graduation checkpoint:

1. **How does changing the lookahead distance ($L_d$) in Pure Pursuit affect vehicle stability, path tracking error, and corner cutting?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **What is the difference in responsibility between the Global Planner (e.g. A*) and the Local Controller (e.g. Pure Pursuit or MPPI)?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **Walk through the full autonomous pipeline from sensor inputs to motor commands: how do LiDAR/Camera, Odometry, SLAM, Costmaps, and Controllers interact to drive the car or rover?**  
   [Write a brief summary to practice your defense]
