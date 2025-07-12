import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):

    def __init__(self):

        #Inherets initilization from node class
        super().__init__("simple_subscriber")

        self.buffer_size = 10
        self.topic_name = "chatter"
        self.sub_ = self.create_subscription(String, self.topic_name, self.msgCallback, self.buffer_size)
        self.sub_

    def msgCallback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)


def main():
    rclpy.init()

    simple_publisher = SimpleSubscriber()
    rclpy.spin(simple_publisher)
    
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()