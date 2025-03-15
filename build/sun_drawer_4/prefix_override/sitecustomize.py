import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ajr/ros2_ws/src/sun_drawer_4/install/sun_drawer_4'
