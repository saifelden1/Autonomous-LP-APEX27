# Week 3 Documentation & Gazebo Arena Verification Report

**Candidate Name**: [Your Name]  
**Subsystem Preference**: [Formula Student AI / ERC Mars Rover]  
**Submission Date**: YYYY-MM-DD  
**Personal Working Branch**: [e.g. candidate/week-3-gazebo-sensors-world]  

---

## 1. Simulation Physics & World Specifications

| Parameter | Implemented Specification |
| :--- | :--- |
| **Arena Dimensions** | 10.0m x 10.0m |
| **Wall Dimensions (L x W x H)** | [e.g. 10.0m x 0.2m x 1.0m] |
| **Physics Solver** | ODE (Open Dynamics Engine) |
| **Max Step Size** | 0.001s (1 kHz rate) |
| **Real Time Update Rate** | 1000 Hz |
| **Average Real Time Factor (RTF)** | [e.g. 0.98 - 1.00] |

---

## 2. Verification Screenshots & Physics Evidence

### 2.1 Gazebo Arena Screenshot
Embed or link your screenshot showing Gazebo running with `apex_arena.world` loaded:
`![Week 3 Gazebo Arena](gazebo_arena_verification.png)`

### 2.2 Simulation Launch Terminal Logs
Paste the terminal snippet showing clean launch without shared library or plugin crashes:
```text
[Paste terminal launch output here]
```

---

## 3. Debugging & AI Hallucination Log

Document at least one issue or AI mistake encountered and how you fixed it.

| Issue Encountered | Root Cause | Solution & Fix |
| :--- | :--- | :--- |
| *Example: Gazebo opened with totally black screen* | *Missing SDF sun model* | *Added `<include><uri>model://sun</uri></include>` to apex_arena.world* |
| [Issue 1] | [Cause] | [Fix] |
| [Issue 2] | [Cause] | [Fix] |

---

## 4. Technical Defense Preparation

Be ready to explain the following questions in your 10-minute 1-on-1 mentor checkpoint:

1. **Why do we configure Gazebo physics to a 0.001s step size (1 kHz) for robotics rather than a larger step size like 0.05s?**  
   [Write a 2-3 sentence explanation to practice your defense]

2. **What is the difference between visual meshes and collision geometries in simulation? Why should collision geometry be simplified?**  
   [Write a 2-3 sentence explanation to practice your defense]

3. **In Formula AI and Mars Rover development, what is the role of a digital twin simulation environment before testing physical hardware?**  
   [Write a 2-3 sentence explanation to practice your defense]
