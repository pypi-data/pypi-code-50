from . import Camera


class SonyNex(Camera):
    img_folders = ["DCIM/*MSDCF"]
    raw_folders = img_folders
    vid_folders = ["PRIVATE/M4ROOT/CLIP"]

    # img_extensions = [".JPG"]
    img_extensions = []
    # raw_extensions = [".ARW"]
    raw_extensions = []
    vid_extensions = [".MP4", ".XML"]
