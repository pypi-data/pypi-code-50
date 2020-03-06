#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import warnings

import pandas as pd

from tstoolbox import tsutils

from . import evaplib

warnings.filterwarnings("ignore")


def _columns(tsd, req_column_list=[], optional_column_list=[]):
    if None in req_column_list:
        raise ValueError(
            tsutils.error_wrapper(
                """
You need to supply the column (name or number, data column numbering
starts at 1) for {0} time-series.

Instead you gave {1}""".format(
                    len(req_column_list), req_column_list
                )
            )
        )

    collect = []
    for loopvar in req_column_list + optional_column_list:
        try:
            nloopvar = int(loopvar) - 1
        except TypeError:
            nloopvar = loopvar
        if nloopvar is None:
            collect.append(None)
        else:
            collect.append(tsd.ix[:, nloopvar])

    return collect


def hargreaves(
    lat,
    temp_min_col,
    temp_max_col,
    source_units,
    input_ts="-",
    start_date=None,
    end_date=None,
    dropna="no",
    clean=False,
    round_index=None,
    skiprows=None,
    index_type="datetime",
    names=None,
    target_units=None,
    print_input=False,
    temp_mean_col=None,
):
    """hargreaves

    """
    columns = [temp_min_col, temp_max_col]
    column_names = ["tmin", "tmax"]
    if temp_mean_col is not None:
        columns.append(temp_mean_col)
        column_names.append("temp")
    internal_target_units = ["degC"] * len(column_names)

    tsd = tsutils.common_kwds(
        tsutils.read_iso_ts(
            input_ts, skiprows=skiprows, names=names, index_type=index_type
        ),
        start_date=start_date,
        end_date=end_date,
        pick=columns,
        round_index=round_index,
        dropna=dropna,
        source_units=source_units,
        target_units=internal_target_units,
        clean=clean,
    )

    tsd.columns = column_names

    if any(tsd.tmax <= tsd.tmin):
        raise ValueError(
            tsutils.error_wrapper(
                """
On the following dates:

{0},

minimum temperature values in column "{1}" are greater than or equal to
the maximum temperature values in column "{2}".""".format(
                    tsd[tsd.tmax <= tsd.tmin].index, temp_min_col, temp_max_col
                )
            )
        )

    if temp_mean_col is None:
        warnings.warn(
            tsutils.error_wrapper(
                """
Since `temp_mean_col` is None, the average daily temperature will be
estimated by the average of `temp_min_col` and `temp_max_col`""".format(
                    **locals()
                )
            )
        )
        tsd.temp = (tsd.tmin + tsd.tmax) / 2.0

    if any(tsd.tmin >= tsd.temp) or any(tsd.tmax <= tsd.temp):
        raise ValueError(
            tsutils.error_wrapper(
                """
On the following dates:

{0},

the daily average is either below or equal to the minimum temperature in column {1}
or higher or equal to the maximum temperature in column {2}.""".format(
                    tsd[tsd.tmin >= tsd.temp | tsd.tmax <= tsd.temp],
                    temp_min_col,
                    temp_max_col,
                )
            )
        )
    # 'Roll-out' the distribution from day to day.
    jday = np.arange(1, 367)

    # FAO declination calculation
    dec = 0.409 * np.sin(2.0 * np.pi * jday / 365.0 - 1.39)

    lrad = lat * np.pi / 180.0

    s = np.arccos(-np.tan(dec) * np.tan(lrad))

    # FAO radiation calculation
    dr = 1.0 + 0.033 * np.cos(2 * np.pi * jday / 365)

    # FAO radiation calculation
    ra = (
        118.08
        / np.pi
        * dr
        * (s * np.sin(lrad) * np.sin(dec) + np.cos(lrad) * np.cos(dec) * np.sin(s))
    )

    # ra just covers 1 year - need to map onto all years...
    newra = tsd.tmin.copy()
    for day in jday:
        newra[newra.index.dayofyear == day] = ra[day - 1]

    tsdiff = tsd.tmax - tsd.tmin

    # Copy tsd.temp in order to get all of the time components correct.
    pe = tsd.temp.copy()
    pe = 0.408 * 0.0023 * newra * (tsd.temp + 17.8) * np.sqrt(abs(tsdiff))

    pe = pd.DataFrame(pe, columns=["pet_hargreaves:mm"])
    if target_units != source_units:
        pe = tsutils.common_kwds(pe, source_units="mm", target_units=target_units)
    return tsutils.return_input(print_input, tsd, pe)


def reference():
    """reference penman-monteith

    """
    print("reference")


def potential():
    """potential

    """
    print("potential")
