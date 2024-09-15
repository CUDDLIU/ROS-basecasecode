#include "ros/ros.h"
#include "std_msgs/String.h"//普通文本类型消息
#include <sstream>//组织字符串
/*
        发布方实现；
                1.包含头文件
                        ROS中文本类型 ---> std_msgs/String.h
                2.初始化ROS节点
                3.创建节点句柄
                4.创建发布者对象
                5.编写发布逻辑并发布数据
*/

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    /* code */
     //2.初始化ROS节点
    ros::init(argc,argv,"teacher");
    //3.创建节点句柄
    ros::NodeHandle nh;
    //4.创建发布者对象
    ros::Publisher pub = nh.advertise<std_msgs::String>("school",10);
    //5.编写发布逻辑并发布数据
    //要求以10HZ的频率发布数据
    //先创建被发布的消息
    std_msgs::String msg;
    //发布频率
    ros::Rate rate(1);
    //设置编号
    int count = 0;
    //编写循环，循环中发布数据
    ros::Duration(3).sleep();
    while (ros::ok())
    {
        /* code */
        count++;
        //实现字符串拼接数字
        std::stringstream ss;
        ss << "CQU -->" << count;
        //msg.data = "hello";
        msg.data = ss.str();
        pub.publish(msg);
        //添加日志：
        ROS_INFO("发布的数据：%s",ss.str().c_str());
        rate.sleep();

        ros::spinOnce();//官方建议，处理回调函数
    }
    
    return 0;
}
