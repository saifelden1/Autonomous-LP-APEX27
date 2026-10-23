# Week 0: Developer Environment, Linux CLI, Git & Docker

Welcome to **Week 0**! The goal of this week is simple: get your developer workstation configured with modern Linux, Git, Docker, and ROS 2 tooling without getting stuck.

---

## 1. Zero-to-One Linux Administration Primitives

Robotics software runs predominantly on Linux (Ubuntu). Master these essential commands:

| Command | What It Does | Practical Example |
| :--- | :--- | :--- |
| `pwd` | Displays current working directory | `pwd` |
| `cd <path>` | Changes current directory | `cd /workspace` |
| `ls -la` | Lists all files including hidden configurations | `ls -la` |
| `mkdir -p <dir>` | Creates a new directory and any parent folders | `mkdir -p ~/ros2_ws/src` |
| `source <file>` | Loads environment settings into the current shell session | `source /opt/ros/jazzy/setup.bash` |
| `chmod +x <file>` | Grants executable permissions to a script | `chmod +x install_dependencies.sh` |
| `export VAR=val` | Sets an environment variable | `export ROS_DOMAIN_ID=10` |

---

## 2. Git & GitHub: How Teams Collaborate

In APEX Autonomous Systems, we never edit code directly on `main`. Every feature has its own branch:

```bash
# 1. Clone the repository
git clone https://github.com/saifelden1/Autonomous-LP-APEX27.git
cd Autonomous-LP-APEX27

# 2. Create and switch to your personal task branch
git checkout -b your-name/week-0-setup

# 3. Stage changes, commit with clear message, and push
git add .
git commit -m "feat(setup): verify environment and ROS 2 smoke test"
git push -u origin your-name/week-0-setup
```

---

## 3. Recommended: 1-Click Native Ubuntu 24.04 Setup

If you are running **Ubuntu 24.04 LTS (Noble Numbat)** natively, we provide an automated installer script that configures ROS 2 Jazzy, Gazebo Harmonic, build tools, and python packages in one step:

```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

---

## 4. Alternative: Docker Container Sandbox (Zero-Install)

If you are on Windows or macOS and cannot dual-boot immediately, run our pre-configured Docker container:

```bash
cd docker
# On Linux:
chmod +x run_docker.sh && ./run_docker.sh

# On Windows:
run_docker.bat
```

---

## 5. Curated Open-Source Video Resources

* **Ubuntu 24.04 Dual Boot Guide**: [How to Dual Boot Ubuntu 24.04 LTS alongside Windows 11](https://www.youtube.com/watch?v=F0fM3f5Lw-Y) *(Learn Linux TV)*
* **Linux CLI**: [Linux Command Line for Beginners (NetworkChuck)](https://www.youtube.com/watch?v=s3ii48qYBxA) *(20 mins)*
* **Git & GitHub**: [Git & GitHub Tutorial for Beginners (Corey Schafer)](https://www.youtube.com/watch?v=mAFoROnOfHs) *(30 mins)*
* **Docker**: [Docker Container Fundamentals (TechWorld with Nana)](https://www.youtube.com/watch?v=pg19Z8LLKh8) *(25 mins)*

---

## ⚠️ Top 3 AI Hallucination Traps for Week 0

When asking AI (ChatGPT/Claude) for setup assistance, watch out for these 3 common hallucinations:

1. **Version Mismatch Hallucination**: AI frequently attempts to install ROS 2 Humble on Ubuntu 24.04 (Ubuntu 24.04 uses **ROS 2 Jazzy**, while 22.04 uses **Humble**). Always verify your Ubuntu version before following AI installation steps.
2. **Missing GUI Desktop Dependencies**: AI often recommends installing `ros-jazzy-ros-base`, which leaves out RViz2, Gazebo, and GUI tools. Always use `ros-jazzy-desktop`.
3. **Docker GUI Display Blindness**: AI will suggest a standard `docker run -it ubuntu bash` command without GUI forwarding flags (`-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY`). Use our ready-made scripts in `docker/`!

---

## 📋 Week 0 Assignment & Deliverables

Follow the step-by-step instructions in [task.md](task.md) and document your results in [Template_Report.md](Template_Report.md) for your Saturday PR submission.
