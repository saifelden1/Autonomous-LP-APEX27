#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 5: Cone Detector & 3D Marker Broadcaster
Role: Processes camera images with OpenCV, extracts blue/yellow cones, and publishes 3D RViz markers.
"""

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from visualization_msgs.msg import Marker, MarkerArray
from cv_bridge import CvBridge, CvBridgeError


class ConeDetectorNode(Node):
    """
    Subscribes to camera frames, detects track cones via HSV segmentation,
    and publishes 3D cylinders in MarkerArray format.
    """

    def __init__(self):
        super().__init__('cone_detector_node')

        self.bridge = CvBridge()

        # Image subscription
        self.image_sub = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.image_callback,
            10
        )

        # Output publishers
        self.debug_image_pub = self.create_publisher(Image, '/perception/debug_image', 10)
        self.marker_pub = self.create_publisher(MarkerArray, '/perception/cone_markers', 10)

        self.get_logger().info('Cone Detector initialized and listening on /camera/color/image_raw.')

    def image_callback(self, msg: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except CvBridgeError as e:
            self.get_logger().error(f'CvBridge error: {e}')
            return

        hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        # HSV ranges for Blue cones (left boundary)
        blue_lower = np.array([95, 120, 50])
        blue_upper = np.array([135, 255, 255])
        blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

        # HSV ranges for Yellow cones (right boundary)
        yellow_lower = np.array([18, 120, 100])
        yellow_upper = np.array([38, 255, 255])
        yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)

        marker_array = MarkerArray()
        marker_id = 0

        # Process Blue Cones
        blue_markers, marker_id = self.extract_cones(
            blue_mask, cv_image, 'blue', (1.0, 0.0, 0.0), (0.0, 0.2, 1.0), marker_id
        )
        marker_array.markers.extend(blue_markers)

        # Process Yellow Cones
        yellow_markers, marker_id = self.extract_cones(
            yellow_mask, cv_image, 'yellow', (0.0, 1.0, 1.0), (1.0, 1.0, 0.0), marker_id
        )
        marker_array.markers.extend(yellow_markers)

        # Publish 3D markers
        self.marker_pub.publish(marker_array)

        # Publish annotated debug image
        debug_msg = self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8')
        debug_msg.header = msg.header
        self.debug_image_pub.publish(debug_msg)

    def extract_cones(self, mask, display_img, cone_type, box_color_bgr, rviz_color_rgb, start_id):
        markers = []
        current_id = start_id

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 100:  # Noise threshold
                continue

            x, y, w, h = cv2.boundingRect(cnt)
            cx = x + w // 2
            cy = y + h // 2

            # Draw bounding box on debug image
            cv2.rectangle(display_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                display_img,
                f"{cone_type.upper()}",
                (x, y - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 255, 255),
                1
            )

            # Approximate 3D spatial position from pixel projection
            # In optical frame: Z is forward depth, X is right, Y is down
            focal_length = 500.0  # Assumed focal length in pixels
            cone_real_height_m = 0.30
            depth_z = (focal_length * cone_real_height_m) / float(h)
            pos_x = (cx - 320.0) * depth_z / focal_length
            pos_y = (cy - 240.0) * depth_z / focal_length

            # Construct 3D RViz Marker
            marker = Marker()
            marker.header.frame_id = 'camera_optical_frame'
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.ns = 'cones'
            marker.id = current_id
            marker.type = Marker.CYLINDER
            marker.action = Marker.ADD

            marker.pose.position.x = float(pos_x)
            marker.pose.position.y = float(pos_y)
            marker.pose.position.z = float(depth_z)

            marker.pose.orientation.w = 1.0

            # Marker dimensions (cone cylinder)
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = cone_real_height_m

            marker.color.r = float(rviz_color_rgb[0])
            marker.color.g = float(rviz_color_rgb[1])
            marker.color.b = float(rviz_color_rgb[2])
            marker.color.a = 1.0

            markers.append(marker)
            current_id += 1

        return markers, current_id


def main(args=None):
    rclpy.init(args=args)
    node = ConeDetectorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
