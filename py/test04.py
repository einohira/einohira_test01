import rospy
from std_msgs.msg import Float64
 
def callback(data):
	rospy.loginfo("state: %f", data.data)
	print dir(data), data._has_header
     
def listener():
	rospy.init_node('listener', anonymous=True)
 
	rospy.Subscriber("talker/state", Float64, callback)

	rospy.spin()
 
if __name__ == '__main__':
	listener()
