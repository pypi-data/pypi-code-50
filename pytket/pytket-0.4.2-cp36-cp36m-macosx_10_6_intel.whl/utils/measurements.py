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

import numpy as np
from typing import Iterable, Tuple
from pytket import Circuit, UnitID
from openfermion import QubitOperator

def append_pauli_measurement(pauli_string:Iterable[Tuple[int,str]], circ:Circuit) :
    """Appends measurement instructions to a given circuit, measuring each qubit in a given basis.
    
    :param pauli_string: The pauli operator to measure, as tuples of pauli name and qubit.
    :type pauli_string: Iterable[Tuple[int,str]]
    :param circ: Circuit to add measurement to.
    :type circ: Circuit
    """
    measured_qbs = []
    measures_set = set()
    for qb_idx, p in pauli_string :
        if qb_idx in measures_set :
            raise ValueError("Pauli string contains qubit " + str(qb_idx) + " multiple times")
        measured_qbs.append(qb_idx)
        measures_set.add(qb_idx)
        if p=='X':
            circ.H(qb_idx)
        elif p=='Y':
            circ.Rx(0.5, qb_idx)
    bits = circ.bits
    for b_idx, qb_idx in enumerate(measured_qbs):
        unit = UnitID('c', b_idx)
        if unit not in bits :
            circ.add_bit(unit)
        circ.Measure(qb_idx, b_idx)

def _all_pauli_measurements(operator:QubitOperator, circ:Circuit) -> Iterable[Circuit] :
    """For each term in the operator, yields a copy of the given circuit with the appropriate measurements on each qubit. The trivial term is omitted.
    
    :param operator: The operator
    :type operator: QubitOperator
    :param circ: The circuit generating the desired state
    :type circ: Circuit
    :return: Pairs of term from the operator and corresponding circuit
    :rtype: Iterable[Tuple[Iterable[Tuple[int,str]], Circuit]]
    """
    for pauli, _ in operator.terms.items() :
        if not pauli :
            continue
        copy = circ.copy()
        append_pauli_measurement(pauli, copy)
        yield copy
