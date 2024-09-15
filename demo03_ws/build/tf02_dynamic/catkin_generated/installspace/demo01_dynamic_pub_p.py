#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import rospy
import tf
import tf2_ros
import tf_conversions
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose
""" 
        发布方：订阅乌龟的位姿信息，转换成坐标系的相对关系，再发布
        准  备
                    话题：/turtle1/pose
                    类型： /turtlesim/Pose

        流程：
                1.导包
                2.初始化节点
                3.创建订阅方对象
                4.回调函数处理订阅到的数据（核心）
                5.spin()
"""

def doPose(pose):
    # 1.创建发布坐标系相对关系的对象
    pub = tf2_ros.TransformBroadcaster()
    # 2.将 pose 转换成坐标系相对关系消息
    ts = TransformStamped()
    ts.header.frame_id = "world"
    ts.header.stamp = rospy.Time.now()
    ts.child_frame_id = "turtle1"
    # 子级坐标系相对于父级坐标系的偏移量
    ts.transform.translation.x = pose.x
    ts.transform.translation.y = pose.y
    ts.transform.translation.z = 0
    # 四元数
    # 从欧拉角转换四元数
    """  
            乌龟是2D的不存在x上的翻滚,Y上的俯仰,只有Z上的偏航
            0 0 pose.theta
    """
    qtn = tf_conversions.transformations.quaternion_from_euler(0,0,pose.theta)
    ts.transform.rotation.x = qtn[0]
    ts.transform.rotation.y = qtn[1]
    ts.transform.rotation.z = qtn[2]
    ts.transform.rotation.w = qtn[3]
    # 3,发布
    pub.sendTransform(ts)



if  __name__ == "__main__":

    # 2.初始化节点
    rospy.init_node("dynamic_pub_p")
    # 3.创建订阅方对象
    sub = rospy.Subscriber("/turtle1/pose",Pose,doPose,queue_size=100)
    # 4.回调函数处理订阅到的数据（核心）

    # 5.spin()
    rospy.spin()