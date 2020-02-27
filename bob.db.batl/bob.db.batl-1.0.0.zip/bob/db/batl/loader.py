import json
from copy import deepcopy
from string import Formatter
import numpy as np
from skimage import transform
from scipy.spatial import cKDTree
from builtins import str
from bob.bio.video import FrameContainer

CALIBRATION_PARAMETERS = ['markers', 'distortion_coefs_opencv', 'camera_matrix_opencv']

def load_data_config(path):
    with open(path, 'r') as data_config_file:
        data_config = json.load(data_config_file)
        for mod_config in data_config.values():
            calibration = mod_config.get('calibration')
            if calibration is not None:
                for field in CALIBRATION_PARAMETERS:
                    fld = calibration.get(field)
                    if fld is not None:
                        calibration[field] = np.array(fld)
    return data_config

def rotate_data(data, angle):
    if angle == 90:
        data = data.swapaxes(-2,-1)[...,::-1]
    elif angle == 180:
        data = data[...,::-1]
    elif angle in (-90, 270):
        data = data.swapaxes(-2,-1)[...,::-1,:]
    else:
        pass
    return data

def dump_data_config(data_config, path):
    data_config = data_config.copy()
    with open(path, 'w') as data_config_file:
        for mod_config in data_config.values():
            calibration = mod_config.get('calibration')
            if calibration is not None:
                for field in CALIBRATION_PARAMETERS:
                    fld = calibration.get(field)
                    if fld is not None:
                        calibration[field] = fld.tolist()
        json.dump(data_config, data_config_file, indent=4, sort_keys=True)

def convert_arrays_to_frame_container(data):
    """
    Convert an input into Frame Container. Inputs is an iterable.

    **Parameters:**

    ``data`` : [] or ND :py:class:`numpy.ndarray`
        An iterable containing the frames data: a list or an ND array, where
        first dimension corresponds to number of frames.

    **Returns:**

    ``frame_container`` : FrameContainer
        FrameContainer containing the frames data.
    """

    frame_container = FrameContainer()  # initialize the FrameContainer

    for idx, item in enumerate(data):

        frame_container.add(idx, item)  # add frame to FrameContainer

    return frame_container

def load_video_stream_from_hdf5(hdf5_file,
                                stream_type,
                                reference_stream_type,
                                data_format_config,
                                warp_to_reference=False,
                                convert_to_rgb=False,
                                crop=None,
                                max_frames=None):
    """
    Load one video stream from a multi-strteam .hdf5 file given filename and
    stream descriptor.

    **Parameters:**

    ``hdf5_file`` : bob.io.base.HDF5File or adapted Pytables
        hdf5 file containing the data

    ``stream_type`` : :py:class:`str`
        Name of the stream to be loaded.

    ``reference_stream_type`` : :py:class:`str`
        Name of the reference stream (temporal and spatial alignment).

    ``data_format_config`` : :py:class:`dict`
        A dictionary defining the format of data in hdf5 files. Key is the name
        of the stream. Value is the list with two elements: first - key of the
        corresponding data in the hdf5 file, second - a bool flag defining if
        data is color (``True``) or gray-scale (``False``).

    ``warp_to_color`` : :py:class:`bool`
        Warp the stream to the color stream. Default: ``False``.

    ``convert_to_rgb`` : :py:class:`bool`
        Convert the data to RGB format. Default: ``False``.

    ``crop`` : :py:class:`bool`
        A list with four parameters - startx = crop[0], starty = crop[1],
        width  = crop[2], height = crop[3]. If given, the video will be cropped.
        Default: ``None``.

    ``max_frames`` : :py:class:`bool`
        A maximum number of frames to load. If not given all frames will be
        loaded. Default: ``None``.

    **Returns:**

    ``video_data`` : numpy array
        Numpy array containing the frames data.

    ``timestamps`` : array
        Array containing the frames timestamps, as millisecond from the
        beginning of the day.
    """

    # stream parameters

    data_config = data_format_config[stream_type]
    reference_config = data_format_config[reference_stream_type]
    # read data

    video_data, timestamps, warp_xform = _load_data(hdf5_file, data_config, reference_config, max_frames)

    # convert from OpenCV's <h, w, BGR> to bob's <RGB, h, w>
    video_data = _adjust_format(video_data, data_config['array_format'])

    if 'rotation' in data_format_config[stream_type]:
        rotation = data_format_config[stream_type]['rotation']
        video_data = rotate_data(video_data, rotation)

    image_mask = np.ones((video_data.shape[0],)+video_data.shape[-2:], dtype=np.bool)
    if stream_type=='depth':
        image_mask[video_data==0] = False

    # warp_to_reference
    if stream_type != reference_stream_type and  warp_to_reference and warp_xform is not None:
        video_data = _warp_to_reference(video_data, warp_xform)
        image_mask = _warp_to_reference(image_mask.astype(np.uint8), warp_xform).astype(np.bool)

    # convert to rgb format for visualization
    if convert_to_rgb:
        video_data = _to_rgb(video_data, stream_type)

    # crop data
    # @TODO: fetch and process only relevant data
    if crop is not None:
        video_data, image_mask = _crop(video_data, image_mask, crop)

    return video_data, timestamps, image_mask

