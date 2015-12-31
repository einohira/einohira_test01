import rospy
import sensor_msgs.msg

def callback(data):
	print data.header.stamp.secs, data.header.stamp.nsecs, data.temperature
     
def listener():
	rospy.init_node('listener', anonymous=True)
 
	rospy.Subscriber("talker/state", sensor_msgs.msg.Temperature, callback)

	rospy.spin()

	print 'finished'
 
if __name__ == '__main__':
	listener()
