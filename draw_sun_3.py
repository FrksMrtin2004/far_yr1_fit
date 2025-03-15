import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
import time

class TurtleSun(Node):
    def __init__(self):
        super().__init__('turtle_sun')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def draw_triangle_ray(self, height=2.0, speed=1.0):
        msg = Twist()

        # Első oldal rajzolása (kifelé)
        msg.linear.x = speed
        duration = height / speed
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        # Mozgás leállítása
        msg.linear.x = 0.0
        self.publisher_.publish(msg)

        # Balra fordulás
        self.rotate_turtle(120)

        # Második oldal rajzolása (visszafele)
        msg.linear.x = speed
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        # Mozgás leállítása
        msg.linear.x = 0.0
        self.publisher_.publish(msg)

        # Visszafordulás az eredeti irányba
        self.rotate_turtle(-60)

    def rotate_turtle(self, angle_degree, angular_speed=1.0):
        msg = Twist()
        msg.angular.z = math.radians(angle_degree) * angular_speed
        duration = abs(math.radians(angle_degree) / angular_speed)
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher_.publish(msg)

        # Forgás leállítása
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

    def draw_sun(self, num_rays=8, height=2.0):
        for i in range(num_rays):
            self.draw_triangle_ray(height)
            if i < num_rays - 1:  # Az utolsó sugár után nincs elforgatás
                self.rotate_turtle(360 / num_rays)
        
        # Teknős megállítása
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)

def main():
    rclpy.init()
    node = TurtleSun()
    time.sleep(2)  # Várakozás a szimuláció indítására
    node.draw_sun(num_rays=8, height=2.0)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
