#!/usr/bin/env python

import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryResult, FollowJointTrajectoryFeedback
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from moveit_commander import RobotCommander, PlanningSceneInterface, MoveGroupCommander
from moveit_msgs.msg import RobotTrajectory
from mycobot_communication.msg import MycobotSetAngles  # Import your custom message
import math 
import time

class JointTrajectoryActionServer:
    def __init__(self):
        rospy.init_node('joint_trajectory_action_server')

        # Initialize MoveIt! Commander
        self.robot = RobotCommander()
        # self.scene = PlanningSceneInterface()
        self.group = MoveGroupCommander("arm_group")  # Replace "arm" with the name of your MoveIt! group

        # Action server setup
        self.server = actionlib.SimpleActionServer(
            'arm_group/follow_joint_trajectory', 
            FollowJointTrajectoryAction, 
            execute_cb=self.execute_callback, 
            auto_start=False)
        
        self.server.start()

        self.pub = rospy.Publisher("/mycobot/angles_goal", MycobotSetAngles, queue_size=10)

        rospy.loginfo("JointTrajectoryActionServer started.")
        

    def execute_callback(self, goal):
        feedback = FollowJointTrajectoryFeedback()
        result = FollowJointTrajectoryResult()

        rospy.loginfo("Received goal with %d points in trajectory.", len(goal.trajectory.points))

        # Loop through each trajectory point and execute
        for point in goal.trajectory.points:
            current_state = self.robot.get_current_state()
            self.group.set_start_state(current_state)

            self.group.set_joint_value_target(list(point.positions))

            feedback.desired = point
            self.server.publish_feedback(feedback)

            # Plan and execute the trajectory point
            # success = self.group.go(wait=True)

            # print(success)

            angles = list(point.positions)

            mycobot_sendAngles = MycobotSetAngles()
            mycobot_sendAngles.joint_1 = math.degrees(angles[0])
            mycobot_sendAngles.joint_2 = math.degrees(angles[1])
            mycobot_sendAngles.joint_3 = math.degrees(angles[2])
            mycobot_sendAngles.joint_4 = math.degrees(angles[3])
            mycobot_sendAngles.joint_5 = math.degrees(angles[4])
            mycobot_sendAngles.joint_6 = math.degrees(angles[5])
            mycobot_sendAngles.speed = 40 

            print(mycobot_sendAngles)
            self.pub.publish(mycobot_sendAngles)
            # Wait briefly to avoid overlapping trajectories
            time.sleep(0.1)  # Adjust delay as necessary

        rospy.loginfo("Trajectory executed successfully.")
        result.error_code = result.SUCCESSFUL
        self.server.set_succeeded(result)


if __name__ == '__main__':
    try:
        server = JointTrajectoryActionServer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
