#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
""" 
    演示参数查询：    
        get_param(键,默认值)
            当键存在时，返回对应的值，如果不存在返回默认值
        get_param_cached
            和get_param使用一致， 只是效率高
        get_param_names
            获取所有的参数的键的集合
        has_param
            判断是否包含某个键
        search_param
            查找某个参数的键，并返回完整键名
 """
if __name__ == "__main__":
        rospy.init_node("get_param_p")
        # 1.get_param
        radius = rospy.get_param("radius_p",0.5)
        radius2 = rospy.get_param("radius_xxx",0.5)
        rospy.loginfo("radius = %.2f",radius)
        rospy.loginfo("radius2 = %.2f",radius2)

        # 2.get_param_ached
        radius3 = rospy.get_param_cached("radius_p",0.5)
        radius4 = rospy.get_param_cached("radius_xxx",0.5)
        rospy.loginfo("radius3 = %.2f",radius3)
        rospy.loginfo("radius4 = %.2f",radius4)

        # 3.get_param_names
        names = rospy.get_param_names()
        for name in names:
                rospy.loginfo("name = %s",name)
        
        # 4.has_param
        flag1 = rospy.has_param("radius_p")
        if flag1:
                rospy.loginfo("radius_p 存在")
        else:
                rospy.loginfo("radius_p 不存在")
        flag2 = rospy.has_param("radius_xxx")
        if flag2:
                rospy.loginfo("radius_xxx 存在")
        else:
                rospy.loginfo("radius_xxx 不存在")
        
        # 5.search_param
        key = rospy.search_param("radius_p")
        rospy.loginfo("key = %s",key)