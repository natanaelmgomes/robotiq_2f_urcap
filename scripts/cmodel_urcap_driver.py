#!/usr/bin/env python3.7

# """Module to control Robotiq's gripper 2F-85."""
# BASED ON: https://dof.robotiq.com/discussion/1962/programming-options-ur16e-2f-85#latest
# ROS/Python2 port by felixvd
# review by natanaelmgomes

import os
import sys
import socket
import rospy
from cmodel_urcap import RobotiqCModelURCap
from robotiq_2f_gripper_control.msg import Robotiq2FGripper_robot_input as CModelStatus
from robotiq_2f_gripper_control.msg import Robotiq2FGripper_robot_output as CModelCommand

def mainLoop(ur_address):
  # Gripper is a C-Model that is connected to a UR controller with the Robotiq URCap installed. 
  # Commands are published to port 63352 as ASCII strings.
  gripper = RobotiqCModelURCap(ur_address)
  # The Gripper status
  pub = rospy.Publisher('status', CModelStatus, queue_size=3)
  # The Gripper command
  rospy.Subscriber('command', CModelCommand, gripper.sendCommand)
  
  while not rospy.is_shutdown():
    # Get and publish the Gripper status
    status = gripper.getStatus()
    pub.publish(status)
    # Wait a little
    rospy.sleep(0.1)

if __name__ == '__main__':
  rospy.init_node('cmodel_urcap_driver')
  try:
    mainLoop(sys.argv[1])
  except rospy.ROSInterruptException: pass
