# Copyright 2020 Cambridge Quantum Computing
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

import pytest
from pytket.circuit import Circuit, OpType
from pytket.honeywell import tk_to_honeywell


def test_convert():
    circ = Circuit(4)
    circ.H(0).CX(0, 1)
    circ.CRz(0.5, 1, 2)
    # circ.add_barrie   r([2])
    circ.ZZPhase(0.3, 2, 3).CX(3, 0).Tdg(1)
    circ.measure_all()

    circ_hqs = tk_to_honeywell(circ)
    qasm_str = circ_hqs.split('\n')[6:-1]
    test = True
    for com in qasm_str:
        test &= any(com.startswith(gate) for gate in ('rz', 'U1q', 'ZZ', 'measure', 'barrier'))
    assert test


if __name__ == "__main__":
    test_convert()
