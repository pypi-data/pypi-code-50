# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

"""
Read the text file from SeisSpace tool Chv Header Dump.
CHV_HDR_DUMP $Revision: 20070726.0 $
Select header list mode: List
"""

import pandas as pd
from ezcad.utils.logger import logger


def read_chd(filename, skip_lines=-1):
    """Read SeisSpace custom header dump file.

    :param filename: the input file name
    :type filename: str
    :param skip_lines: number of lines to skip
    :type skip_lines: int
    :return: a Pandas dataframe
    :rtype: dataframe
    """
    print("--Reading--", filename)

    # with open(filename, 'r') as f:
    # The header PW_SEQNO type (long integer) is special char in text file.
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x90 in position
    # 4498: invalid start byte. Here I ignore this error at decode.

    column_names = []
    iline = 0
    with open(filename, mode='r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            iline += 1
            if iline <= skip_lines:
                continue
            if line[2:8] == 'Column':
                line = line.strip()
                columns = line.split()
                column_name = columns[2]
                column_names.append(column_name)
            else:
                line = line.strip()
                columns = line.split()
                try:
                    first_number = int(columns[0])
                    break
                except:  # ValueError, IndexError (for blank lines)
                    pass

    if len(column_names) == 0:
        logger.critical("Header lines may contain bad characters")
    print('Number of columns:', len(column_names))
    print('Column names:', column_names)
    print('Line number of the first data line:', iline)
    print('First number at the first data line:', first_number)

    data_frame = pd.read_csv(filename, sep='\s+', header=None,
        skiprows=iline, skipinitialspace=True, names=column_names)
    print('Pandas data frame shape:', data_frame.shape)
    return data_frame


def main():
    fn = '/home/test/ss_chv_header_dump.txt'
    read_chd(fn)


if __name__ == '__main__':
    main()
