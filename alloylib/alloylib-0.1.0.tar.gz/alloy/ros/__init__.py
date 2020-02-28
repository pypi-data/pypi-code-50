

import warnings

#test if ros exist
try:
    import rospy
    #import everything else if possible
    from .basic import *
    from .ros_conversions import *

    __all__ = []
    __all__ += basic.__all__
    __all__ += ros_conversions.__all__

except ImportError:
    warnings.warn(RuntimeWarning('Unable to find ROS specific libraries, you maybe trying to reference this sub-module on a none ROS machine'))



