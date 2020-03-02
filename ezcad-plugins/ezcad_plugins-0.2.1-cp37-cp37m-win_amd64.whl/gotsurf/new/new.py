# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ..surface import Tsurface


def from_points(points, name):
    """Create tsurface from point object.

    :param points: input point object
    :type points: :class:`~ezcad.gopoint.point.Point`
    :param name: name of the new object
    :type name: str
    :return: a tsurface object
    :type: :class:`~ezcad.gotsurf.surface.Tsurface`
    """
    vertexes = points.vertexes['xyz']
    dob = Tsurface(name=name, vertexes=vertexes)
    dob.set_triangles()  # Delaunay
    for prop_name in points.prop:
        array = points.prop[prop_name][points.prop_array_key]
        dob.add_property(prop_name, array=array)
    dob.set_current_property(prop_name=points.current_property)
    dob.set_xyz_range()
    return dob
