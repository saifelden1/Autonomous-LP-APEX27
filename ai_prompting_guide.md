# Week 5: AI Prompting Guide & Comprehension Protocol

Computer vision involves pixel-to-metric conversions, camera intrinsic projection matrices, and color thresholding.

---

## 1. Prompt Templates for Week 5

### Prompt 1: OpenCV to ROS 2 Image Conversion
> "Write a clean ROS 2 subscriber callback in Python that receives `sensor_msgs/msg/Image`.
> Use `cv_bridge.CvBridge()` to convert the image to an OpenCV BGR numpy array safely.
> Add proper error handling for `CvBridgeError`.
> Convert the processed annotated image back to `sensor_msgs/msg/Image` and publish to `/perception/debug_image`."

### Prompt 2: Camera Intrinsic Projection Math (Pinhole Model)
> "Explain how the Pinhole Camera Model uses focal length $(f_x, f_y)$ and principal point $(c_x, c_y)$ from `sensor_msgs/msg/CameraInfo` to project a 2D pixel coordinate $(u, v)$ with known depth $Z$ into 3D metric coordinates $(X, Y, Z)$ in `camera_optical_frame`.
> Provide the mathematical formula and a Python function."

### Prompt 3: Building a `visualization_msgs/MarkerArray`
> "Write a Python function to create a `visualization_msgs/msg/MarkerArray` containing 3D cylinders representing detected track cones in RViz.
> Cones on the left must have color Blue (`rgba = 0.0, 0.2, 1.0, 1.0`), and cones on the right must have color Yellow (`rgba = 1.0, 1.0, 0.0, 1.0`).
> Ensure frame_id is set to `camera_optical_frame` and `action = Marker.ADD`."

---

## 2. Common Vision Traps

* **Color Space Confusion**: OpenCV reads images in **BGR**, whereas standard image libraries (PIL, Matplotlib) use **RGB**. Converting directly without checking will swap blue and red channels.
* **Pixel Coordinate Inversion**: In image arrays, `image[y, x]` corresponds to row $y$ (vertical) and column $x$ (horizontal). Inverting rows and columns causes incorrect centroid math.
* **Marker Overwrite (ID Collision)**: Every marker in a `MarkerArray` must have a **unique integer `id`**. If two markers share the same ID, RViz will only draw the last one.
