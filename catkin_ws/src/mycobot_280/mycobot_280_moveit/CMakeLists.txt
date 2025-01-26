cmake_minimum_required(VERSION 3.1.3)
project(mycobot_280_moveit)

# Find the necessary packages
find_package(catkin REQUIRED
  COMPONENTS
  roscpp
  actionlib
  control_msgs
  joint_trajectory_controller
  controller_interface
  controller_manager
  moveit_ros_move_group
  moveit_fake_controller_manager
  moveit_kinematics
  moveit_planners_ompl
  moveit_ros_visualization
  moveit_setup_assistant
  moveit_simple_controller_manager
  joint_state_publisher
  joint_state_publisher_gui
  robot_state_publisher
  rviz
  tf2_ros
  xacro
)

# Declare the message files (only if you're defining custom messages, which you aren't here)
# If using existing messages from control_msgs, you don't need this section.

# add_action_files(
#   DIRECTORY action
#   FILES FollowJointTrajectory.action
# )

# Generate the messages
generate_messages(
  DEPENDENCIES
  actionlib_msgs
  control_msgs
)

# Declare the catkin package and dependencies
catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  LIBRARIES mycobot_280_moveit
  CATKIN_DEPENDS roscpp actionlib control_msgs joint_trajectory_controller controller_interface controller_manager
)

# Include directories
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Add the executable for the FollowJointTrajectory action server (if implemented in cpp)
add_executable(follow_joint_trajectory_action_server src/follow_joint_trajectory_action_server.cpp)

# Link the executable with necessary libraries
target_link_libraries(follow_joint_trajectory_action_server
  ${catkin_LIBRARIES}
)
