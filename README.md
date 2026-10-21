# APEX Autonomous Systems: 7-Week Onboarding Sprint (Week 0 – 6)
## Exposure to Autonomous Systems & ROS 2 for Formula Student AI & ERC 27

Welcome to **APEX Autonomous Systems**! This onboarding program is designed to give beginners **practical exposure and fundamental knowledge** of the modern ROS 2 autonomous robotics pipeline without overwhelming them with unnecessary complexity.

---

## 🎯 Track Relevance

Candidates build foundational awareness for our two competition tracks:
1. **Formula Student Driverless (Formula AI)**: High-speed autonomous race cars, cone perception, odometry, path tracking, and vehicle control.
2. **European Rover Challenge (ERC 27)**: Mars Yard planetary rovers, 3D terrain navigation, sensor fusion, obstacle detection, and mapping.

---

## 📅 7-Week Curriculum Roadmap

| Week | Branch | Core Concepts | Hands-On Project |
| :---: | :--- | :--- | :--- |
| **0** | [`week-0-git-docker-linux`](../../tree/week-0-git-docker-linux) | Linux CLI basics, Git/GitHub workflow, Docker container setup, ROS 2 install steps & links | **Developer Environment Setup & ROS 2 Smoke Test** |
| **1** | [`week-1-ros2-basics`](../../tree/week-1-ros2-basics) | `colcon build`, ROS 2 architecture, Publisher & Subscriber nodes in Python, Launch files | **Telemetry Heartbeat & `rqt_graph` Node Inspection** |
| **2** | [`week-2-urdf-tf-rviz`](../../tree/week-2-urdf-tf-rviz) | URDF & Xacro modeling, Coordinate frames, REP-105 TF tree, RViz2 visual inspection | **4-Wheel Vehicle Model & RViz TF Inspection** |
| **3** | [`week-3-gazebo-sensors-world`](../../tree/week-3-gazebo-sensors-world) | Gazebo physics, custom world creation, sensor physics (LiDAR, Camera, IMU, Encoders) | **Custom Arena Creation & Sensor Plugin Attachment** |
| **4** | [`week-4-simulation-rviz-bridge`](../../tree/week-4-simulation-rviz-bridge) | Model deployment in Gazebo, sensor streams into RViz (LaserScan, Images), `rqt_graph` | **Driving Rover in World & Live RViz Sensor Visualization** |
| **5** | [`week-5-perception-slam`](../../tree/week-5-perception-slam) | Perception & SLAM fundamentals: types (2D/3D SLAM), cone/ArUco detection, sensor/topic contracts | **Simulated SLAM Mapping & Landmark Detection Exploration** |
| **6** | [`week-6-planning-control`](../../tree/week-6-planning-control) | Path planning & control fundamentals: Nav2 costmaps, Global Planners, Pure Pursuit, `/cmd_vel` | **Autonomous Navigation to Goal Marker in Simulation** |

---

## 📊 Master Onboarding Plan & Daily Schedule

All daily schedules, curated open-source videos, and candidate milestones are organized in:
* **Master Online Syllabus & Daily Schedule**: [Apex Autonomous Systems — 7-Week Plan (Google Sheets)](https://docs.google.com/spreadsheets/d/1_--5qcV5tGVSPDrbM6lix-A-b456UNzBtC8ZENiewVs/edit)
* **Weekly Cadence (4 Active Days / Week)**:
  * **Day 1 (Mon)**: Core Theory & Curated YouTube Links (1.5 hrs)
  * **Day 2 (Wed)**: AI-Assisted Implementation Lab (2.0 hrs)
  * **Day 3 (Fri)**: Simulation & Sensor Testing (1.5 hrs)
  * **Day 4 (Sat)**: Deliverable Report & Pull Request (1.0 hr)
  * *(Sun: 10-min Oral Code Defense; Tue & Thu: Buffer/Flex)*

---

## 🛠️ Quick Start (Zero-Friction Setup)

### Step 1: Clone Repository
```bash
git clone https://github.com/saifelden1/Autonomous-Systems-LP.git
cd Autonomous-Systems-LP
```

### Step 2: Start Container Environment
* **On Windows (Double-click or run in PowerShell/CMD)**:
  ```cmd
  docker\run_docker.bat
  ```
* **On Linux / Ubuntu**:
  ```bash
  chmod +x docker/run_docker.sh && ./docker/run_docker.sh
  ```

*(If developing natively on Ubuntu 22.04 LTS: simply run `source /opt/ros/humble/setup.bash`)*

---

## ⚠️ The "Top 3 AI Hallucination Traps" Rule

Each week includes a dedicated **Top 3 AI Hallucination Traps** section warning you of the exact mistakes AI tools (ChatGPT, Claude) make for that topic (e.g. giving ROS 1 `roscore` commands, swapping TF frames, or using obsolete Gazebo plugins). Check that section before running any AI code!

