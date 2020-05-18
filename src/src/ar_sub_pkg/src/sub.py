#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker

def callback(data):
    msg = "\nmarker id: " + str(data.id) + "\n" + str(data.pose)
    rospy.loginfo(msg)
    #rospy.loginfo(data.id)
    #rospy.loginfo(data.pose)

def listener():
    rospy.init_node('ar_sub')
    rospy.Subscriber("visualization_marker", Marker, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
