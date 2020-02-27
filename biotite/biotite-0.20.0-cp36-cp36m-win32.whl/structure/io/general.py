# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

"""
This module contains a convenience function for loading structures from
general structure files.
"""

__name__ = "biotite.structure.io"
__author__ = "Patrick Kunzmann"
__all__ = ["load_structure", "save_structure"]

import os.path
import io
from ..atoms import AtomArray, AtomArrayStack


def load_structure(file_path, template=None, **kwargs):
    """
    Load an :class:`AtomArray` or class`AtomArrayStack` from a structure
    file without the need to manually instantiate a :class:`File`
    object.
    
    Internally this function uses a :class:`File` object, based on the
    file extension.
    Trajectory files furthermore require specification of the `template`
    parameter.
    
    Parameters
    ----------
    file_path : str
        The path to structure file.
    template : AtomArray or AtomArrayStack or file-like object or str, optional
        Only required when reading a trajectory file.
    kwargs
        Additional parameters will be passed to either the
        :func:`get_structure()` or :func:`read()` method of the file
        object.
        This does not affect files given via the `template` parameter.
    
    Returns
    -------
    array : AtomArray or AtomArrayStack
        If the file contains multiple models, an AtomArrayStack is
        returned, otherwise an AtomArray is returned.
    
    Raises
    ------
    ValueError
        If the file format (i.e. the file extension) is unknown.
    TypeError
        If a trajectory file is loaded without specifying the
        `template` parameter.
    """
    # Optionally load template from file
    if isinstance(template, (io.IOBase, str)):
        template = load_structure(template)

    # We only need the suffix here
    _, suffix = os.path.splitext(file_path)
    if suffix == ".pdb":
        from .pdb import PDBFile
        file = PDBFile()
        file.read(file_path)
        array = file.get_structure(**kwargs)
        if isinstance(array, AtomArrayStack) and array.stack_depth() == 1:
            # Stack containing only one model -> return as atom array
            return array[0]
        else:
            return array
    elif suffix == ".cif" or suffix == ".pdbx":
        from .pdbx import PDBxFile, get_structure
        file = PDBxFile()
        file.read(file_path)
        array = get_structure(file, **kwargs)
        if isinstance(array, AtomArrayStack) and array.stack_depth() == 1:
            # Stack containing only one model -> return as atom array
            return array[0]
        else:
            return array
    elif suffix == ".gro":
        from .gro import GROFile
        file = GROFile()
        file.read(file_path)
        array = file.get_structure(**kwargs)
        if isinstance(array, AtomArrayStack) and array.stack_depth() == 1:
            # Stack containing only one model -> return as atom array
            return array[0]
        else:
            return array
    elif suffix == ".mmtf":
        from .mmtf import MMTFFile, get_structure
        file = MMTFFile()
        file.read(file_path)
        array = get_structure(file, **kwargs)
        if isinstance(array, AtomArrayStack) and array.stack_depth() == 1:
            # Stack containing only one model -> return as atom array
            return array[0]
        else:
            return array
    elif suffix == ".npz":
        from .npz import NpzFile
        file = NpzFile()
        file.read(file_path)
        array = file.get_structure(**kwargs)
        if isinstance(array, AtomArrayStack) and array.stack_depth() == 1:
            # Stack containing only one model -> return as atom array
            return array[0]
        else:
            return array
    elif suffix in [".trr", ".xtc", ".tng", ".dcd", ".netcdf"]:
        if template is None:
            raise TypeError("Template must be specified for trajectory files")
        from .trr import TRRFile
        from .xtc import XTCFile
        from .tng import TNGFile
        from .dcd import DCDFile
        from .netcdf import NetCDFFile
        if suffix == ".trr":
            traj_file_cls = TRRFile
        if suffix == ".xtc":
            traj_file_cls = XTCFile
        if suffix == ".tng":
            traj_file_cls = TNGFile
        if suffix == ".dcd":
            traj_file_cls = DCDFile
        if suffix == ".netcdf":
            traj_file_cls = NetCDFFile
        file = traj_file_cls()
        file.read(file_path, **kwargs)
        return file.get_structure(template)
    else:
        raise ValueError(f"Unknown file format '{suffix}'")


def save_structure(file_path, array, **kwargs):
    """
    Save an :class:`AtomArray` or class`AtomArrayStack` to a structure
    file without the need to manually instantiate a :class:`File`
    object.
    
    Internally this function uses a :class:`File` object, based on the
    file extension.
    
    Parameters
    ----------
    file_path : str
        The path to structure file.
    array : AtomArray or AtomArrayStack
        The structure to be saved.
    kwargs
        Additional parameters will be passed to the respective `set_structure`
        method.

    Raises
    ------
    ValueError
        If the file format (i.e. the file extension) is unknown.
    """
    # We only need the suffix here
    _, suffix = os.path.splitext(file_path)
    if suffix == ".pdb":
        from .pdb import PDBFile
        file = PDBFile()
        file.set_structure(array, **kwargs)
        file.write(file_path)
    elif suffix == ".cif" or suffix == ".pdbx":
        from .pdbx import PDBxFile, set_structure
        file = PDBxFile()
        set_structure(file, array, data_block="STRUCTURE", **kwargs)
        file.write(file_path)
    elif suffix == ".gro":
        from .gro import GROFile
        file = GROFile()
        file.set_structure(array, **kwargs)
        file.write(file_path)
    elif suffix == ".mmtf":
        from .mmtf import MMTFFile, set_structure
        file = MMTFFile()
        set_structure(file, array, **kwargs)
        file.write(file_path)
    elif suffix == ".npz":
        from .npz import NpzFile
        file = NpzFile()
        file.set_structure(array, **kwargs)
        file.write(file_path)
    elif suffix in [".trr", ".xtc", ".tng", ".dcd", ".netcdf"]:
        from .trr import TRRFile
        from .xtc import XTCFile
        from .tng import TNGFile
        from .dcd import DCDFile
        from .netcdf import NetCDFFile
        if suffix == ".trr":
            traj_file_cls = TRRFile
        if suffix == ".xtc":
            traj_file_cls = XTCFile
        if suffix == ".tng":
            traj_file_cls = TNGFile
        if suffix == ".dcd":
            traj_file_cls = DCDFile
        if suffix == ".netcdf":
            traj_file_cls = NetCDFFile
        file = traj_file_cls()
        file.set_structure(array, **kwargs)
        file.write(file_path)
    else:
        raise ValueError(f"Unknown file format '{suffix}'")