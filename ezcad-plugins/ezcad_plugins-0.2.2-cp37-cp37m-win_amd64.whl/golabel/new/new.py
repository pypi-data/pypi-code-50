# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ..label import Label


def init_dob_from_dframe(name, dataframe):
    """Create label from dataframe.
    It calls function :func:`~ezcad.golabel.new.new.init_dob`.

    :param name: name of the new object
    :type name: str
    :param dataframe: a Pandas dataframe
    :type dataframe: dataframe
    :return: a label object
    :rtype: :class:`~ezcad.golabel.label.Label`
    """
    # prop_list = dataframe.columns
    data_array = dataframe.values
    # print(type(data_array))  # <class 'numpy.ndarray'>
    # print(data_array.dtype)  # object
    vertexes = data_array[:, :3]
    labels = data_array[:, 3]
    vertexes = vertexes.astype(float)
    labels = labels.astype(str)
    dob = init_dob(name, vertexes, labels)
    return dob


def init_dob(object_name, vertexes, labels):
    """Create label, base function.

    :param object_name: name of the new object
    :type object_name: str
    :param vertexes: vertexes XYZ
    :type vertexes: array
    :param labels: label for each vertex
    :type labels: array
    :return: a label object
    :rtype: :class:`~ezcad.golabel.label.Label`
    """
    dob = Label(object_name)
    dob.set_text_style()
    dob.set_font()
    dob.set_vertexes(vertexes)
    dob.set_labels(labels)
    # dob.make_pg2d()
    # dob.make_pg3d()
    dob.set_xyz_range()
    return dob
