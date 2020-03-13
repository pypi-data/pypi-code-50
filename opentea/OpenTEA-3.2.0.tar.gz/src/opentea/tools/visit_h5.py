"""Visit h5py file"""
import sys
import json
import h5py
import numpy as np
import yaml
from opentea.noob.asciigraph import nob_asciigraph
from opentea.noob.noob import nob_get

class H5LookupError(Exception):
    """ Exception class for h5 lookup
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def ascii2string(ascii_list):
    """ Ascii to string conversion

        Parameters:
        -----------
        ascii_list : a list of string to be converted

        Returns:
        --------
        a string joining the list elements

    """
    return ''.join(chr(i) for i in ascii_list[:-1])

def get_node_description(node):
    """Get number of elements in an array or
      value of a single-valued node.

    Parameters:
    -----------
    node : hdf5 node

    Returns:
    --------
    a value with a Python format
    None if data is not a singlevalued quantity
    """
    out = None
    value = node[()]
    shape = node.shape
    if np.prod(shape) == 1:
        # this is a strong assumption because if you find int8
        # your are probably looking at an hdf5 file applying the cgns standard
        if node.dtype in ["int8"]:
            out = np.char.array(ascii2string(value))[0]
        elif shape in [(1), (1,)]:
            if node.dtype in ["int32", "int64"]:
                out = int(value[0])
            elif node.dtype in ["float32", "float64"]:
                out = float(value[0])
    else:
        out = "array of %s elements" %(" x ".join([str(k) for k in shape]))
    return out

def log_hdf_node(node):
    """
    Build a dictionnary with the structure of a HDF5 node

    Parameters:
    -----------
    node : hdf5 node

    Returns:
    --------
    a dictionnary
    """
    out = dict()

    def extend_dict(dict_, address, attr):
        tmp = dict_
        for key in address[:]:
            if key not in tmp:
                #tmp[key] = dict()
                tmp[key] = attr.copy()
            tmp = tmp[key]

    def visitor_func(name, node):
        key_list = [item.strip() for item in name.split('/')]
        if isinstance(node, h5py.Dataset):
            attr = dict()
            attr["dtype"] = str(node.dtype)
            attr["value"] = get_node_description(node)
            extend_dict(out, key_list, attr)
        else:
            pass

    node.visititems(visitor_func)

    return out

def hdf5_query_field(node, address):
    """Get the content of the adress

    Parameters:
    -----------
    node : hdf5 node
    address : the adress of the content to retrieve. Possible options:
                - String : key of the value to retrieve (e.g 'content')
                - String : A posix-like full address
                  (e.g 'full/address/to/content')
                - List : A list of adress stages, complete or not
                  (e.g ['full', 'address', 'to', 'content'] or, ['content'])
                - A list of lists : a list holding address stages, as it is
                  done for instance in h5py.
                  (e.g [['full'], ['address'], ['to'], ['content']]])

    Returns:
    --------
    content of the address
    """
    if isinstance(address, str):
        keys = address.split('/')
    elif isinstance(address, list):
        if all([isinstance(item, str) for item in address]):
            keys = address
        else:
            keys = [item for sublist in address for item in sublist]
    else:
        msg = 'Unknown address %s !\n' %str(address)
        msg = msg + 'address should be a list of keys or a string'
        raise H5LookupError(msg)

    return nob_get(node, *keys, failsafe=False)

def pprint_dict(dict_, style=None):
    """Pretty pring a dictionnary using yaml or json formatting"""
    if style == "json":
        lines = json.dumps(dict_, indent=4)
    elif style == "yaml":
        lines = yaml.dump(dict_, default_flow_style=False)
    else:
        lines = nob_asciigraph(dict_)
        lines = lines.replace('dtype (str)', 'dtype')
        lines = lines.replace('value (str)', 'value')
        lines = lines.replace(' (dict)\n', '\n')
    print(lines)

def h5_node_to_dict(node):
    """Read hdf5 node values and structure into a dictionnary

        Parameters:
        ==========
        node : hdf5 node

        Returns:
        =======
        data_dict : a dictionnary holding the data
    """
    def _get_datasets(buf=None, data_dict=None, path_=""):
        if data_dict is None:
            data_dict = dict()

        for gname, group in buf.items():
            data_dict[gname] = dict()
            path = path_ + "/" + gname
            if not isinstance(group, h5py.Dataset):
                _get_datasets(buf[gname], data_dict[gname], path_=path)
            else:
                if buf[path][()].size >= 1:
                    data_dict[gname] = buf[path][()]
        return data_dict

    data_dict = _get_datasets(node)

    return data_dict

def h5_datasets_names(node):
    """Get hdf5 node datasets names

        Parameters:
        ==========
        node : hdf5 node

        Returns:
        =======
        ds_names : a list of datasets names
    """

    ds_names = []
    for path, _ in _rec_h5_dataset_iterator(node):
        ds_names.append(path.split('/')[-1].strip())
    return ds_names

def _rec_h5_dataset_iterator(node, prefix=''):
    for key in node.keys():
        item = node[key]
        path = '{}/{}'.format(prefix, key)
        if isinstance(item, h5py.Dataset): # test for dataset
            yield (path, item)
        elif isinstance(item, h5py.Group): # test for group (go down)
            yield from _rec_h5_dataset_iterator(item, path)

def visit_h5(h5_filename):
    """ Show hdf5 file components

        Parameters:
        ----------
        h5_filename : path to hdf5 file to inspect
    """
    with h5py.File(h5_filename) as node:
        pprint_dict(log_hdf_node(node), style="yaml")

if __name__ == "__main__":
    visit_h5(sys.argv[1])
