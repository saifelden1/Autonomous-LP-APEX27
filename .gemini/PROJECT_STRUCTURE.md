# Apex Racing Team — Autonomous Systems Onboarding Repository Structure

## Overview
This repository contains the 7-week training track for the Apex Racing Team Autonomous Systems division (Formula Student AI & ERC 27 Mars Rover).
It is structured for progressive hands-on mastery of ROS 2, URDF robot modeling, Gazebo physics simulation, perception, and path planning.

## Master Plan & Tracking
* `Apex_Autonomous_7Week_Plan.xlsx`: Master syllabus and 7 daily operations sheets with 4-day active schedules and curated video links.

## Branch & Directory Layout (Option B)
```
Autonomous-Systems-LP/
├── .gemini/
│   └── PROJECT_STRUCTURE.md     # AI context and directory navigation
├── docker/                      # Zero-install Docker environment
│   ├── Dockerfile               # ROS 2 Humble + Gazebo + RViz desktop
│   ├── docker-compose.yml
│   ├── run_docker.bat           # Windows container launcher
│   └── run_docker.sh            # Linux container launcher
├── docs/                        # Global reference documentation
│   ├── ai_pair_programming_charter.md
│   ├── ros2_cheatsheet.md
│   └── submission_guidelines.md
├── week-0/                      # Week 0: Linux CLI, Git & Docker Setup
│   ├── README.md                # Reading guide, CLI cheatsheet, video links
│   ├── task.md                  # 4-day task instructions & smoke test
│   └── Template_Report.md       # Submission report & defense prep
├── week-1/                      # Week 1: ROS 2 Basics & Pub/Sub
│   ├── README.md
│   ├── task.md
│   ├── ai_prompting_guide.md
│   ├── Template_Report.md
│   └── template_ws/src/apex_telemetry/
├── week-2/                      # Week 2: URDF, TF Trees & RViz2
│   └── template_ws/src/apex_robot_description/
├── week-3/                      # Week 3: Gazebo Arena & Sensor Plugins
│   └── template_ws/src/apex_gazebo_worlds/
├── week-4/                      # Week 4: Simulation-to-RViz Bridge & Teleop
│   └── template_ws/src/apex_simulation/
├── week-5/                      # Week 5: Perception & Landmark Markers
│   └── template_ws/src/apex_perception/
├── week-6/                      # Week 6: Path Planning & Pure Pursuit Control
│   └── template_ws/src/apex_navigation/
└── README.md                    # Master curriculum roadmap & quick start
```
