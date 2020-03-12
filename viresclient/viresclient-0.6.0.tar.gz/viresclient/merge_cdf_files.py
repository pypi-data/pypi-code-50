#!/usr/bin/env python
​
import sys
import re
import os
import os.path
import contextlib
import datetime
import numpy
import cdflib
​
​
RE_TITILE = re.compile("([A-Za-z0-9_]+)([0-9]{8,8}T[0-9]{6,6})_([0-9]{8,8}T[0-9]{6,6})(.*)")
​
CDF_CHAR = 51
CREATOR = os.path.basename(sys.argv[0])
CDF_SPEC = {"Majority": "Row_major"}
CDF_VAR_SPEC = {
    "Compress": 4,
}
CDF_TYPE_FIX = {
    CDF_CHAR: lambda a: a.astype("S")
}
CDF_BLOCKING_FACTOR_BYTE_SIZE = 1000 * 1024
​
​
class CdfError(ValueError):
    "CDF error exception."
​
​
def merge_cdf_files(output, *inputs):
    """ Merge multiple CDF files into one. """
​
    if not inputs:
        raise ValueError("At least one input CDF file must be provided!")
​
    try:
        cdf_in = []
        for input_ in inputs:
            if not os.path.exists(input_):
                raise FileNotFoundError(input_)
            cdf_in.append(cdflib.CDF(input_))
​
        cdf_info = extract_common_info(*cdf_in)
​
        if os.path.exists(output):
            os.remove(output)
​
        with contextlib.closing(cdflib.CDF(output, cdf_spec=CDF_SPEC)) as cdf_out:
            _merge_cdf(cdf_out, cdf_info, *cdf_in)
​
    finally:
        for cdf in cdf_in:
            cdf.close()
​
​
def _merge_cdf(cdf_out, cdf_info, *cdf_in):
    """ Merge multiple CDF files in one. """
    write_global_attributes(cdf_out, cdf_info['Attributes'])
​
    for variable, vinfo in cdf_info['Variables'].items():
        write_variable(
            cdf_out, variable, vinfo,
            numpy.concatenate([cdf.varget(variable) for cdf in cdf_in])
        )
​
​
def write_variable(cdf, name, info, data):
    """ Write new CDF variable. """
    data = CDF_TYPE_FIX.get(info.get('Data_Type'), lambda a: a)(data)
    var_spec = {
        'Variable': name,
    }
    var_spec.update(CDF_VAR_SPEC)
    var_spec.update(info)
    attrs = var_spec.pop('Attributes')
    cdf.write_var(var_spec, attrs, data)
​
​
def write_global_attributes(cdf, attrs):
    """ Write global CDF attributes. """
    cdf_attrs = {
        'CREATED': {0: datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'},
        'CREATOR': {0: CREATOR},
    }
​
    for key, value in attrs.items():
        if isinstance(value, list):
            cdf_attrs[key] = {idx: item for idx, item in enumerate(value)}
        else:
            cdf_attrs[key] = {0: value}
​
    cdf.write_globalattrs(cdf_attrs)
​
​
def extract_common_info(*cdf_in):
    """ Extra common info from the input CDF files. """
    print(merge_vires_global_attrs(*cdf_in))
    return {
        "Attributes": merge_vires_global_attrs(*cdf_in),
        "Variables": merge_variable_infos(*cdf_in),
    }
​
​
def merge_vires_global_attrs(*cdf_in):
    """ Merge VirES specific global attributes of the given CDFs. """
​
    def _format_timestamp(value):
        return value.replace('-', '').replace(':', '')[:15]
​
    def _to_list(value):
        return value if isinstance(value, list) else [value]
​
    def _merge_timespan(timespan0, timespan1):
        start0, end0 = timespan0
        start1, end1 = timespan1
        return (min(start0, start1), max(end0, end1))
​
    iter_cdf_in = iter(cdf_in)
​
    attrs = dict(next(iter_cdf_in).globalattsget())
​
    match = RE_TITILE.match(attrs.get('TITLE', ''))
    if match:
        head, _, _, tail = match.groups()
        title = "%s%%s_%%s%s" % (head, tail)
    else:
        title = "VIRES_%s_%s.cdf"
​
    models = _to_list(attrs.get('MAGNETIC_MODELS', []))
    products = set(_to_list(attrs.get('ORIGINAL_PRODUCT_NAMES', [])))
    timespan = tuple(attrs['DATA_TIMESPAN'].split("/"))
    sources = _to_list(attrs.get('SOURCES', []))
    filters = _to_list(attrs.get('DATA_FILTERS', []))
​
    for cdf in iter_cdf_in:
        attrs = dict(cdf.globalattsget())
        if models != attrs.get('MAGNETIC_MODELS'):
            raise CdfError('MAGNETIC_MODELS mismatch!')
        if sources != attrs.get('SOURCES'):
            raise CdfError('SOURCES mismatch!')
        if filters != attrs.get('DATA_FILTERS'):
            raise CdfError('DATA_FILTERS mismatch!')
        products.update(_to_list(attrs.get('ORIGINAL_PRODUCT_NAMES', [])))
        timespan = _merge_timespan(timespan, attrs['DATA_TIMESPAN'].split("/"))
​
    return {
        'TITLE': title % tuple(_format_timestamp(ts) for ts in timespan),
        'SOURCES': sources,
        'MAGNETIC_MODELS': models,
        'ORIGINAL_PRODUCT_NAMES': sorted(products),
        'DATA_FILTERS': filters,
        'DATA_TIMESPAN': '%s/%s' % timespan,
    }
​
​
def merge_variable_infos(*cdf_in):
    """ Read info from multiple CDF files and merge it into one. """
    iter_cdf = iter(cdf_in)
    vinfo = extract_variables_info(next(iter_cdf))
    for cdf in iter_cdf:
        if vinfo != extract_variables_info(cdf):
            raise CdfError("Non-compatible CDF variables!")
    return vinfo
​
​
def extract_variables_info(cdf):
    """ Read variable information from a CDF file. """
​
    def _extract_variable_info(name):
        vinfo = cdf.varinq(name)
        vinfo = {
            key: vinfo[key] for key in [
                'Var_Type',
                'Data_Type',
                'Num_Elements',
                'Num_Dims',
                'Dim_Sizes',
                'Sparse',
                'Dim_Vary',
                'Rec_Vary',
            ]
        }
        vinfo['Attributes'] = cdf.varattsget(name)
        return vinfo
​
    return {
        variable: _extract_variable_info(variable)
        for variable in cdf.cdf_info()['zVariables']
    }
​
​
def main(*params):
    """ Main subroutine. """
    merge_cdf_files(*params)
​
​
if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
