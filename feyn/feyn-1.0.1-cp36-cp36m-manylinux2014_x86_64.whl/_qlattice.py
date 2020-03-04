import os
import typing

import requests

from feyn import Graph, QGraph


class Register:
    """
    Registers are the main interaction point with the QLattice, IO interfaces.
    Users connect registers with their data concepts, columns in their dataset or stores.
    """
    def __init__(self, celltype, label, location) -> None:
        """Construct a new 'Register' object.

        Arguments:
            celltype {str} -- Either "cont" or "cat" (continous or categorical).
            label {str} -- Name of the register, so that you can find it again later.
                           Usually the column name in your dataset, or the name of the concept this register represents.
            location {[type]} -- Location in the QLattice.
        """
        # TODO: Documentation. What is the type of 'location'?
        self.celltype = celltype
        self.label = label
        self.location = location

    def to_dict(self):
        return {
            'celltype': self.celltype,
            'label': self.label
        }


class QLattice:
    """
    The QLattice is a potentially very large lattice that links registers to
    each other through a set of interaction cells.

    QLattice incorporates all the knowledge learned about the probabilities of
    relations between registers and interaction cells.

    Through abzu algorithm we can extract QGraphs from the QLattice.
    """
    QLATTICE_BASE_URI = os.environ.get('QLATTICE_BASE_URI') or 'http://localhost:5000'

    def __init__(self, url=None, reset=False) -> None:
        """Construct a new 'QLattice' object.

        Keyword Arguments:
            url {str} -- URL of where your QLattice is running.
            reset {bool} -- Clears all learnings in the QLattice. Potentially very dangerous. Think twice before setting this to True! (default: {False})
        """
        if url is None:
            url = f"{self.QLATTICE_BASE_URI}/api/v1/qlattice"
        elif '/api/v1/qlattice' not in url:
            url = f"{url}/api/v1/qlattice"

        self.url = url

        self._load_qlattice(reset)

    def add_register(self, label: str, register_type: str = "cont") -> Register:
        """Add a new register to QLattice, if the register already exists returns same
        instance.

        Arguments:
            label {str} -- Name for register.
            register_type {str} -- Register type, either "cont" or "cat". (continous or categorical)

        Returns:
            Register -- The register instance.
        """

        req = requests.put("%s/register" % self.url, {
            'celltype': register_type,
            'label': label
        })
        req.raise_for_status()

        if req.status_code == 200:
            self._load_qlattice()

        reg = req.json()

        return Register(reg['celltype'], reg['label'], reg['location'])

    def get_qgraph(self, inputs: typing.List[Register], output: Register, steps: int = 3) -> QGraph:
        """Extract QGraph from inputs registers to output register.

        Arguments:
            inputs {typing.List[Register]} -- Input registers.
            output {Register} -- Output register.

        Returns:
            QGraph -- The QGraph instance from the inputs to the output.
        """
        req = requests.post("%s/simulation" % self.url, json={
            'inputs': [reg.to_dict() for reg in inputs],
            'output': output.to_dict(),
            'steps': steps
        })

        req.raise_for_status()

        graph = req.json()

        qgraph = QGraph(graph)

        return qgraph

    def update(self, graph: Graph) -> None:
        """ Update QLattice with learnings from a graph.

        Arguments:
            graph {Graph} -- Graph with learnings worth storing.
        """
        req = requests.post("%s/update" % self.url,
                            json=graph._to_dict()
                            )

        req.raise_for_status()

    def _load_qlattice(self, reset=False):
        req = requests.get("%s" % self.url, params={'reset': reset})
        req.raise_for_status()
        qlattice = req.json()

        self.width = qlattice['width']
        self.height = qlattice['height']

        self.registers = [Register(reg['celltype'], reg['label'], reg['location']) for reg in qlattice['registers']]

    def __repr__(self):
        return "<Abzu QLattice[%i,%i] '%s'>" % (self.width, self.height, self.url)
