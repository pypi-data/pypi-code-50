import numpy as np
from ..filterable import Filterable
from ..filters.accum_flow import AccumFlow
from ..util.add_flow import add_flow_points
from .base_operator import Operator


class TrackFromFirst(Operator):
    """
        Given a set of points and image data, track the set of points
        to see if they track the image's features correctly
    """

    def __init__(self, point_data, image_data):
        if not isinstance(point_data, Filterable):
            raise AssertionError(
                'point_data should contain a list of point data')
        if not isinstance(image_data, Filterable):
            raise AssertionError(
                'image_data should contain a list of image data')
        point_data.assert_type('point')
        image_data.assert_type('rgb')
        Operator.__init__(self)
        self._point_data = point_data
        self._image_data = image_data

    def _items(self):
        yield self._rect
        for flow in self._flow_data:
            self._rect = self._add(self._rect, flow)
            yield self._rect

    def __len__(self):
        return min(len(self._point_data), len(self._point_data))

    def get_type(self):
        return 'rgb'

