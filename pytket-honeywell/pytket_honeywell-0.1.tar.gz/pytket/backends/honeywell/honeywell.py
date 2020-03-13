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

import json
import sys
from collections import Counter
from functools import reduce
from http import HTTPStatus
from typing import Dict, Iterable, List, Optional, Tuple, Union

import numpy as np
import requests
from pytket.backends import Backend
from pytket.circuit import BasisOrder, Circuit, OpType
from pytket.honeywell.honeywell_convert import (honeywell_pass,
                                                translate_honeywell)
from pytket.passes import BasePass, SequencePass, SynthesiseIBM
from pytket.predicates import (DefaultRegisterPredicate, GateSetPredicate,
                               MaxNQubitsPredicate,
                               NoClassicalControlPredicate,
                               NoFastFeedforwardPredicate, Predicate)

from .api_wrappers import retrieve_job, status

HONEYWELL_URL_PREFIX = "https://qapi.honeywell.com/v1/"

HONEYWELL_DEVICE_QC = "HQS-LT-1.0"
HONEYWELL_DEVICE_APIVAL = "HQS-LT-1.0-APIVAL"

# Hard-coded for now as there is no API to retrieve these.
# All devices are fully connected.
device_info = {
    HONEYWELL_DEVICE_QC: {"max_n_qubits": 4},
    HONEYWELL_DEVICE_APIVAL: {"max_n_qubits": 10},
}

def _shottable_from_str(strlist: Iterable):
    return np.array([[int(i) for i in val[::-1]] for val in strlist])

#TODO spell identifiers correctly
class JobHandle:
    """Object to store multidimensional identifiers for a circuit sent to a backend for execution
    Initialisation arguments must be hashable.
    """
    def __init__(self, *args):
        self.identifiers = tuple(args)
    def __hash__(self):
        return hash(self.identifiers)
    def __eq__(self, other):
        return hash(self.identifiers) == hash(self.identifiers)
    def __repr__(self):
        return repr(self.identifiers)

