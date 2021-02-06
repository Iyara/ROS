#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def callback(data):
    # print data heard from ROS topic
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
    # initialize node
    rospy.init_node('listener', anonymous=True)
    # subscribe to the 'chatter' topic
    rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("pose", String, callback)

    rospy.spin()


if __name__ == '__main__':
    listener()




