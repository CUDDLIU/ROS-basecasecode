#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import String

if  __name__ == "__main__":
    rospy.init_node("hello")
    """ 
            需求：实现不同类型的话题设置
    """
    #1.全局
    # pub = rospy.Publisher("/chatter",String,queue_size=10) #/xxx/hello /chatter
    # pub = rospy.Publisher("/yyy/chatter",String,queue_size=10) #/xxx/hello /yyy/chatter
    # *有无"/"的区别
    #2.相对
    # pub = rospy.Publisher("chatter",String,queue_size=10) #/xxx/hello /xxx/chatter
    # pub = rospy.Publisher("yyy/chatter",String,queue_size=10) #/xxx/hello /xxx/yyy/chatter
    
    #3.私有 
    # pub = rospy.Publisher("~chatter",String,queue_size=10) #/xxx/hello /xxx/hello/chatter
    pub = rospy.Publisher("~yyy/chatter",String,queue_size=10) #/xxx/hello /xxx/hello/yyy/chatter

    while not rospy.is_shutdown():
        pass
