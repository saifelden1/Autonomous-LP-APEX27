# Week 2: AI Prompting Guide & Comprehension Protocol

This week involves compiling custom C++ / CMake interfaces and running asynchronous Action servers in Python.

---

## 1. Prompt Templates for Week 2

### Prompt 1: Handling Action Server Cancellation Gracefully
> "I am writing a ROS 2 Humble Action Server in Python using `rclpy.action.ActionServer`.
> When executing a long-running goal loop, how do I check if the client requested a cancellation (`goal_handle.is_cancel_requested`)? How do I properly transition the goal state to `canceled` instead of `succeeded` or `aborted`? Provide an idiomatic code snippet."

### Prompt 2: Debugging CMake Interface Compilation
> "I created a custom interface package `apex_mission_interfaces` containing `.action` and `.srv` files. When running `colcon build`, I get:
> `Could not find a package configuration file provided by "rosidl_default_generators"`
> Explain what dependencies are required in `CMakeLists.txt` and `package.xml` for custom ROS 2 message generation."

### Prompt 3: Writing Parameter-Driven Launch Files
> "How do I write a ROS 2 Python launch file that loads parameters from a YAML file (`config/mission_params.yaml`) while also allowing the user to override individual arguments from the CLI?"

---

## 2. Common Beginner Pitfalls

1. **Building Interfaces in Python Packages**: Custom messages/actions cannot be built in a pure `ament_python` package; they must reside in an `ament_cmake` package.
2. **Synchronous Service Deadlocks**: Calling a service synchronously (`client.call(request)`) inside a single-threaded node callback causes an immediate deadlock because the executor cannot process the incoming response.
3. **Forgetting `execute_callback` Decorator/Handling**: Action execution should run in a reentrant callback group or multi-threaded executor so cancel requests can be processed concurrently while the goal is running.

---

## 3. Self-Check Comprehension Gate

1. Why do `.action` files require three sections separated by `---`?
2. What is the difference between an Action **Goal**, **Feedback**, and **Result**?
3. How does `ros2 action send_goal` report feedback in real-time on the terminal?
