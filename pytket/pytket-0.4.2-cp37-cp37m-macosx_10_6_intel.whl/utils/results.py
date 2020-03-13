# Copyright 2019 Cambridge Quantum Computing
#
# Licensed under a Non-Commercial Use Software Licence (the "Licence");
# you may not use this file except in compliance with the Licence.
# You may obtain a copy of the Licence in the LICENCE file accompanying
# these documents or at:
#
#     https://cqcl.github.io/pytket/build/html/licence.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence, but note it is strictly for non-commercial use.
from typing import Dict, List, Tuple
import numpy as np
import math

def counts_from_shot_table(shot_table : np.ndarray) -> Dict[Tuple[int, ...], int] :
    """Summarises a shot table into a dictionary of counts for each observed outcome.
    
    :param shot_table: Table of shots from a pytket backend.
    :type shot_table: np.ndarray
    :return: Dictionary mapping observed readouts to the number of times observed.
    :rtype: Dict[Tuple[int, ...], int]
    """
    shot_values, counts = np.unique(shot_table, axis=0, return_counts=True)
    return {tuple(s):c for s, c in zip(shot_values, counts)}

def probs_from_counts(counts : Dict[Tuple[int, ...], int]) -> Dict[Tuple[int, ...], float] :
    """Converts raw counts of observed outcomes into the observed probability distribution.
    
    :param counts: Dictionary mapping observed readouts to the number of times observed.
    :type counts: Dict[Tuple[int, ...], int]
    :return: Probability distribution over observed readouts.
    :rtype: Dict[Tuple[int, ...], float]
    """
    total = np.sum([c for _, c in counts.items()])
    return {outcome : c/total for outcome, c in counts.items()}

def _index_to_outcome(index : int, width : int) -> Tuple[int, ...] :
    bitstring = "{0:b}".format(index).zfill(width)
    return tuple([int(b) for b in bitstring])

def probs_from_state(state : np.ndarray) -> Dict[Tuple[int, ...], float] :
    """Converts statevector to the probability distribution over readouts in the computational basis. Ignores probabilities lower than 1e-10.
    
    :param state: Full statevector with little-endian encoding.
    :type state: np.ndarray
    :return: Probability distribution over readouts.
    :rtype: Dict[Tuple[int, ...], float]
    """
    width = int(math.log2(len(state)))
    if 2**width != len(state) :
        raise ValueError("Length of statevector is not a power of 2")
    probs = {_index_to_outcome(i, width) : abs(coeff)**2 for i, coeff in enumerate(state) if abs(coeff)**2 >= 1e-10}
    if not math.isclose(np.sum([p for _, p in probs.items()]), 1.) :
        raise ValueError("Statevector is not normalised")
    return probs

def permute_qubits_in_statevector(state:np.ndarray, permutation:List[int]) -> np.ndarray :
    """Rearranges a statevector according to a permutation of the qubit indices.
    
    :param state: Original statevector.
    :type state: np.ndarray
    :param permutation: Map from current qubit index (little-endian) to its new position, encoded as a list.
    :type permutation: List[int]
    :return: Updated statevector.
    :rtype: np.ndarray
    """
    s = np.copy(state)
    dim = len(s)
    n_qb = int(np.log2(dim))
    if 2**n_qb != len(state) :
        raise ValueError("Length of statevector is not a power of 2")
    if len(permutation) != n_qb :
        raise ValueError("Invalid permutation: length does not match number of qubits")
    idx_found = set()
    for i in permutation :
        if i >= n_qb :
            raise ValueError("Invalid permutation: invalid index")
        if i in idx_found :
            raise ValueError("Invalid permutation: repeated index")
        idx_found.add(i)
    for i in range(dim) :
        basis_bin = "{0:b}".format(i).zfill(n_qb)
        basis_bin = [i for i in basis_bin]
        basis_bin.reverse()
        new_basis_bin = ['0']*n_qb
        for start, end in enumerate(permutation) :
            new_basis_bin[end] = basis_bin[start]
        new_basis_bin.reverse()
        j = int(''.join(new_basis_bin), 2)
        s[j] = state[i]
    return s

def reverse_permutation_matrix(n_qubits:int) -> np.ndarray :
    """Returns a permutation matrix to reverse the order of qubits.
    
    :param n_qubits: Number of qubits in system
    :type n_qubits: int
    :return: Permutation matrix
    :rtype: np.ndarray
    """    
    dim = 2**n_qubits
    m = np.zeros([dim, dim])
    for i in range(dim) :
        index = int('{0:b}'.format(i).zfill(n_qubits)[::-1], 2)
        m[i][index] = 1
    return m
