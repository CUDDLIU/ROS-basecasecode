#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import rospy
from turtlesim.msg import Pose

""" 
        方实现：订阅并输出乌龟位姿信息
                话题：/turtle1/pose
                消息：turtlesim/Pose
        1.导包
        2.初始化ros
        3.创建订阅对象
        4.使用回调函数处理数据
        5.spin()

 """

def doPose(pose):
    rospy.loginfo("P-->乌龟位姿信息：坐标(%.2f,%.2f),朝向：%.2f,线速度：%.2f,角速度：%.2f",
                  pose.x,pose.y,pose.theta,pose.linear_velocity,pose.angular_velocity)

if  __name__ == "__main__":
    # 2.初始化ros
    rospy.init_node("sub_pose_p")
    # 3.创建订阅对象
    sub =  rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    # 4.使用回调函数处理数据
    # 5.spin()
    rospy.spin()