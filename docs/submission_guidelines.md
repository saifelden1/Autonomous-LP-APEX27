# Weekly Submission & Verification Guidelines

To pass each week of the APEX Autonomous Systems Learning Phase, every candidate must submit a Pull Request (PR) from their weekly working branch back into `main`.

---

## 1. Pull Request Structure

Each candidate must name their branch:
`<your-github-username>/week-<number>-<project-name>`  
Example: `john_doe/week-1-telemetry-watchdog`

Your Pull Request description must follow this exact template:

```markdown
### Milestone Summary
- Week Completed: [Week 1 / Week 2 / ... / Week 6]
- Track Focus: [Formula AI / ERC 27 / Core Foundation]

### Implemented Architecture
- Nodes Created:
  - `<node_1_name>`: [Role & responsibilities]
  - `<node_2_name>`: [Role & responsibilities]
- Topics & Interfaces:
  - Subscribed: `/example/input` (`type`)
  - Published: `/example/output` (`type`)

### Verification Proof
- [ ] Colcon build clean with zero warnings
- [ ] Unit tests / Lint checks passed
- Attached Video / GIF: [Link or embedded 60-second screen capture demonstrating Gazebo / RViz / Terminal pass criteria]

### AI Prompt Audit Log
1. **Initial Scaffold Prompt**: [The exact prompt you used to generate the skeleton]
2. **Key Blocker Encountered**: [What error or bug occurred during simulation?]
3. **Debugging Prompt Used**: [How did you prompt the AI to explain and resolve the issue?]
4. **Takeaway Learned**: [What ROS 2 architectural concept did you learn from this fix?]
```

---

## 2. Capturing Verification Proof

1. **Video Proof**:
   - Must be between 30 and 60 seconds.
   - Screen layout should show terminal execution side-by-side with RViz or Gazebo.
   - Show terminal command starting the launch file, robot reacting, and terminal echo confirming topic data.
2. **Acceptable Recorders**:
   - Ubuntu: `SimpleScreenRecorder`, `Kazam`, or `OBS Studio`.
   - Windows (WSL2): Xbox Game Bar (`Win + Alt + R`) or `OBS Studio`.

---

## 3. Evaluation Rubric (100 Points Total)

| Criterion | Points | Description |
| :--- | :--- | :--- |
| **Functional Correctness** | 40 | System meets all pass/fail topic contracts and simulation behavior. |
| **Code Quality & ROS Standards** | 25 | Proper namespace, clean parameters, no blocking sleeps, clean package structure. |
| **AI Prompting Audit & Understanding** | 20 | Candidate demonstrates full comprehension of generated code and effective AI prompting. |
| **Documentation & PR Clarity** | 15 | Clear PR description, reproducible launch instructions, and complete video proof. |
