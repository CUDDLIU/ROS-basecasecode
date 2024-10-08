#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
import rosbag
from std_msgs.msg import String

"""  
        需求:写出消息数据到磁盘上的 bag 文件
        流程:
            1.导包
            2.初始化
            3.创建 rosbag 对象并且打开文件流
            4.写数据
            5.关闭流

"""

if  __name__ == "__main__":
    # 2.初始化
    rospy.init_node("write_bag_p")
    # 3.创建 rosbag 对象并且打开文件流
    bag = rosbag.Bag("hello_p.bag",'w')
    # 4.写数据
    msg = String()
    msg.data = "hello bag!"
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    bag.write("/liaoTian",msg)
    # 5.关闭流
    bag.close()
