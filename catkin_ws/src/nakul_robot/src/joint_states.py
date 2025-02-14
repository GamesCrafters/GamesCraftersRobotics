#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from mycobot_communication.msg import MycobotAngles  # Import your custom message
import math  # Import math for degrees to radians conversion

class JointStateRepublisher:
    def __init__(self):
        # Create a publisher for JointState
        self.joint_state_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
        
        # Subscribe to the topic that publishes joint angles (of type JointAngles)
        rospy.Subscriber('/mycobot/angles_real', MycobotAngles, self.joint_angles_callback)

        # Initialize the JointState message
        self.joint_state_msg = JointState()
        self.joint_state_msg.name = ['joint2_to_joint1', 'joint3_to_joint2', 'joint4_to_joint3', 'joint5_to_joint4', 'joint6_to_joint5', 'joint6output_to_joint6']  # Replace with actual joint names
        self.joint_state_msg.position = [0.0] * 6  # Initialize with zero angles for 6 joints

    def joint_angles_callback(self, msg):
        # Extract joint angles from the received message and convert them from degrees to radians
        joint_angles = [
            math.radians(msg.joint_1),
            math.radians(msg.joint_2),
            math.radians(msg.joint_3),
            math.radians(msg.joint_4),
            math.radians(msg.joint_5),
            math.radians(msg.joint_6)
        ]

        # Update the JointState message
        self.joint_state_msg.header.stamp = rospy.Time.now()  # Update timestamp
        self.joint_state_msg.position = joint_angles

        # Publish the JointState message
        self.joint_state_pub.publish(self.joint_state_msg)

if __name__ == '__main__':
    # Initialize the ROS node
    rospy.init_node('joint_state_republisher', anonymous=True)
    
    # Create the republisher object
    republisher = JointStateRepublisher()
    
    # Keep the node running
    rospy.spin()
