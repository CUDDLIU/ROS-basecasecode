#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
    参数服务器操作之删除_Python实现:
    rospy.delete_param("键")
    键存在时，可以删除成功，键不存在时，会抛出异常
"""
import rospy

if __name__ == "__main__":
    rospy.init_node("radius_p")

    try:
        rospy.delete_param("radius_p")
    except Exception as e:
        rospy.loginfo("删除失败")
