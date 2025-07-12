import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimplePublisher(Node):

    def __init__(self):

        #Inherets initilization from node class
        super().__init__("simple_publisher")

        self.buffer_size = 10
        self.topic_name = "chatter"
        self.pub_ = self.create_publisher(String, self.topic_name, self.buffer_size)
        self.counter_ = 0
        self.frequency_ = 1.0
        self.get_logger().info("Publishing at %d Hz" % self.frequency_)
        
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_
        self.pub_.publish(msg)
        self.counter_ += 1


def main():
    rclpy.init()
    simple_publisher = SimplePublisher()

    # runs and keeps node running
    rclpy.spin(simple_publisher)
    
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()