class HoneywellBackend(Backend):
    """
    Interface to a HONEYWELL device or simulator.
    """

    def __init__(
        self,
        api_key: str,
        device_name: Optional[str] = HONEYWELL_DEVICE_APIVAL,
        label: Optional[str] = "job",
    ):
        """
        Construct a new Honeywell backend.

        :param      api_key: HONEYWELL API key
        :type       api_key: string
        :param      device_name:  device name (suffix of URL, e.g. "HQS-LT-1.0")
        :type       device_name:  string
        :param      label:        label to apply to submitted jobs
        :type       label:        string
        """
        super().__init__(shots=True, counts=True)
        self._device_name = device_name
        self._label = label
        self._cache = {}
        self._header = {"x-api-key": api_key}
        self._max_n_qubits = (
            device_info[device_name]["max_n_qubits"]
            if device_name in device_info
            else None
        )

    @property
    def required_predicates(self) -> List[Predicate]:
        preds = [
            # DefaultRegisterPredicate(),
            # NoClassicalControlPredicate(),
            # NoFastFeedforwardPredicate(),
            GateSetPredicate(
                {OpType.Rz, OpType.PhasedX, OpType.ZZMax, OpType.Reset, OpType.Measure, OpType.Barrier}
            ),
        ]
        if self._max_n_qubits is not None:
            preds.append(MaxNQubitsPredicate(self._max_n_qubits))
        return preds

    @property
    def default_compilation_pass(self) -> BasePass:
        return SequencePass([SynthesiseIBM(), honeywell_pass])

    def process_circuits(
        self,
        circuits: Iterable[Circuit],
        n_shots: Optional[int] = None,
        seed: Optional[int] = None,
        valid_check: bool = True,
    ):
        if valid_check:
            for c in circuits:
                if not self.valid_circuit(c):
                    raise ValueError(
                        "Circuits do not satisfy all required predicates for this backend"
                    )
        jobids = []
        for c in circuits:
            honeywell_circ = translate_honeywell(c)
            try:
                 # send job request
                body = {
                    'machine': self._device_name,
                    'name': self._label,
                    'language': 'OPENQASM 2.0',
                    'program': honeywell_circ,
                    'priority': 'normal',
                    'count': n_shots,
                    'options': None
                }
                res = requests.post(
                    HONEYWELL_URL_PREFIX + 'job',
                    json.dumps(body),
                    headers=self._header
                )
                if res.status_code != HTTPStatus.OK:
                    jr = res.json()
                    print(jr)
                    raise RuntimeError(f'HTTP error while submitting job, {jr["error"]["text"]}')

                # extract job ID from response
                jr = res.json()
                job_id = jr['job']

            except ConnectionError:
                raise ConnectionError('{} Connection Error: Error during submit...'.format(self._label))


            self._cache[c] = job_id
            jobids.append(JobHandle(job_id))
        
        return jobids

    def empty_cache(self):
        self._cache = {}

    def job_status(self, handle: JobHandle) -> str:
        res = requests.get(
            HONEYWELL_URL_PREFIX + 'job/' + handle.identifiers[0] + '?websocket=true',
            headers=self._header
        )
        jr = res.json()
        return jr['status']

    def _get_samples(self, job: JobHandle) -> Tuple[int, List[int]]:
        jr = retrieve_job(self._header["x-api-key"], job.identifiers[0], HONEYWELL_URL_PREFIX)
        if "error" in jr:
            raise RuntimeError(jr["error"]["text"])
        if jr["status"] == "canceled":
            raise RuntimeWarning("Job has been cancelled, attempting to retrieve partial results.")
        if jr["status"] != "completed":
            raise RuntimeError(f"Cannot retrieve results, job status is {jr['status']}")
        try:
            res = jr["results"]
        except KeyError:
            raise RuntimeError("Results missing.")


        return reduce(np.char.add, (res[c] for c in sorted(res)))


    def _process_one_circuit(
        self,
        circuit: Circuit,
        n_shots: Optional[int] = None,
        seed: Optional[int] = None,
        valid_check: bool = True,
        remove_from_cache: bool = True,
        basis: BasisOrder = BasisOrder.ilo,
    ) -> Tuple[int, List[int]]:
        if circuit not in self._cache:
            if not n_shots:
                raise ValueError(
                    "Circuit has not been processed; please specify a number of shots"
                )
            jids = self.process_circuits([circuit], n_shots, seed, valid_check)
        job = self._cache[circuit]
        if remove_from_cache:
            del self._cache[circuit]
        return self._get_samples(jids[0])

    def _get_or_process(
        self,
        *args, **kwargs) -> Iterable[str]:
        if isinstance(args[0], Circuit):
            return self._process_one_circuit(args, kwargs)
        elif isinstance(args[0], JobHandle):
            return self._get_samples(args[0])
        else:
            raise RuntimeError("Provide either a circuit run or a handle to a previously submitted circuit.")
        
    def get_shots(
        self,
        circuit: Union[Circuit, JobHandle],
        n_shots: Optional[int] = None,
        seed: Optional[int] = None,
        valid_check: bool = True,
        remove_from_cache: bool = True,
        basis: BasisOrder = BasisOrder.ilo,
    ) -> np.ndarray:
        return _shottable_from_str(self._get_or_process(circuit, n_shots, seed, valid_check, remove_from_cache, basis))

    def get_counts(
        self,
        circuit: Union[Circuit, JobHandle],
        n_shots: Optional[int] = None,
        seed: Optional[int] = None,
        valid_check: bool = True,
        remove_from_cache: bool = True,
        basis: BasisOrder = BasisOrder.ilo,
    ) -> Dict[Tuple[int, ...], int]:

        ctr = Counter(self._get_or_process(circuit, n_shots, seed, valid_check, remove_from_cache, basis))

        return {tuple(int(i) for i in reversed(string)): count for string, count in ctr.items()}
