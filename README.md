# APEX Autonomous Systems: 6-Week Onboarding Sprint
## From Zero to Autonomous Robotics for Formula Student AI & ERC 27

Welcome to the **APEX Autonomous Systems** onboarding repository! This program is designed to take recruits from **absolute zero** (no prior robotics or ROS knowledge) to building full simulation-ready autonomous vehicle pipelines in **6 weeks**.

---

## 🎯 Program Mission & Track Integration

Candidates choose or cross-train across our two primary international competition tracks:
1. **Formula Student Driverless (Formula AI)**: High-speed path tracking, cone perception (yellow/blue), state estimation, and dynamic vehicle control.
2. **European Rover Challenge (ERC 27)**: Mars Yard terrain navigation, 3D obstacle pointcloud clustering, ArUco visual fiducial tracking, and terrain mapping.

This sprint is **AI-Augmented**: You will use AI (ChatGPT, Claude, Antigravity) as your senior engineering mentor. You do not wait for lectures—you engineer, prompt, debug, simulate, and defend your work.

---

## 📅 6-Week Master Syllabus

| Week | Branch | Core Concepts | Hands-On Project | Competition Link |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [`week-1-ros2-basics`](../../tree/week-1-ros2-basics) | Linux Bash CLI, ROS 2 Architecture, Nodes, Pub/Sub, QoS Profiles | **Rover/Car Telemetry Heartbeat & Safety Watchdog** | Vehicle health monitoring & CAN telemetry bridge |
| **2** | [`week-2-interfaces-actions`](../../tree/week-2-interfaces-actions) | Custom `.msg`/`.srv`/`.action`, Node Parameters, Python Launch Systems | **Mission State Machine & Cancelable E-Stop Server** | Autonomous state machine (AS Off / Ready / Driving / Emergency) |
| **3** | [`week-3-urdf-tf2`](../../tree/week-3-urdf-tf2) | REP-105 Coordinate standard, URDF/Xacro robot kinematics, TF2 dynamic broadcasting | **From-Scratch 4-Wheel Autonomous Chassis in RViz** | Coordinate frames for sensors, chassis, and world |
| **4** | [`week-4-gazebo-sensors`](../../tree/week-4-gazebo-sensors) | Gazebo Sim physics, Skid-Steer / Ackermann plugins, LiDAR & Camera sensor bridges | **Simulation Arena Spawn & Laser Emergency Braking Node** | Autonomous virtual testing & collision prevention |
| **5** | [`week-5-perception`](../../tree/week-5-perception) | OpenCV `cv_bridge`, Color segmentation, Pointcloud clustering, 3D Marker visualizers | **Formula Cone Detector / ERC ArUco Pose Estimator** | Track boundary detection & waypoint visual localization |
| **6** | [`week-6-localization-control`](../../tree/week-6-localization-control) | Robot Localization EKF (IMU + Odom), Pure Pursuit path follower, Nav2 architecture | **Autonomous Slalom & Waypoint Capstone Challenge** | Complete autonomous driving around track/obstacles |

---

## 🚀 Environment Setup

You can run the environment in **Docker (Recommended for Windows/Mac/Linux)** or **Natively on Ubuntu 22.04 LTS (Jammy)**.

### Option A: Docker (Zero-Install Configuration)
Ensure [Docker Desktop](https://www.docker.com/products/docker-desktop/) is installed and running.
```bash
# Clone the repository
git clone https://github.com/saifelden1/Autonomous-Systems-LP.git
cd Autonomous-Systems-LP/docker

# On Linux:
chmod +x run_docker.sh
./run_docker.sh

# On Windows (Command Prompt / PowerShell):
run_docker.bat
```

### Option B: Ubuntu Native (ROS 2 Humble Desktop)
```bash
# Source ROS 2 underlay
source /opt/ros/humble/setup.bash

# Install dependencies
sudo apt-get update && sudo apt-get install -y \
  python3-colcon-common-extensions \
  ros-humble-joint-state-publisher-gui \
  ros-humble-xacro \
  ros-humble-tf2-tools \
  ros-humble-gazebo-ros-pkgs \
  ros-humble-cv-bridge \
  ros-humble-vision-msgs \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-robot-localization
```

---

## 📜 How to Study Each Week

1. **Switch to the weekly branch**:
   ```bash
   git checkout week-1-ros2-basics
   ```
2. **Read the Theory**: Open `README.md` on that branch for the complete concept walkthrough.
3. **Read the AI Guide**: Open `ai_prompting_guide.md` to see the exact prompt templates and anti-patterns.
4. **Implement the Project**: Open `task.md` for project requirements, topic contracts, and pass/fail criteria. Complete code in `template_ws/`.
5. **Verify**: Run the automated test commands in `task.md` and record a 60-second video of your terminal + RViz/Gazebo.
6. **Submit**: Open a Pull Request following [`docs/submission_guidelines.md`](docs/submission_guidelines.md).

---

## 📚 Essential Developer Guides
* [AI Pair-Programming Charter](docs/ai_pair_programming_charter.md) — How to use AI effectively without failing technical reviews.
* [ROS 2 CLI Cheatsheet](docs/ros2_cheatsheet.md) — Daily command-line reference.
* [Submission & Grading Guidelines](docs/submission_guidelines.md) — Video proof and PR guidelines.
