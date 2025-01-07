import rosbag

# Specify the bag file
bag_file = '/mnt/d/Hesai_apartment.bag'

# Open the bag
with rosbag.Bag(bag_file, 'r') as bag:
    with open('lidar_timestamps.txt', 'w') as output_file:
        for topic, msg, t in bag.read_messages(topics=['/hesai/pandar']): #/hesai/pandar - /alphasense/imu - /mavros/imu/data_raw
            # Write the message timestamp to the file
            output_file.write(f"Message time: {msg.header.stamp.to_sec()} - Bag time: {t.to_sec()}\n")
