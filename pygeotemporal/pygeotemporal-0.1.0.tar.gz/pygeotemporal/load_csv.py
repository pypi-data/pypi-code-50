# coding: utf-8

"""
    Load data from CSV files.
"""
from __future__ import absolute_import
from builtins import range
from builtins import object
import logging

from pygeotemporal.time_transformers import time2utc


def load(file):
    pass


class ParametersMap(object):
    def __init__(self, yaml_file):
        pass

    def lookup(self, csv_name):
        return "new_parameter_id"


def parameters_map(yaml_file):
    pass


def get_needed_values(needed_names, column_headers_in, parameters_map, data_in):
    """Drop all columns from data_in that are not in needed_names

    Keyword arguments:
        needed_names -- array of columns to include
        column_headers_in -- array of all columns from original file
        parameters_map -- `ParametersMap`
        data_in -- 2D array for data values from original file
    """
    column_headers_out = []
    needed_indexes = []
    for i in range(len(column_headers_in)):
        if column_headers_in[i] in needed_names:
            column_headers_out.append(parameters_map.lookup(column_headers_in[i]))
            needed_indexes.append(i)

    logging.info(" [pyG.map_names] Removing unneeded data values.")
    data_hold = []
    while len(data_in) > 0:
        data_row = []
        for i in needed_indexes:
            data_row.append(data_in[0][i])
        data_hold.append(data_row)
        data_in.pop(0)

    data_out = []
    while len(data_hold) > 0:
        data_dict = {}
        # FIXME why return this data dictionary?
        data_dict['sensor_name'] = data_hold[0][column_headers_out.index("sensor_name")]
        data_dict['lat'] = float(data_hold[0][column_headers_out.index("lat")])
        data_dict['long'] = float(data_hold[0][column_headers_out.index("long")])
        data_dict['start_time'] = time2utc(data_hold[0][column_headers_out.index("start_date")])
        data_dict['time_zone'] = data_hold[0][column_headers_out.index("time_zone")]

        parameter_name = parameters_map.lookup(data_hold[0][column_headers_out.index("Characteristic Name")],
                                               data_hold[0][column_headers_out.index("Sample Fraction")])

        try:
            pass
            data_dict[parameter_name] = float(data_hold[0][column_headers_out.index("Result Value as Number")])
        except:
            logging.warning("[pyG.map_names] couldn't get value for datapoint - skipping datapoint")
            data_hold.pop(0)
            continue
        data_out.append(data_dict)
        data_hold.pop(0)

    return data_out
