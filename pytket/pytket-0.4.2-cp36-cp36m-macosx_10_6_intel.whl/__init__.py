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
"""Python Interface to CQC t|ket>
"""

from pytket.circuit import (Circuit, OpType, Pauli, CircBox, Unitary2qBox,
    ExpBox, PauliExpBox, UnitID, BasisOrder)
from pytket.routing import route, Architecture, Placement
from pytket.transform import Transform
from pytket.device import Device
from pytket.predicates import (GateSetPredicate, NoClassicalControlPredicate,
                                NoFastFeedforwardPredicate, NoClassicalBitsPredicate, NoWireSwapsPredicate,
                                MaxTwoQubitGatesPredicate, ConnectivityPredicate, DirectednessPredicate,
                                CliffordCircuitPredicate,
                                UserDefinedPredicate, CompilationUnit)
from pytket.passes import (SequencePass, RepeatPass, RepeatWithMetricPass, RepeatUntilSatisfiedPass, BasePass,
                                SynthesiseIBM, SynthesiseHQS, _SynthesiseOQC, SynthesiseUMD,
                                RebaseCirq, RebaseTket, RebaseIBM, RebaseQuil, RebasePyZX, RebaseProjectQ,
                                RebaseHQS, RebaseUMD, PauliSimp, DecomposeSingleQubitsIBM, DecomposeBoxes,
                                OptimisePhaseGadgets, RemoveRedundancies, FullPeepholeOptimise,
                                CommuteThroughMultis, DecomposeArbitrarilyControlledGates,
                                DecomposeMultiQubitsIBM, USquashIBM, gen_clifford_simp_pass,
                                gen_rebase_pass, gen_routing_pass, gen_directed_cx_routing_pass,
                                gen_decompose_routing_gates_to_cxs_pass, gen_user_defined_swap_decomp_pass,
                                gen_placement_pass, gen_full_mapping_pass, gen_default_mapping_pass)
from pytket.qasm import circuit_from_qasm, circuit_to_qasm
from pytket.quipper import circuit_from_quipper
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

def O1Pass() -> BasePass :
    """A recommended, all-purpose circuit optimisation pass for fast compilation.
    Compiles to the gateset {CX, tk1, Reset, Measure}.
    This should be applied before the default compilation pass of the target backend.
    
    :return: An optimisation pass that performs only basic circuit simplifications for basic usage.
    :rtype: BasePass
    """    
    return SequencePass([SynthesiseIBM(), RebaseTket()])

def O2Pass() -> BasePass :
    """A recommended, all-purpose circuit optimisation pass for thorough compilation.
    Compiles to the gateset {CX, tk1, Reset, Measure}.
    This should be applied before the default compilation pass of the target backend.
    
    :return: An optimisation pass that performs local circuit simplification techniques.
    :rtype: BasePass
    """    
    return SequencePass([FullPeepholeOptimise(), RebaseTket()])
