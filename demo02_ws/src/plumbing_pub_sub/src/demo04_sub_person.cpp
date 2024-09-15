#include "ros/ros.h"
#include "plumbing_pub_sub/Person.h"

/* 
        发布人的消息
            1.包含头文件
                #include "plumbing_pub_sub/Person.h"
            2.初始化ros节点
            3.创建ros节点句柄
            4.创建订阅者对象
            5.处理订阅数据
            6.调用spin函数
 */

void doperson(const plumbing_pub_sub::Person::ConstPtr& person){
     ROS_INFO("订阅人的信息：%s,%d,%.2f",person->name.c_str(),person->age,person->height);
}

int main(int argc, char *argv[])
{
    /* code */
    setlocale(LC_ALL,"");
    ROS_INFO("这是订阅方");
    // 2.初始化ros节点
    ros::init(argc,argv,"jiaZhang");
    // 3.创建ros节点句柄
    ros::NodeHandle nh;
    // 4.创建订阅者对象
    ros::Subscriber sub = nh.subscribe("liaotian",10,doperson);
    // 5.处理订阅数据
    // 6.调用spin函数
    ros::spin();
    return 0;
}

