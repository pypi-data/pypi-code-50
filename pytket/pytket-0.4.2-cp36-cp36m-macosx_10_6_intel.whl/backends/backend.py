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

from abc import ABC, abstractmethod
from pytket import Circuit, BasisOrder
from pytket.predicates import Predicate, CompilationUnit
from pytket.passes import BasePass
from typing import Iterable, Dict, List, Optional, Tuple
import numpy as np

class Backend(ABC) :
    """
    This abstract class defines the structure of a backend as something that
    can run quantum circuits and produce output as at least one of shots,
    counts, state, or unitary
    """

    def __init__(self, shots:bool=False, counts:bool=False, state:bool=False, unitary:bool=False, expectation:bool=False) :
        self._supports_shots = shots
        self._supports_counts = counts
        self._supports_state = state
        self._supports_unitary = unitary
        self._supports_expectation = expectation

    @property
    @abstractmethod
    def required_predicates(self) -> List[Predicate] :
        """The minimum set of predicates that a circuit must satisfy before it can be successfully run on this backend.

        :return: Required predicates.
        :rtype: List[Predicate]
        """
        pass

    def valid_circuit(self, circuit:Circuit) -> bool :
        """Checks that the circuit satisfies all of required_predicates.

        :param circuit: The circuit to check.
        :type circuit: Circuit
        :return: Whether or not all of required_predicates are satisfied.
        :rtype: bool
        """
        return all([pred.verify(circuit) for pred in self.required_predicates])

    @property
    @abstractmethod
    def default_compilation_pass(self) -> BasePass :
        """A suggested compilation pass that will guarantee the resulting circuit will be suitable to run on this backend with as few preconditions as possible.

        :return: Compilation pass guaranteeing required predicates.
        :rtype: BasePass
        """
        pass

    def compile_circuit(self, circuit:Circuit) :
        """Apply the default_compilation_pass to a circuit in place.

        :param circuit: The circuit to compile.
        :type circuit: Circuit
        """
        self.default_compilation_pass.apply(circuit)

    @abstractmethod
    def process_circuits(self, circuits:Iterable[Circuit], n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True) :
        """Submit circuits to the backend for running. The results will be stored in the backend's result cache to be retrieved by the corresponding get_<data> method.

        :param circuits: Circuits to process on the backend.
        :type circuits: Iterable[Circuit]
        :param n_shots: Number of shots to run per circuit. None is to be used for state/unitary simulators. Defaults to None.
        :type n_shots: Optional[int], optional
        :param seed: Seed to set for simulations. None is to be used for quantum hardware or when a seed is not needed. Defaults to None
        :type seed: Optional[int], optional
        :param valid_check: Explicitly check that all circuits satisfy all required predicates to run on the backend. Defaults to True
        :type valid_check: bool, optional
        """
        pass

    @abstractmethod
    def empty_cache(self) :
        """Manually empty the result cache on the backend.
        """
        pass

    @property
    def supports_shots(self) -> bool :
        return self._supports_shots

    def get_shots(self, circuit:Circuit, n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        """Run the circuit on the backend and returns a table of the shots. This will fail if the circuit does not match the device's requirements.
        If results for the circuit are already in the backend's cache from running process_circuits, those will be returned, regardless of the number of shots requested here.

        :param circuit: The circuit to run.
        :type circuit: Circuit
        :param n_shots: Number of shots to generate.
        :type n_shots: Optional[int], optional
        :param seed: Seed to set for simulations. None is to be used for quantum hardware or when a seed is not needed. Defaults to None
        :type seed: Optional[int], optional
        :param valid_check: Explicitly check that the circuit satisfies all of the required predicates before running. Defaults to True.
        :type valid_check: bool, optional
        :param remove_from_cache: Remove the circuit's results from the backend's cache. Defaults to True.
        :type remove_from_cache: bool, optional
        :param basis: Toggle between ILO (increasing lexicographic order of bit ids) and DLO (decreasing lexicographic order) for column ordering. Defaults to BasisOrder.ilo.
        :type basis: BasisOrder, optional
        :return: Table of shot results. Each row is a single shot, with columns ordered by classical bit order (according to `basis`). Entries are 0 or 1 corresponding to qubit basis states.
        :rtype: numpy.ndarray
        """
        raise NotImplementedError("Cannot get shots from this backend")

    @property
    def supports_counts(self) -> bool :
        return self._supports_counts

    def get_counts(self, circuit:Circuit, n_shots:Optional[int]=None, seed:Optional[int]=None, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> Dict[Tuple[int, ...], int] :
        """Run the circuit on the backend and accumulate the shot results into a summary of counts. This will fail if the circuit does not match the device's requirements.
        If results for the circuit are already in the backend's cache from running process_circuits, those will be returned, regardless of the number of shots requested here.

        :param circuit: The circuit to run.
        :type circuit: Circuit
        :param n_shots: Number of shots to generate.
        :type n_shots: Optional[int], optional
        :param seed: Seed to set for simulations. None is to be used for quantum hardware or when a seed is not needed. Defaults to None
        :type seed: Optional[int], optional
        :param valid_check: Explicitly check that the circuit satisfies all of the required predicates before running. Defaults to True.
        :type valid_check: bool, optional
        :param remove_from_cache: Remove the circuit's results from the backend's cache. Defaults to True.
        :type remove_from_cache: bool, optional
        :param basis: Toggle between ILO (increasing lexicographic order of bit ids) and DLO (decreasing lexicographic order) for column ordering. Defaults to BasisOrder.ilo.
        :type basis: BasisOrder, optional
        :return: Dictionary mapping observed readouts to the number of times observed.
        :rtype: Dict[Tuple[int, ...],int]
        """
        raise NotImplementedError("Cannot get counts from this backend")

    @property
    def supports_state(self) -> bool :
        return self._supports_state

    def get_state(self, circuit:Circuit, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        """Calculate the statevector for a circuit. Statevectors :math:`[a_{00}, a_{01}, a_{10}, a_{11}]` are little-endian, so :math:`a_{01}` is the amplitude when qubit q[0] is in state :math:`\\left|1\\right>` and qubit q[1] is in state :math:`\\left|0\\right>`.
        If results for the circuit are already in the backend's cache from running process_circuits, those will be returned.

        :param circuit: The circuit to simulate.
        :type circuit: Circuit
        :param valid_check: Explicitly check that the circuit satisfies all of the required predicates before running. Defaults to True.
        :type valid_check: bool, optional
        :param remove_from_cache: Remove the circuit's results from the backend's cache. Defaults to True.
        :type remove_from_cache: bool, optional
        :param basis: Toggle between ILO-BE (increasing lexicographic order of bit ids, big-endian) and DLO-BE (decreasing lexicographic order, big-endian) for column ordering. Defaults to BasisOrder.ilo.
        :type basis: BasisOrder, optional
        :return: Full statevector in encoding given by `basis`.
        :rtype: np.ndarray
        """
        raise NotImplementedError("Cannot get statevector from this backend")

    @property
    def supports_unitary(self) -> bool :
        return self._supports_unitary

    def get_unitary(self, circuit:Circuit, valid_check:bool=True, remove_from_cache:bool=True, basis:BasisOrder=BasisOrder.ilo) -> np.ndarray :
        """Calculate the unitary matrix for a given circuit.
        If results for the circuit are already in the backend's cache from running process_circuits, those will be returned.

        :param circuit: The circuit to simulate.
        :type circuit: Circuit
        :param valid_check: Explicitly check that the circuit satisfies all of the required predicates before running. Defaults to True.
        :type valid_check: bool, optional
        :param remove_from_cache: Remove the circuit's results from the backend's cache. Defaults to True.
        :type remove_from_cache: bool, optional
        :param basis: Toggle between ILO-BE (increasing lexicographic order of bit ids, big-endian) and DLO-BE (decreasing lexicographic order, big-endian) for column ordering. Defaults to BasisOrder.ilo.
        :type basis: BasisOrder, optional
        :return: Unitary matrix with encoding given by `basis`.
        :rtype: np.ndarray
        """
        raise NotImplementedError("Cannot get unitary from this backend")

    @property
    def supports_expectation(self) -> bool :
        return self._supports_expectation
