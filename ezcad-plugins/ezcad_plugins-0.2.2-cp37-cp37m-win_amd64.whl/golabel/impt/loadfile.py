# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import pandas as pd
from ..new.new import init_dob_from_dframe


def load_label_csv(fufn, object_name=None):
    """Load CSV file.
    Format definition.
    The CSV file must NOT have a header row.
    The header names do not matter. The first four columns are
    the x, y, z, and label, respectively.

    :param fufn: full-path filename
    :type fufn: str
    :param object_name: name of the new object
    :type object_name: str
    :return: a label object
    :rtype: :class:`~ezcad.golabel.label.Label`
    """
    # read file with pandas
    column_names = ['x', 'y', 'z', 'label']
    dataFrame = pd.read_csv(fufn, header=None, names=column_names,
                            skipinitialspace=True)
    if object_name is None:
        path, fn = os.path.split(fufn)
        object_name = os.path.splitext(fn)[0]
    dob = init_dob_from_dframe(object_name, dataFrame)
    return dob
