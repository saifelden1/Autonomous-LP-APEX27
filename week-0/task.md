# Week 0 Task: Environment Verification & Smoke Test

## 🎯 Objective
Verify that your Linux, Git, Docker, and ROS 2 environment is operational and ready for robotics development.

---

## 🛠️ Step-by-Step Instructions

1. **Clone or Fork the Repository**:
   ```bash
   git clone https://github.com/saifelden1/Autonomous-Systems-LP.git
   cd Autonomous-Systems-LP
   ```
2. **Start the Environment**:
   * *If using Docker*:
     ```bash
     cd docker
     # Linux:
     ./run_docker.sh
     # Windows:
     run_docker.bat
     ```
   * *If using native Ubuntu*:
     ```bash
     source /opt/ros/humble/setup.bash
     ```
3. **Execute the Smoke Test Commands**:
   ```bash
   ros2 --help
   ros2 topic list
   git --version
   ```

---

## ✅ Pass / Fail Deliverable

Take a screenshot showing:
1. Terminal running `ros2 --help` without errors.
2. Terminal showing `git status` on your working branch.

Submit this screenshot in your Week 0 Pull Request!
