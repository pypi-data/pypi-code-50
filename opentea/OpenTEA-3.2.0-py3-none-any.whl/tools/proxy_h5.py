""" Module container for class ProxyH5
"""
import warnings
import h5py
from opentea.tools.visit_h5 import (pprint_dict,
                                    log_hdf_node,
                                    h5_node_to_dict,
                                    hdf5_query_field,
                                    h5_datasets_names)


class ProxyH5():
    """Class container for hdf5 file inspector

       Parameters :
       ===========
       h5_filename : Path to hdf5 file
    """
    def __init__(self, h5_filename):
        warnings.warn(
            "ProxyH5 is deprecated, move to hdfdict for h5 quick access")
        with h5py.File(h5_filename, 'r') as node:
            self.nob = h5_node_to_dict(node)
            self._structure = log_hdf_node(node)
            self.datatsets_names = h5_datasets_names(node)

    def show(self, style=None):
        """ Pretty print of the hdf5 content

            Parameters :
            ==========
            style : style of printing, possible options
                    - yaml : for a yaml formatting
                    - json : for a yaml formatting
                    - None : for a default printing
        """
        pprint_dict(self._structure, style=style)

    def get_field(self, identifier):
        """ Get a value of a field given its identifier

            Parameters:
            ==========
            identifier : the adress of the content to retrieve.

                    Possible options:
                        - String : key of the value to retrieve
                         (e.g 'content')

                        - String : A posix-like full address
                          (e.g 'full/address/to/content')

                        - List : A list of adress stages, complete or not
                          (e.g ['full', 'address', 'to', 'content'] or,
                           ['content'])

                        - A list of lists : a list holding address stages,
                          as it is done for instance in h5py.
                          (e.g [['full'], ['address'], ['to'], ['content']]])
            Returns:
            =======
            field : array or value of the query field
        """
        return hdf5_query_field(self.nob, identifier)


def test():
    """ example of usage
    """
    filename = "/Users/erraiya/Desktop/HULK/hulk/hulk/Data/solut_00027500.h5"
    prox = ProxyH5(filename)
    prox.show(style='yaml') #style="yaml"
    print(prox.get_field(['GaseousPhase', 'rhou']))
    print(prox.get_field('GaseousPhase/rhou'))
    print(prox.get_field([['GaseousPhase'], ['rhou']]))
    print(prox.get_field('rhou'))

if __name__ == '__main__':
    test()
