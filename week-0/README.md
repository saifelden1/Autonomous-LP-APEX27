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
| `source <file>` | Loads environment settings into the current shell session | `source /opt/ros/humble/setup.bash` |
| `chmod +x <file>` | Grants executable permissions to a script | `chmod +x run_docker.sh` |
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
git commit -m "feat(setup): verify environment and docker run"
git push -u origin your-name/week-0-setup
```

---

## 3. Why Docker in Robotics?

Installing ROS 2 natively on Windows or macOS can be extremely difficult due to missing Linux kernel drivers and incompatible libraries.
**Docker** packages the entire Ubuntu OS, ROS 2 Humble/Jazzy, Gazebo, and RViz into a pre-configured sandbox that runs identically on any computer.

To launch the provided container:
```bash
cd docker
# On Linux:
chmod +x run_docker.sh
./run_docker.sh

# On Windows:
run_docker.bat
```

---

## 4. Official ROS 2 Installation Steps & Useful Links

If you prefer installing natively on Ubuntu instead of Docker:
* **Ubuntu 22.04 LTS (Jammy)**: Install **ROS 2 Humble Hawksbill** ([Official Guide](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)).
* **Ubuntu 24.04 LTS (Noble)**: Install **ROS 2 Jazzy Jalisco** ([Official Guide](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debians.html)).

### Recommended Tools:
* **VS Code**: Install with extensions `Python`, `C/C++`, `ROS`, and `Docker`.
* **Terminator**: A terminal multiplexer that allows splitting your window into multiple panes (`sudo apt install -y terminator`).

---

## 5. Curated Open-Source Video Resources

* **Linux CLI**: [Linux Command Line for Beginners (NetworkChuck)](https://www.youtube.com/watch?v=s3ii48qYBxA)
* **Git & GitHub**: [Git & GitHub Tutorial for Beginners (Corey Schafer)](https://www.youtube.com/watch?v=mAFoROnOfHs)
* **Docker**: [Docker Container Fundamentals (TechWorld with Nana)](https://www.youtube.com/watch?v=pg19Z8LLKh8)

---

## 📋 Week 0 Assignment & Deliverables

Follow the step-by-step instructions in [task.md](task.md) and document your results in [Template_Report.md](Template_Report.md) for your Saturday PR submission.

