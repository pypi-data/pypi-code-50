import gzip
import warnings
from urllib.error import URLError
from urllib.request import urlopen

import pandas as pd
from lxml import etree
from pandas.io.common import (_infer_compression, _is_url,
                              get_filepath_or_buffer)


ATTR_TYPES = ['infer', 'global']


def _is_float(a):
    try:
        num = float(a)
    except ValueError:
        return False
    return True


def _is_int(a):
    try:
        num = int(a)
    except ValueError:
        return False
    return True


def _infer_type(value):
    res = value
    if _is_float(value):
        res = float(value)
    if _is_int(value):
        res = int(value)
    return res


def _get_attrib(element, expected_attribs=None):
    attrib = {}
    if element.attrib and 'key' in element.attrib and 'value' in element.attrib:
        if expected_attribs is None or element.attrib['key'] in expected_attribs:
            value = _infer_type(element.attrib['value'])
            kv_pair = {element.attrib['key']: value}
            attrib.update(kv_pair)
    return attrib


def _get_attribs(element, expected_attribs=None):
    attribs = {}

    if not element:
        element = [element]

    for child in element:
        attrib = _get_attrib(child, expected_attribs)
        attribs.update(attrib)

    return attribs


def _get_columns(tree, trace_attrs, event_attrs):
    _trace_attrs, _event_attrs = set(), set()
    _has_found_trace_attrs, _has_found_event_attrs = False, False

    for child in tree:
        if _has_found_trace_attrs and _has_found_event_attrs:
            break

        if "global" in child.tag and 'scope' in child.attrib:
            if child.attrib['scope'] == 'trace':
                _global_trace_attrs = _get_attribs(child)
                _has_found_trace_attrs = True if event_attrs == "global" else False

            if child.attrib['scope'] == 'event':
                _global_event_attrs = _get_attribs(child)
                _has_found_event_attrs = True if trace_attrs == "global" else False

        if "trace" in child.tag:
            if trace_attrs == "infer":
                for el in child:
                    if 'key' in el.attrib:
                        _trace_attrs.add(el.attrib['key'])

            if event_attrs == "infer":
                for el in child:
                    if 'event' not in el.tag:
                        continue
                    attr_set = set(x.attrib['key']
                                   for x in el if 'key' in x.attrib)
                    _event_attrs = _event_attrs.union(attr_set)

    if trace_attrs == "global":
        _trace_attrs = _global_trace_attrs
    elif trace_attrs != "infer":
        for attr in trace_attrs:
            if attr not in _global_trace_attrs:
                warnings.warn("Trace attribute '{}' not in the global trace attribute.".format(
                    attr), UserWarning)
        _trace_attrs = trace_attrs

    if event_attrs == "global":
        _event_attrs = _global_event_attrs
    elif event_attrs != "infer":
        for attr in event_attrs:
            if attr not in _global_event_attrs:
                warnings.warn("Event attribute '{}' not in the global event attribute.".format(
                    attr), UserWarning)
        _event_attrs = event_attrs

    return list(_trace_attrs), list(_event_attrs)


def _get_case(trace, trace_attribs=None, event_attribs=None):
    case = {
        'events': []
    }

    for child in trace:
        if 'event' in child.tag:
            event = _get_attribs(child, event_attribs)
            case['events'].append(event)
            continue
        attrib = _get_attribs(child, trace_attribs)
        case.update(attrib)
    return case


def _to_dataframe(cases, trace_attribs, event_attribs):
    columns = ["T_" + x for x in trace_attribs] + \
        ["E_" + x for x in event_attribs]
    data = []

    for case in cases:
        base = []
        for k in trace_attribs:
            if k in case:
                base.append(case[k])
            else:
                base.append('UNK')
        # TODO: Check for missing events in case/trace:
        for event in case['events']:
            entry = [] + base
            for k in event_attribs:
                if k in event:
                    entry.append(event[k])
                else:
                    entry.append('UNK')
            data.append(entry)

    return pd.DataFrame(data=data, columns=columns)


def _read_xes(tree, trace_attrs, event_attrs):
    trace_attrs, event_attrs = _get_columns(
        tree, trace_attrs, event_attrs)

    cases = []
    for el in tree:
        if "trace" in el.tag:
            case = _get_case(el, trace_attrs, event_attrs)
            cases.append(case)

    return _to_dataframe(cases, trace_attrs, event_attrs)


def read_xes(filepath: str, trace_attrs='infer', event_attrs='infer') -> pd.DataFrame:
    """Read an eXtensible event stream (xes) file into DataFrame.

    Parameters
    ----------
    filepath : str, path object or file-like object
        Any valid string path is acceptable. The string could be a URL. Valid
        URL schemes include http and file. For file URLs, a host is
        expected. A local file could be: file://localhost/path/to/table.csv.

        If you want to pass in a path object, pyromorphite accepts any ``os.PathLike``.

        By file-like object, we refer to objects with a ``read()`` method, such as
        a file handler (e.g. via builtin ``open`` function) or ``StringIO``.
        
    trace_attrs, event_attrs : 'infer', 'global' or list of names, default 'infer'
        Specifies the attributes to pick for the dataframe's columns. The 
        behaviour is as follows:

        * 'infer'. If passed, the column names will be composed of the union
        of all the attributes found on each trace, as well as each individual
        event. 
        * 'global'. If passed, the column names will be extracted from the
        global tags found in the xes file.
        * list of names. Names that match the attributes of the traces or
        events in the xes file.  

        Trace attributes and/or event attributes to be extracted from traces,
        respectively events present in the xes file.

    Returns
    -------
    DataFrame 
        A eXtensible event stream (xes) file is returned as two-dimensional
        data structure with labeled axes.

    Warns
    -----
    UserWarning
        In the case that trace_attrs or event_attrs is a list of names, warn
        if name in list is not present in global tag.

    Examples
    --------
    >>> log = pm.read_xes('data.xes') # doctest: +SKIP
    """
    if not (trace_attrs in ATTR_TYPES or
            hasattr(trace_attrs, "__getitem__") or
            hasattr(trace_attrs, "__iter__")):
        raise ValueError(
            "`trace_attrs` can either be 'infer', 'global' or a list-like object.")

    if not (event_attrs in ATTR_TYPES or
            hasattr(event_attrs, "__getitem__") or
            hasattr(event_attrs, "__iter__")):
        raise ValueError(
            "`event_attrs` can either be 'infer', 'global' or a list-like object.")

    root = _get_xml_tree(filepath)

    return _read_xes(root, trace_attrs, event_attrs)


def _get_xml_tree(filepath):

    if _is_url(filepath):
        tree = urlopen(filepath)
        content_encoding = tree.headers.get("Content-Type", None)
        if "gzip" in content_encoding:
            with gzip.open(tree) as f:
                content = f.read()
                return etree.fromstring(content)

    return etree.parse(filepath).getroot()


