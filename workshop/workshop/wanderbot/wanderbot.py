import rclpy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    global scan
    scan = msg.ranges

def timer_callback():
    print(f'0*: {scan[0]}, 90*: {scan[90]}, 180*: {scan[180]}, 270*: {scan[270]}')

def main(args=None):

    rclpy.init(args=args)

    global node
    node = rclpy.create_node('wanderbot')

    global publisher
    publisher = node.create_publisher(Twist, 'cmd_vel', rclpy.qos.qos_profile_system_default)
    sub = node.create_subscription(LaserScan, 'scan', scan_callback, rclpy.qos.qos_profile_sensor_data)
    sub

    timer = node.create_timer(0.5, timer_callback)
    timer

    rclpy.spin(node)
        
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()