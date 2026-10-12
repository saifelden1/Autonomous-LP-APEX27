# Week 5 Project: Target Detection & RViz 3D Marker Broadcaster

## 🎯 Objective
In this project, you will build a computer vision perception node for your chosen competition track (Formula Student AI or ERC 27):

* **Formula Student Track**: Detect Yellow and Blue track cones from an image feed, calculate their 3D coordinates relative to `camera_optical_frame`, and publish them as colored cylinders in a `visualization_msgs/msg/MarkerArray`.
* **ERC 27 Track**: Detect ArUco fiducial markers (Dictionary 4x4) or obstacle clusters, estimate their 3D position, and publish them as 3D visual markers in RViz.

The package includes a synthetic image publisher `synthetic_camera_publisher.py` that generates realistic camera frames with simulated cones and ArUco tags so you can develop and test immediately without needing physical cameras or complex Gazebo worlds.

---

## 📐 System Pipeline

```
+------------------------------------+
|     synthetic_camera_publisher     |
| publishes: /camera/color/image_raw |
+------------------------------------+
                  │
                  ▼
+------------------------------------+
|          cone_detector_node        |
|  1. Convert to OpenCV (cv_bridge)  |
|  2. HSV thresholding & contours    |
|  3. Approximate 3D position        |
|  4. Annotate debug image           |
+------------------------------------+
        │                      │
        ▼                      ▼
/perception/debug_image    /perception/cone_markers
(sensor_msgs/Image)        (visualization_msgs/MarkerArray)
[View in rqt_image_view]   [View in RViz2 3D Grid]
```

---

## 🛠️ Step-by-Step Instructions

### Step 1: Inspect the Starter Package
Navigate to `week-5/template_ws`:
```bash
cd template_ws
colcon build --symlink-install
source install/setup.bash
```

### Step 2: Implement `cone_detector.py`
* File: `apex_perception/apex_perception/cone_detector.py`
* Subscriptions:
  * `/camera/color/image_raw` (`sensor_msgs/msg/Image`)
* Publications:
  * `/perception/debug_image` (`sensor_msgs/msg/Image`): Image annotated with bounding boxes and centroid circles.
  * `/perception/cone_markers` (`visualization_msgs/msg/MarkerArray`): 3D visual cylinders.
* Processing:
  * Use `CvBridge().imgmsg_to_cv2(msg, desired_encoding='bgr8')`.
  * Segment Yellow cones ($H \in [20, 35]$) and Blue cones ($H \in [100, 130]$).
  * Filter contours by area ($> 100$ pixels).
  * Estimate $(X, Y, Z)$ using simple pinhole projection with assumed cone physical height $H_{\text{real}} = 0.3$ meters.
  * Populate `MarkerArray` with cylinders (Yellow for right, Blue for left).

### Step 3: Launch Detection Pipeline
* File: `apex_perception/launch/perception_pipeline.launch.py`.

---

## ✅ Pass / Fail Verification Checklist

Launch the pipeline:
```bash
ros2 launch apex_perception perception_pipeline.launch.py
```

In a second terminal, inspect the detection outputs:
```bash
# 1. Verify marker array publish rate
ros2 topic hz /perception/cone_markers

# 2. View annotated image
ros2 run rqt_image_view rqt_image_view /perception/debug_image
```

### Verification Criteria:
1. `rqt_image_view` shows the camera feed with bounding boxes around both blue and yellow cones.
2. In RViz2 (Fixed frame: `camera_optical_frame` or `base_link`), add a **MarkerArray** display subscribed to `/perception/cone_markers`.
3. 3D blue and yellow cylinders appear in RViz at the corresponding spatial locations.

Record a 30-to-60 second video showing the camera view alongside the 3D markers appearing in RViz!
