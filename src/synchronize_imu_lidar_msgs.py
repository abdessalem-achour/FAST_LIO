import rospy
from sensor_msgs.msg import Imu, PointCloud2
from message_filters import ApproximateTimeSynchronizer, Subscriber

def sync_callback(imu_msg, lidar_msg):
    # Republish the IMU message
    imu_pub.publish(imu_msg)
    
    # Republish the LiDAR message
    lidar_pub.publish(lidar_msg)
    
    rospy.loginfo(f"Published synchronized IMU and LiDAR messages.")

# Initialize the ROS node
rospy.init_node('sync_and_republish_node')

# Subscribers for the IMU and LiDAR topics
imu_sub = Subscriber('/alphasense/imu', Imu)
lidar_sub = Subscriber('/hesai/pandar', PointCloud2)

# Publishers for the synchronized IMU and LiDAR messages
imu_pub = rospy.Publisher('/synchronized_imu', Imu, queue_size=10)
lidar_pub = rospy.Publisher('/synchronized_lidar', PointCloud2, queue_size=10)

# Approximate Time Synchronizer
ats = ApproximateTimeSynchronizer([imu_sub, lidar_sub], queue_size=10, slop=0.01)
ats.registerCallback(sync_callback)

# Keep the node running
rospy.spin()
