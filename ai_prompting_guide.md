# Week 3: AI Prompting Guide & Comprehension Protocol

URDF and TF2 coordinate math are common areas where AI can generate subtle bugs like frame flips or unnormalized quaternions.

---

## 1. Prompt Templates for Week 3

### Prompt 1: Generating a Differential-Drive Xacro Macro
> "Write a modular Xacro macro for a robot wheel.
> Macro name: `wheel_macro`
> Parameters: `prefix`, `x_reflect`, `y_reflect`, `wheel_radius`, `wheel_width`, `wheel_mass`.
> Include visual cylinder geometry, collision cylinder geometry, and correct inertia calculations for a solid cylinder along the rotation axis (Y-axis). Provide the complete XML macro."

### Prompt 2: Writing a TF2 Transform Broadcaster in Python
> "Write a ROS 2 Humble node in Python named `OdomTFBroadcaster`.
> Requirements:
> 1. Use `tf2_ros.TransformBroadcaster(self)`.
> 2. Run a timer at 30 Hz simulating a robot driving in a circle with radius 2.0 meters at 0.5 rad/s.
> 3. Construct a `geometry_msgs/msg/TransformStamped` message with:
>    - `header.stamp = self.get_clock().now().to_msg()`
>    - `header.frame_id = 'odom'`
>    - `child_frame_id = 'base_link'`
> 4. Convert yaw angle $\theta$ to quaternion $(x, y, z, w)$ using mathematical formulas or `scipy.spatial.transform.Rotation`.
> Explain the coordinate convention of the quaternion."

### Prompt 3: Debugging Missing Frame Errors in RViz
> "In RViz, my robot model shows an error:
> `No transform from [camera_link] to [base_link]`
> How do I check if `robot_state_publisher` is receiving `/joint_states`? What diagnostic command can I run to see the entire active TF2 tree?"

---

## 2. Common Pitfalls to Avoid

* **Cylinder Orientation in URDF**: Cylinders in URDF default to aligning along the Z-axis. To make a wheel spin around the Y-axis, you must add an `<origin rpy="1.5708 0 0" xyz="0 0 0"/>` tag!
* **Non-Normalized Quaternions**: Setting quaternion $(0, 0, 0, 0)$ will cause RViz to throw an assertion failure. Quaternions must always satisfy $x^2 + y^2 + z^2 + w^2 = 1.0$.
* **Missing Root Link Dummy**: In ROS 2 / KDL, it is best practice to have a massless root link `base_link` connected via a fixed joint to the physical `chassis` link to avoid inertial warnings.
