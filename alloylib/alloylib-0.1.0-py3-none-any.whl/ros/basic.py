# Copyright - Transporation, Bots, and Disability Lab - Carnegie Mellon University
# Released under MIT License

import std_msgs.msg
import os
from rospkg import RosPack
import rospy

__all__ = [
    'create_ros_header',
    'resolve_res_path',
    'create_res_dir',
    'get_res_path'
]

def create_ros_header(rospy, frame=""):
    """Creates ros header for a given rospy and frame

    parameters
    ----------
    rospy: rospy object
        You must pass in the rospy object as the time is relative to it.
    frame: string (optional)
        The frame of the header, if it's empty, it means the global frame

    returns
    -------
    std_msgs.msg.Header
        Header message
    """
    msg = std_msgs.msg.Header()
    msg.stamp = rospy.Time.now()
    msg.frame_id = frame

    return msg


def create_res_dir(package_name):
    """
    Create a folder call res at the root of the given ros package

    parameters
    ----------
    package_name: string  
        ROS package name

    returns
    -------
    string
        the path of the res folder; None if package was unresolvable.

    """
    rp = RosPack()
    try:
        dirpath = rp.get_path(package_name)
        res_path = os.path.join(dirpath,"res")
        os.mkdir(res_path)
        return res_path
    except ResourceNotFound as err:
        rospy.logerror('unable find given rospackage in "create_res_dir"')
    return None


def get_res_path(package_name, res_path="res"):
    """
    Return the resource path for this package

    parameters
    ----------
    package_name: string   
        ROS package name

    res_path: string (optional)  
        the name of the res folder in this package

    returns
    -------
    string
        the path of the res folder; None if package was unresolvable.

    """
    rp = RosPack()
    try:
        dirpath = rp.get_path(package_name)
        return os.path.join(dirpath, res_path)
    except ResourceNotFound as err:
        rospy.logerror('unable find given rospackage in "create_res_dir"')
    return None


def get_res_path(package_name, res_path=None):
    rp = RosPack()
    try:
        dirpath = rp.get_path(package_name)
    except ResourceNotFound as err:
        rospy.logwarn('unable find given rospackage in "get_res_path"')
        return None
    if res_path is None:
        res_path = 'res'
    return os.path.join(dirpath,res_path)


def resolve_res_path(path, package_name=None, res_path=None):
    """
    Follow a list of rules to find this path.
    (1) If the path exist and it's a file, return True, path
    (2) package_name_dir/path
    (3) Extra filename and apply package_name/res/file_name

    parameters
    ----------
    path: string
        the complete path or just the filename
    package_name: string (optional)  
        ROS package name
    res_path: string (optional)  
        resource directory in ROS package

    returns
    -------
    string
        If the path exist, the actual path. None if unresolvable.
    """

    #Rule (1)
    if os.path.isfile(path):
        return path

    #Rule (2)
    if package_name:
        #try to find the ros package
        rp = RosPack()
        try:
            dirpath = rp.get_path(package_name)
        except ResourceNotFound as err:
            rospy.logwarn('unable find given rospackage in "resolve_path"')
            return None
        if res_path is None:
            res_path = 'res'
        filepath = os.path.join(dirpath,res_path,path)
        if os.path.isfile(filepath):
            return filepath
        else:
            return None
    else:
        return None

       
