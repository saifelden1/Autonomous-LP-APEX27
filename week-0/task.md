# Week 0 Task: Environment Verification & Smoke Test

## 🎯 Objective
Configure and verify your workstation with modern Linux tooling, Git/GitHub version control, Docker container isolation, and ROS 2 Humble/Jazzy runtime readiness.

---

## 📅 4-Day Operational Schedule

### Day 1 (Mon) — Git & Toolchain Setup (1.5 hrs)
1. Install **Git** and **Docker Desktop** (or set up Ubuntu 22.04 LTS native dual-boot / WSL2).
2. Curated Open-Source Tutorials:
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
   echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
   ```

### Day 3 (Fri) — Container Launch & Smoke Test (1.5 hrs)
1. Launch the APEX Autonomous Docker container:
   * **Windows**: Run `docker/run_docker.bat`
   * **Linux / Mac**: `chmod +x docker/run_docker.sh && ./docker/run_docker.sh`
2. Run the ROS 2 smoke test commands inside the container terminal:
   ```bash
   ros2 --help
   ros2 topic list
   git --version
   ```
3. Verify that zero command errors or display connection failures occur.

### Day 4 (Sat) — Report Submission & Oral Defense Prep (1.0 hr)
1. Capture required verification screenshots:
   * `git status` showing your active branch.
   * Container terminal executing `ros2 --help` and `ros2 topic list`.
2. Complete all sections of [Template_Report.md](Template_Report.md).
3. Commit and push changes:
   ```bash
   git add week-0/Template_Report.md
   git commit -m "docs(week-0): complete environment verification report"
   git push -u origin your-name/week-0-setup
   ```
4. Open a Pull Request on GitHub by Saturday 11:59 PM.
5. Prepare for your Sunday 10-minute technical defense checkpoint.

---

## ✅ Pass / Fail Deliverables Checklist

To receive full credit and advance to Week 1:
- [ ] Working branch named `<name>/week-0-setup` created and pushed to GitHub.
- [ ] High-resolution screenshot of `ros2 --help` without errors attached.
- [ ] High-resolution screenshot of `git status` attached.
- [ ] [Template_Report.md](Template_Report.md) fully filled out with debugging log and defense prep answers.
