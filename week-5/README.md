# Week 5: Perception & Feature Extraction (Vision & LiDAR)

In Weeks 1–4, you mastered vehicle kinematics and simulation. Now we equip our vehicle with **eyes**. 

In autonomous racing (Formula AI) and rover planetary exploration (ERC 27), the perception pipeline must convert raw camera pixels and laser pulses into spatial coordinates of objects.

---

## 1. The ROS 2 Image Pipeline & `cv_bridge`

Cameras publish raw byte arrays as `sensor_msgs/msg/Image`. To process these images with computer vision libraries like OpenCV, we use `cv_bridge`.

```
+------------------------------------+
|            Camera Driver           |
|  publishes: sensor_msgs/msg/Image  |
+------------------------------------+
                  │
                  ▼
+------------------------------------+
|             cv_bridge              |
|  cv_bridge.imgmsg_to_cv2(msg, BGR) |
+------------------------------------+
                  │
                  ▼
+------------------------------------+
|         OpenCV NumPy Array         |
|   (Shape: Height x Width x 3)      |
+------------------------------------+
```

---

## 2. Track 1: Formula Student AI — Cone Detection via HSV Segmentation

Formula Student rules specify:
* **Blue Cones**: Mark the left track boundary.
* **Yellow Cones**: Mark the right track boundary.
* **Orange Cones**: Mark the start/finish line and time-keeping gates.

### Why HSV instead of RGB?
In outdoor sunlight and shadows, RGB values shift wildly. **HSV (Hue, Saturation, Value)** separates the chromatic color (**Hue**) from brightness (**Value**).

```python
import cv2
import numpy as np

# Convert to HSV color space
hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

# Yellow cone HSV threshold bounds
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([35, 255, 255])
yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

# Blue cone HSV threshold bounds
blue_lower = np.array([100, 120, 70])
blue_upper = np.array([130, 255, 255])
blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)
```

Finding contours and centroid in image coordinates $(u, v)$:
```python
contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if cv2.contourArea(cnt) > 150: # Filter small noise
        M = cv2.moments(cnt)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
```

---

## 3. Track 2: ERC 27 — ArUco Marker 6-DoF Pose Estimation

European Rover Challenge uses ArUco visual fiducial tags at charging stations, sample sites, and navigation waypoints.
```python
import cv2

# Define ArUco dictionary (e.g. DICT_4X4_50)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

corners, ids, rejected = detector.detectMarkers(grayscale_image)
```

---

## 4. Visualizing Features in RViz with `visualization_msgs/MarkerArray`

Perception outputs are not just printed to the terminal—they are published as 3D markers so planners can see them in RViz:
* `Marker.CYLINDER`: Used for traffic cones.
* `Marker.SPHERE`: Used for detected obstacle centroids.
* `Marker.CUBE`: Used for rover sample containers.
