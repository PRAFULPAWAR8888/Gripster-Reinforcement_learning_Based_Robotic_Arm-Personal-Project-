import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/praful_pawar/dreambot_ws/install/dreambot_py_examples'
