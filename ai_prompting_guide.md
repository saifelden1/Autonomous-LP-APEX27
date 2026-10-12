# Week 6: AI Prompting Guide & Comprehension Protocol

Pure Pursuit controller tuning requires careful mathematical handling of angle normalization and lookahead search.

---

## 1. Prompt Templates for Week 6

### Prompt 1: Pure Pursuit Target Search
> "Write a Python function for Pure Pursuit path tracking:
> Inputs: Current vehicle position $(x, y)$, current heading $\theta$, target path (list of $(x_i, y_i)$ waypoints), lookahead distance $L_d$.
> Task: Search the path sequentially forward from the closest waypoint to find the first point whose distance is $\ge L_d$.
> Return the target $(g_x, g_y)$ point."

### Prompt 2: Angle Normalization & Curvature Calculation
> "Explain how to calculate the Pure Pursuit steering curvature $\kappa = 2 \cdot \sin(\alpha) / L_d$.
> Why must the angle difference $\alpha = \text{target\_angle} - \text{vehicle\_heading}$ be normalized to $[-\pi, \pi]$?
> What happens if angle normalization is omitted when crossing the $\pm \pi$ discontinuity?"

### Prompt 3: Tuning Controller Stability
> "My vehicle is violently oscillating (snaking) left and right as it tries to track the path.
> Explain how changing the lookahead distance $L_d$ and linear velocity $v$ affects controller damping and tracking error."

---

## 2. Controller Tuning Rules of Thumb

* **If vehicle oscillates wildly (over-steering)**: Increase $L_d$ (makes the path smoother and more stable, like looking further down the road).
* **If vehicle cuts corners (under-steering)**: Decrease $L_d$ (tracks sharp turns closer, but increases risk of oscillation).
* **Typical Starting Values**: $L_d = 0.8\text{m} - 1.2\text{m}$ for slow rovers; $L_d = 2.0\text{m} - 4.0\text{m}$ for race cars.
