#!/bin/bash

# Start a new tmux session named "robot_automation"
tmux new-session -d -s robot_automation

# Pane 1: SSH and run roscore
tmux send-keys -t robot_automation "./ssh_automation.exp" C-m
tmux send-keys -t robot_automation "roscore" C-m

# Pane 2: SSH and run communication topic
tmux split-window -h
tmux send-keys "./ssh_automation.exp" C-m
tmux send-keys "roslaunch mycobot_communication communication_topic_pi.launch" C-m

# Pane 3: SSH and run tf.launch
tmux split-window -v
tmux send-keys "./ssh_automation.exp" C-m
tmux send-keys "roslaunch nakul_robot tf.launch" C-m

# Pane 4: SSH and run mycobot_moveit.launch
tmux split-window -h
tmux send-keys "./ssh_automation.exp" C-m
tmux send-keys "roslaunch mycobot_280_moveit mycobot_moveit.launch" C-m

# Pane 5: SSH and run controller.launch
tmux split-window -v
tmux send-keys "./ssh_automation.exp" C-m
tmux send-keys "roslaunch nakul_robot controller.launch" C-m

# Pane 6: SSH and run main.py
tmux split-window -h
tmux send-keys "./ssh_automation.exp" C-m
tmux send-keys "rosrun nakul_robot main.py" C-m

# Arrange panes in a tiled layout and attach to the session
tmux select-layout tiled
tmux attach-session -t robot_automation
