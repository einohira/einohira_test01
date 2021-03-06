#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
 
def talker():
	pub = rospy.Publisher('talker/state', Float64, queue_size=1)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(500)
	
	state = 0;
	while not rospy.is_shutdown():
		_msg = Float64()
		#rospy.loginfo(hello_str)
		state = state + 0.01
		if state > 1.0:
			state = 0
		_msg.data = state
		pub.publish(_msg)
		rate.sleep()
 
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass


