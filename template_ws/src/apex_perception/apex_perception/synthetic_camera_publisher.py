#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 5: Synthetic Camera Publisher
Role: Generates simulated 640x480 camera frames with blue and yellow track cones.
"""

import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


class SyntheticCameraPublisherNode(Node):
    """
    Publishes synthetic camera frames with simulated blue and yellow traffic cones.
    """

    def __init__(self):
        super().__init__('synthetic_camera_publisher_node')

        self.publisher_ = self.create_publisher(Image, '/camera/color/image_raw', 10)
        self.bridge = CvBridge()
        self.timer = self.create_timer(0.1, self.publish_frame)  # 10 Hz
        self.frame_count = 0
        self.get_logger().info('Synthetic Camera Publisher active on /camera/color/image_raw (10 Hz).')

    def publish_frame(self):
        # Create a synthetic road canvas (dark gray)
        canvas = np.full((480, 640, 3), 50, dtype=np.uint8)

        # Draw a synthetic horizon / sky
        canvas[0:150, :] = [180, 140, 100]

        # Draw road boundaries
        cv2.line(canvas, (0, 480), (280, 150), (200, 200, 200), 2)
        cv2.line(canvas, (640, 480), (360, 150), (200, 200, 200), 2)

        # Draw Left Boundary Cones (Blue in BGR: [255, 50, 0])
        blue_color = (255, 60, 20)
        cv2.fillPoly(canvas, [np.array([[120, 420], [150, 360], [180, 420]], dtype=np.int32)], blue_color)
        cv2.fillPoly(canvas, [np.array([[200, 320], [220, 280], [240, 320]], dtype=np.int32)], blue_color)

        # Draw Right Boundary Cones (Yellow in BGR: [0, 230, 255])
        yellow_color = (0, 230, 255)
        cv2.fillPoly(canvas, [np.array([[460, 420], [490, 360], [520, 420]], dtype=np.int32)], yellow_color)
        cv2.fillPoly(canvas, [np.array([[400, 320], [420, 280], [440, 320]], dtype=np.int32)], yellow_color)

        # Add slight oscillation simulating car vibration
        shift = int(3 * np.sin(self.frame_count * 0.2))
        canvas = np.roll(canvas, shift, axis=0)

        img_msg = self.bridge.cv2_to_imgmsg(canvas, encoding='bgr8')
        img_msg.header.stamp = self.get_clock().now().to_msg()
        img_msg.header.frame_id = 'camera_optical_frame'

        self.publisher_.publish(img_msg)
        self.frame_count += 1


def main(args=None):
    rclpy.init(args=args)
    node = SyntheticCameraPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
