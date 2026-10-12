#!/usr/bin/env python3
"""
APEX Autonomous Systems - Week 2: Mission Coordinator
Role: Executes waypoint mission as a ROS 2 Action Server and hosts E-Stop Service.
"""

import time
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.executors import MultiThreadedExecutor

from apex_mission_interfaces.action import MissionTraverse
from apex_mission_interfaces.srv import TriggerEStop


class MissionCoordinatorNode(Node):
    """
    Action Server executing MissionTraverse with real-time feedback and E-Stop support.
    """

    def __init__(self):
        super().__init__('mission_coordinator_node')

        # Use reentrant callback group to allow simultaneous action execution & service calls
        self.cb_group = ReentrantCallbackGroup()

        # Declare configurable speed parameter
        self.declare_parameter('default_speed', 1.5)
        self.default_speed = (
            self.get_parameter('default_speed').get_parameter_value().double_value
        )

        # Internal emergency stop flag
        self.estop_triggered = False

        # Register Emergency Stop Service
        self.estop_service = self.create_service(
            TriggerEStop,
            '/mission/emergency_stop',
            self.handle_estop,
            callback_group=self.cb_group
        )

        # Register Action Server
        self.action_server = ActionServer(
            self,
            MissionTraverse,
            '/mission/traverse',
            execute_callback=self.execute_mission_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            callback_group=self.cb_group
        )

        self.get_logger().info('Mission Coordinator Action Server is active and ready.')

    def goal_callback(self, goal_request):
        """Accepts or rejects incoming goal requests."""
        if self.estop_triggered:
            self.get_logger().warn('Rejected mission goal: Emergency Stop is currently ACTIVE!')
            return GoalResponse.REJECT

        self.get_logger().info(
            f'Accepted goal: {goal_request.waypoint_count} waypoints at {goal_request.traverse_speed} m/s.'
        )
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        """Accepts or rejects cancellation requests."""
        self.get_logger().warn('Client requested cancellation of current mission.')
        return CancelResponse.ACCEPT

    def handle_estop(self, request, response):
        """Emergency Stop service callback."""
        self.estop_triggered = True
        response.success = True
        response.confirmation = f'EMERGENCY STOP TRIGGERED: {request.reason}'
        self.get_logger().error(response.confirmation)
        return response

    async def execute_mission_callback(self, goal_handle):
        """Executes the waypoint loop and sends progress feedback."""
        self.get_logger().info('Executing mission...')
        feedback_msg = MissionTraverse.Feedback()
        start_time = self.get_clock().now()

        total_waypoints = goal_handle.request.waypoint_count
        speed = goal_handle.request.traverse_speed if goal_handle.request.traverse_speed > 0 else self.default_speed

        for i in range(1, total_waypoints + 1):
            # Check for external cancellation or internal E-Stop
            if goal_handle.is_cancel_requested or self.estop_triggered:
                goal_handle.canceled()
                result = MissionTraverse.Result()
                result.success = False
                result.final_state = 'CANCELED_OR_ESTOPPED'
                result.total_time_sec = (self.get_clock().now() - start_time).nanoseconds / 1e9
                self.get_logger().warn('Mission aborted mid-execution.')
                return result

            # Simulate traversal time per waypoint
            time.sleep(1.0 / (speed if speed > 0 else 1.0))

            # Send feedback
            feedback_msg.current_waypoint = i
            feedback_msg.progress_percent = (i / total_waypoints) * 100.0
            feedback_msg.status_message = f'Traversing waypoint {i}/{total_waypoints} at {speed:.1f} m/s'
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback: {feedback_msg.status_message} ({feedback_msg.progress_percent:.0f}%)')

        # Successful completion
        goal_handle.succeed()
        result = MissionTraverse.Result()
        result.success = True
        result.final_state = 'MISSION_COMPLETE'
        result.total_time_sec = (self.get_clock().now() - start_time).nanoseconds / 1e9
        self.get_logger().info(f'Mission successfully completed in {result.total_time_sec:.2f} seconds.')
        return result


def main(args=None):
    rclpy.init(args=args)
    node = MissionCoordinatorNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Mission Coordinator.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
