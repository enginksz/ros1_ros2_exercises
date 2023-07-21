import rosbag
import matplotlib.pyplot as plt
from geometry_msgs.msg import Pose2D
import sys
import time
# rosbag dosyalarının isimleri
bag1_name = "...bag"
bag2_name = "...bag"

# okunacak topiclerin isimleri
topic1_name = "topic_name1"
topic2_name = "topic_name2"

# verileri depolamak için boş listeler oluşturun
bag1_topic1_data = []
bag1_topic2_data = []

bag2_topic1_data = []
bag2_topic2_data = []

# rosbag dosyalarını acma
bag1 = rosbag.Bag(bag1_name)
bag2 = rosbag.Bag(bag2_name)

# rosbag dosyalarından verileri okuma 
topics=[topic1_name]

for (topic, msg, ts) in bag1.read_messages(topics=str(topic1_name)):
    bag1_topic1_data.append(msg.y)
     #print(msg.x)

for (topic, msg, ts) in bag2.read_messages(topics=str(topic2_name)):
    bag2_topic2_data.append(msg.pose.y)
    print(msg.pose.x)

plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Title")

plt.plot(bag1_topic1_data, label="label1")
plt.plot(bag2_topic2_data, label="label2")
plt.legend()
plt.show()

for topic, msg, t in bag1.read_messages(topics=[topic1_name]):
    pass

for topic, msg, t in bag2.read_messages(topics=[topic2_name]):

    if topic == topic2_name:
        bag2_topic2_data.append(msg.data)
        print("msg", msg)


print("closeee")
bag1.close()
bag2.close()

