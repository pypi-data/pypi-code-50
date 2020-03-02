# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.
"""
Read space delimited text file
"""

import pandas as pd
from ezcad.utils.envars import DEFAULT_PROPERTY_NAMES


def read_sdt(filename):
    """Read space-delimited text file.
    The first line must not be blank.
    It detects if has header or not, and act accordingly.

    :param filename: the input file name
    :type filename: str
    :return: a Pandas dataframe
    :rtype: dataframe
    """
    print("--Reading--", filename)

    with open(filename, 'r') as f:
        first_line = f.readline()
    first_line = first_line.strip()
    columns = first_line.split()
    first_item = columns[0]

    # detect if has header or not
    try:
        first_item = float(first_item)
        print("The first item is number, so no header.")
        has_header = False
    except ValueError:
        print("The first item is not number, so has header.")
        has_header = True

    if has_header:
        data_frame = pd.read_csv(filename, sep='\s+', skipinitialspace=True)
    else:
        # assign column names
        default_column_names = DEFAULT_PROPERTY_NAMES
        if len(columns) > len(default_column_names):
            raise IOError("Has %i columns. Handle max %i columns",
                          len(columns), len(default_column_names))
        else:
            column_names = default_column_names[:len(columns)]

        data_frame = pd.read_csv(filename, sep='\s+', header=None,
                                 skipinitialspace=True, names=column_names)

    print('Pandas data frame columns:', data_frame.columns)
    print('Pandas data frame shape:', data_frame.shape)
    return data_frame


def main():
    fn = '/data_qc/surfs20171206/2_wilcox_xyz.ascii'
    read_sdt(fn)


if __name__ == '__main__':
    main()
