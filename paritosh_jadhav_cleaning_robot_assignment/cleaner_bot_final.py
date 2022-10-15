#! /usr/bin/env python3

import rospy
import time
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def cleaner_bot(publisher):

    current_pose = Pose()
    current_pose.x = 1
    current_pose.y = 1
    current_pose.theta = 0

    go_to_goal(publisher, x_goal, y_goal)

    set_desired_orientation(publisher, 30, math.radians(current_pose.theta))

    for i in range(0,5):
        move_straight(publisher, 2.0, 1.0, True)
        set_desired_orientation(publisher, 20, 90, False)
        move_straight(publisher, 2.0, 9.0, True)
        set_desired_orientation(publisher, 20, 90, True)
        move_straight(publisher, 2.0, 1.0, True)
        set_desired_orientation(publisher, 20, 90, True)
        move_straight(publisher, 2.0, 9.0, True)
        set_desired_orientation(publisher, 20, 90, False)
        






