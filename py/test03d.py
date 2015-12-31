#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
 
def talker():
	pub = rospy.Publisher('talker/state', Float64, tcp_nodelay=True, queue_size=2)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(10)
	
	state = rospy.get_time();
	while not rospy.is_shutdown():
		_msg = Float64()
		#rospy.loginfo(hello_str)
		state_new = rospy.get_time()
		_msg.data = state_new - state
		state = state_new
		pub.publish(_msg)
		rate.sleep()
 
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


