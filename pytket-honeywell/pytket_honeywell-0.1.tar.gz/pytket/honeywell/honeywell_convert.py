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

""" Conversion from :math:`\\mathrm{t|ket}\\rangle` to Honeywell
"""

from io import StringIO

from pytket.circuit import Circuit, OpType
from pytket.passes import (FlattenRegisters, RebaseHQS, RemoveRedundancies,
                           SequencePass, gen_rebase_pass)
from pytket.qasm.qasm import circuit_to_qasm_io

# Flatten registers, rebase to the Honeywell gate set, and remove redundancies
honeywell_pass = SequencePass(
    [
        # FlattenRegisters(),
        RebaseHQS(),
        RemoveRedundancies(),
    ]
)


def translate_honeywell(circ: Circuit) -> str:
    """ Convert a circuit in the Honeywell gateset to a honeywell qasm string """
    with StringIO() as s:
        circuit_to_qasm_io(circ, s, header='hqslib1')
        stri = s.getvalue()
    return stri


def tk_to_honeywell(circ: Circuit) -> str:
    """ Convert a circuit to Honeywell QASM representation """
    c = circ.copy()
    honeywell_pass.apply(c)
    return translate_honeywell(c)
