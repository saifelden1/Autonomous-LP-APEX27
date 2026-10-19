# Week 0 Documentation & Environment Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-0-setup]  

---

## 1. Workstation & Environment Specifications

| Component | Selected Specification |
| :--- | :--- |
| **Host Operating System** | [e.g. Windows 11 Home / Ubuntu 22.04 LTS / macOS Sonoma] |
| **Setup Mode** | [Docker Sandbox (run_docker.bat) / Native Ubuntu Dual-Boot / WSL2] |
| **ROS 2 Distribution** | [ROS 2 Humble Hawksbill / ROS 2 Jazzy Jalisco] |
| **Docker Desktop Version** | [e.g. v4.28.0 or N/A] |
| **Editor / IDE** | [VS Code / Cursor / PyCharm] |

---

## 2. Environment Verification Logs & Evidence

### 2.1 Git Branch Status
Provide the terminal output demonstrating your branch setup:
```bash
git status
```
*Paste your output below:*
```text
[Paste terminal text here]
```

### 2.2 ROS 2 Core Smoke Test
Execute inside your ROS 2 environment:
```bash
ros2 --help
ros2 topic list
```
*Paste your output below:*
```text
[Paste terminal text here]
```

### 2.3 Verification Screenshot
Embed or link your verification screenshot showing the terminal output running the smoke test commands:
`![Week 0 Smoke Test Screenshot](smoke_test_verification.png)`

---

## 3. Debugging & Troubleshooting Log

Document at least one issue or unexpected behavior encountered during installation/setup and how you fixed it.

| Issue Encountered | Root Cause | Diagnosis & Solution |
| :--- | :--- | :--- |
| *Example: Docker daemon not running error on Windows* | *Docker Desktop service was closed* | *Started Docker Desktop app from Start Menu and enabled WSL2 integration* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. AI Interaction & Policy Reflection

> [!NOTE]
> AI tools (ChatGPT, Claude, Gemini) are permitted. Submitting unverified AI-generated content is disqualified.

1. **What AI tool(s) did you consult during this week's setup, and what specific queries did you ask?**  
   [Your response here]

2. **Did the AI suggest any outdated or invalid commands (e.g. ROS 1 `roscore` or wrong distro package names)? How did you verify the correct solution?**  
   [Your response here]

---

## 5. Oral Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **Why do professional autonomous racing and rover teams use Docker containers or standardized Ubuntu environments instead of running raw Windows binaries?**  
   [Write a brief 2-3 sentence answer to practice your defense]

2. **What does the command `source /opt/ros/humble/setup.bash` do inside your Linux shell session, and what happens if you forget to run it?**  
   [Write a brief 2-3 sentence answer to practice your defense]

3. **What is the difference between working on a dedicated Git branch versus committing directly to `main`?**  
   [Write a brief 2-3 sentence answer to practice your defense]