def _load_data(hdf5_file, data_config, reference_config, max_frames):
    def get_timestamps(path):
        if not hdf5_file.has_attribute('timestamps', path):
            return None
        timestamps = hdf5_file.get_attribute('timestamps', path)
        if isinstance(timestamps, np.ndarray)  and \
                len(timestamps) == 1 and \
                isinstance(timestamps[0], np.bytes_):
            timestamps = timestamps[0]
        if isinstance(timestamps, bytes):
            timestamps = timestamps.decode("utf-8")
        if isinstance(timestamps, str):
            return np.array(json.loads('['+timestamps.strip().strip('[').strip(']')+']'))
        else:
            return timestamps

    stitch = data_config.get('stitch')
    data_path = data_config['path']
    if stitch is not None:
        keydict = {key:value['labels'][0] for key, value in stitch.items()}
        data_path = data_path.format(**keydict)
    timestamps = get_timestamps(data_path)
    reference_stitch = reference_config.get('stitch')
    reference_path = reference_config['path']
    if reference_stitch is not None:
        keydict = {key:value['labels'][0] for key, value in reference_stitch.items()}
        reference_path = reference_path.format(**keydict)
    reference_timestamps = get_timestamps(reference_path)
    reference_nframes = hdf5_file.describe(reference_path)[1][0][1][0]

    if max_frames is not None:
        max_frames = min(reference_nframes, max_frames)

    else:
        max_frames = reference_nframes

    if timestamps is None or reference_timestamps is None:
        data_nframes = hdf5_file.describe(data_path)[1][0][1][0]
        timestamps = np.arange(data_nframes)
        reference_timestamps = np.arange(reference_nframes)
    step = reference_timestamps.shape[0]//max_frames if max_frames is not None else 1
    end = -(reference_timestamps.shape[0]%max_frames if max_frames is not None else 0)
    end = end if end != 0 else None
    selected_timestamps = reference_timestamps[:end:step]
    kdtree = cKDTree(timestamps[:,np.newaxis])
    def get_index(val):
        _, i = kdtree.query(val, k=1)
        return i
    indices = [get_index(timestamp[np.newaxis]) for timestamp in selected_timestamps]

    def read(path): return np.stack([hdf5_file.lread(path, i) for i in indices])

    if stitch is not None:
        class PartialFormatter(Formatter):
             def get_field(self, field_name, args, kwargs):
                 try:
                     return super(PartialFormatter, self).get_field(field_name, args, kwargs)
                 except (IndexError, KeyError):
                     return '{'+field_name+'}', field_name

        formatter = PartialFormatter()

        def stitchit(path, instructions):
            instructions = deepcopy(instructions)
            key, value = instructions.popitem()
            dimension = value['dim']
            labels = value['labels']
            array = []
            for label in labels:
                keydict = {key:label}
                _path = formatter.vformat(path, (), keydict)
                if len(instructions) == 0:
                    array.append(read(_path))
                else:
                    array.append(stitchit(_path, instructions))
            return np.concatenate(array, axis=dimension)

        video_data = stitchit(data_config['path'], stitch)
    else:
        video_data = read(data_config['path'])
    timestamps = np.take(timestamps, indices)

    if max_frames is not None:
        assert(selected_timestamps.shape[0] == max_frames)
        assert(video_data.shape[0]==max_frames)

    warp_xform = _get_warp_transform(hdf5_file, data_config, reference_config)

    return video_data, timestamps, warp_xform

def _adjust_format(video, array_format):
    flip = array_format.get('flip')
    if flip is not None:
        for axis in flip:
            video = np.flip(video, axis=array_format[axis])
    depth_index = array_format.get('depth')
    if depth_index is None:
        video = np.transpose(video, (array_format['frame'],
                                     array_format['height'],
                                     array_format['width']))
    else:
        video = np.transpose(video, (array_format['frame'],
                                     depth_index,
                                     array_format['height'],
                                     array_format['width']))
        if video.shape[1] == 1:
            video = video[:,0]

    return video

def _get_warp_transform(f, origin_config, destination_config):
    def get_marker(config):
        if config.get('stitch') is None and f.has_attribute("markers", config['path']):
            markers = f.get_attribute('markers', config['path'])
            if isinstance(markers, np.ndarray)  and \
                    len(markers) == 1 and \
                    isinstance(markers[0], np.bytes_):
                markers = markers[0]
            if isinstance(markers, bytes):
                markers = markers.decode("utf-8")
            if isinstance(markers, str):
                markers = np.array(json.loads('['+markers.strip().strip('[').strip(']')+']'))
        else:
            markers = config.get('calibration',{}).get('markers')
        return markers

    markers = (get_marker(destination_config), get_marker(origin_config))
    if any(m is None for m in markers):
        warp_xform = None
    else:
        warp_xform = transform.ProjectiveTransform()
        warp_xform.estimate(*markers)
    return warp_xform

def _warp_to_reference(video, warp_transform):
    def warp(x):
        return transform.warp(x, warp_transform, output_shape=(1920, 1080), preserve_range=True)
    vectorized_warp = np.vectorize(warp, signature='(m,n)->(o,p)')

    video = vectorized_warp(video)
    return video

def _to_rgb(video, stream_type):
    if stream_type == "infrared":
        video = (np.stack([video, video, video]) / 256).astype('uint8')
        video = np.swapaxes(video, 0, 1)
    elif stream_type == "depth":
        video = (np.stack([video, video, video]) / 32).astype('uint8')
        video = np.swapaxes(video, 0, 1)
    elif len(video.shape) < 4:
        tmin = np.amin(video)
        tmax = np.amax(video)
        video = (video - tmin).astype('float')
        video = (video * 255.0 / float(tmax - tmin))
        video = (np.stack([video, video, video])).astype('uint8')
        video = np.swapaxes(video, 0, 1)
    return video

def _crop(video, mask, crop):
    startx = crop[0]
    starty = crop[1]
    width = crop[2]
    height = crop[3]
    if len(video.shape) == 4:
        video = video[:, :, starty:starty + height, startx:startx + width]
    else:
        video = video[:, starty:starty + height, startx:startx + width]
    mask = mask[:, starty:starty + height, startx:startx + width]
    return video, mask
