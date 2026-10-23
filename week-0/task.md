# Week 0 Task: Environment Verification & Smoke Test

## 🎯 Objective
Configure and verify your workstation with Ubuntu 24.04 LTS (Dual-Boot or Docker sandbox), Git/GitHub version control, ROS 2 Jazzy, and Gazebo runtime readiness.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — OS & Toolchain Setup (1.5 hrs)
1. **Choose your setup mode**:
   * **Preferred (Native Linux)**: Follow the [Ubuntu 24.04 Dual Boot Guide](https://www.youtube.com/watch?v=F0fM3f5Lw-Y) to install Ubuntu 24.04 alongside Windows 11.
   * **Alternative (Docker)**: Install Docker Desktop on Windows.
2. Watch open-source tutorials:
   * [Git & GitHub Tutorial for Beginners](https://www.youtube.com/watch?v=mAFoROnOfHs) (Corey Schafer)
   * [Docker Container Fundamentals](https://www.youtube.com/watch?v=pg19Z8LLKh8) (TechWorld with Nana)
3. Clone repository and create a personal working branch:
   ```bash
   git clone https://github.com/saifelden1/Autonomous-LP-APEX27.git
   cd Autonomous-LP-APEX27
   git checkout -b your-name/week-0-setup
   ```

### Day 2 (Wed) — Linux Terminal Primitives (1.0 hr)
1. Study and execute core Linux CLI navigation:
   * [Linux Command Line for Beginners](https://www.youtube.com/watch?v=s3ii48qYBxA) (NetworkChuck)
2. Practice running essential terminal commands inside bash:
   ```bash
   pwd
   ls -la
   mkdir -p test_ws/src
   echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
   ```

### Day 3 (Fri) — Dependency Installation & Smoke Test (1.5 hrs)
1. **If on Native Ubuntu 24.04**:
   Run the 1-click automated installer script:
   ```bash
   chmod +x install_dependencies.sh
   ./install_dependencies.sh
   ```
2. **If using Docker sandbox**:
   * Windows: Run `docker\run_docker.bat`
   * Linux: `chmod +x docker/run_docker.sh && ./docker/run_docker.sh`
3. Execute ROS 2 smoke test commands:
   ```bash
   ros2 --help
   ros2 topic list
   git --version
   ```
4. Verify that zero command errors occur.

### Day 4 (Sat) — Report Submission & Defense Prep (1.0 hr)
1. Capture required verification screenshots:
   * `git status` showing your active branch.
   * Terminal executing `ros2 --help` and `ros2 topic list`.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push changes:
   ```bash
   git add week-0/Template_Report.md
   git commit -m "docs(week-0): complete environment verification report"
   git push -u origin your-name/week-0-setup
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Review the 3 oral defense questions for Sunday's 10-minute checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

- [ ] Working branch named `<name>/week-0-setup` created and pushed to GitHub.
- [ ] Screenshot of `ros2 --help` without errors attached.
- [ ] Screenshot of `git status` attached.
- [ ] [Template_Report.md](Template_Report.md) fully filled out with debugging log and defense prep answers.
