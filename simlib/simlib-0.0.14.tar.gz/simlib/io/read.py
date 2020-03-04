"""
read.py
written in Python3
author: C. Lockhart <chris@lockhartlab.org>
"""

from simlib.framework import Structure, Topology, Trajectory

import numpy as np
import pandas as pd
import re


# Read PDB
# TODO currently the only backend will by pandas; in future, expand to Cython or C or Fortran backend
def read_pdb(filename, backend='pandas'):
    """
    Read PDB file and return Trajectory

    PDB format can be described in depth at `<http://www.wwpdb.org/documentation/file-format>`_.

    Parameters
    ----------
    filename : str
        Name of PDB file to be read
    backend : str
        (Default: 'pandas').

    Returns
    -------
    simlib.Trajectory
        Trajectory of PDB
    """

    # Make sure we know we're using the pandas backend
    if backend.lower() != 'pandas':
        raise AttributeError('only pandas backend presently supported')

    # Open file, read in all records
    with open(filename, 'r') as buffer:
        records = buffer.read()

    # Filter out atom records
    # TODO this will be slow for large PDB files; perhaps move to Cython or C backend
    atoms = re.sub(r'^(?!ATOM).*$', '', records, flags=re.MULTILINE).replace('\n\n', '\n').lstrip()

    # Sections of PDB
    sections = np.array([
        (6, 'record', '<U6'),
        (5, 'atom_id', 'int'),
        (5, 'atom', '<U5'),
        (5, 'residue', '<U5'),
        (1, 'chain', '<U1'),
        (4, 'residue_id', 'int'),
        (4, 'blank', '<U1'),
        (8, 'x', 'float'),
        (8, 'y', 'float'),
        (8, 'z', 'float'),
        (6, 'alpha', 'float'),
        (6, 'beta', 'float'),
        (9, 'segment', '<U9'),
        (2, 'element', '<U2')
    ], dtype=[('width', 'i1'), ('column', '<U10'), ('type', '<U10')])

    # Read in
    data = np.genfromtxt(atoms.split('\n'), delimiter=sections['width'], dtype=sections['type'], autostrip=True)
    data = pd.DataFrame(data.tolist(), columns=sections['column'])

    # Drop extraneous columns
    data = data.drop(columns='blank')

    # TODO this should also be done for residue_id probably
    # If the PDB starts at atom_id = 1, change to 0-index
    if data['atom_id'].min() == 1:
        data['atom_id'] -= 1

    # Determine number of structures in PDB
    n_structures = data.pivot_table(index='atom_id', values='record', aggfunc='count')['record'].unique()
    if len(n_structures) != 1:
        raise AttributeError('inconsistent record counts in PDB')
    n_structures = n_structures[0]

    # Separate out dynamic columns for Trajectory and static Topology data
    dynamical_columns = ['x', 'y', 'z']
    static_columns = [column for column in data.columns if column not in dynamical_columns]

    # Create Topology first
    topology = Topology(data[static_columns].drop_duplicates())

    # Next create Trajectory (the result)
    n_atoms = data['atom_id'].nunique()
    result = Trajectory(data[dynamical_columns].values.reshape(n_structures, n_atoms, 3), topology=topology)

    # Return
    return result
