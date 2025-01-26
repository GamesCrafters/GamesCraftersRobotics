cmake_minimum_required(VERSION 3.0.2)
project(mycobot_280pi_moveit)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  moveit_msgs
  moveit_core
  moveit_ros_planning_interface
  moveit_simple_controller_manager
  pluginlib
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs moveit_msgs moveit_core moveit_ros_planning_interface pluginlib moveit_simple_controller_manager
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
catkin_install_python(PROGRAMS
  scripts/sync_plan.py
  scripts/path_planning_and_obstacle_avoidance_demo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
