import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/admin-7/batch2/ros2_ws/src/install/robot_controller_sept_3_dk'
