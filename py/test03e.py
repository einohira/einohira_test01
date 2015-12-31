#!/usr/bin/env python
import rospy
import sensor_msgs.msg
 
def talker():
	pub = rospy.Publisher('talker/state', sensor_msgs.msg.Temperature, tcp_nodelay=True, queue_size=2)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1)
	
	print 'running'
	state = rospy.get_time();
	while not rospy.is_shutdown():
		_msg = sensor_msgs.msg.Temperature()
		#rospy.loginfo(hello_str)
		_msg.header.stamp = rospy.Time.now()
		_msg.temperature = 25
		_msg.variance = 0
		pub.publish(_msg)
		rate.sleep()
 
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


