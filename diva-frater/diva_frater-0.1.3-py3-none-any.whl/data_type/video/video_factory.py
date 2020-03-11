from typing import Dict

from frater.validation.json import validate_json
from .video import Video
from .video_defaults import VIDEO_JSON_DEFAULT

__all__ = ['video_to_json', 'json_to_video']


def video_to_json(video: Video) -> Dict:
    return {
        'data_type': VIDEO_JSON_DEFAULT['data_type'],
        'video_name': video.video_name,
        'experiment': video.experiment,
        'width': video.width,
        'height': video.height,
        'framerate': video.framerate,
        'start_frame': video.start_frame,
        'end_frame': video.end_frame
    }


@validate_json(default=VIDEO_JSON_DEFAULT, completion=True)
def json_to_video(video: Dict) -> Video:
    return Video(video['video_name'],
                 video['experiment'],
                 video['width'],
                 video['height'],
                 video['framerate'],
                 video['start_frame'],
                 video['end_frame'])
