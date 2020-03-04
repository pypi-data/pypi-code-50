import json
import typing

import numpy as np

import _feyn
from feyn import DotRenderer

# Update this number whenever there are breaking changes to save/load
# (or to_dict/from_dict). Then use it intelligently in Graph.load.
SCHEMA_VERSION = "2020-02-07"


def _lattice_loc_hash(location):
    return location[0] + location[1]*1000 + location[2]*100000


class Graph(_feyn.Graph):
    """
    Graph represents a problem that can be to tuned and used for predicting.
    """
    def __init__(self, size):
        """Construct a new 'Graph' object.

        Arguments:
            size {[int]} -- The number of nodes this graph contains.
        """
        # TODO: Documentation: Explain size better (formerly named length)
        super().__init__(size)

        self.samples = 0
        self.loss_ema = None
        self.accuracy_ema = None

    def predict(self, X) -> np.ndarray:
        """
        Calculate predictions based on input values.

        >>> graph.predict({ "age": [34, 78], "sex": ["male", "female"] })
        [True, False]

        Arguments:
            X {dict or pandas.DataFrame} -- The input values.

        Returns:
            np.ndarray -- The calculated predictions.
        """
        # Magic support for pandas DataFrame
        if type(X).__name__ == "DataFrame":
            X = {col: X[col].values for col in X.columns}

        return super().query(X, None)

    def save(self, file: typing.TextIO):
        """Save the 'Graph' to a file-like object.

        It can later be used to recreate the 'Graph' with 'Graph.load'.


        Arguments:
            file {typing.TextIO} -- A file-like object to save the graph to.
        """
        as_dict = self._to_dict()
        as_dict["version"] = SCHEMA_VERSION
        json.dump(as_dict, file)

    @staticmethod
    def load(file: typing.TextIO):
        """Load a 'Graph' from a file-like object.

        Usually used together with 'Graph.save'.

        Arguments:
            file {typing.TextIO} -- A file-like object to load the 'Graph' from.

        Returns:
            Graph -- The loaded 'Graph'-object
        """
        as_dict = json.load(file)
        return Graph._from_dict(as_dict)

    def __hash__(self):
        checksum = 0
        for ix in range(self.size):
            interaction = self.get_interaction(ix)
            for _, src in enumerate(interaction.sources):
                if src != -1:
                    srcinteraction = self.get_interaction(src)
                    checksum += _lattice_loc_hash(interaction.latticeloc) + _lattice_loc_hash(srcinteraction.latticeloc)

        return checksum

    def __eq__(self, other):
        return other.__hash__() == self.__hash__()

    def _tune(self, X, Y, epochs=1, verbose=False):
        for epoch in range(epochs):
            predictions = super().query(X, Y)
            loss = np.mean(np.square(Y.astype(float)-predictions))
            acc = np.mean(Y.astype(int) == np.round(predictions).astype(int))

            if self.loss_ema is None:
                self.loss_ema = loss
                self.accuracy_ema = acc
            else:
                self.loss_ema = .8*self.loss_ema + .2*loss
                self.accuracy_ema = .8*self.accuracy_ema + .2*acc

            if verbose:
                print("Epoch %i: loss %.4f (%.4f). Acc %.4f%%" %(epoch, self.loss_ema, loss, acc))

        self.samples += epochs * Y.shape[0]

        return self.loss_ema

    def _to_dict(self):
        nodes = []
        links = []
        for ix in range(self.size):
            interaction = self.get_interaction(ix)
            nodes.append({
                "id": interaction.location,
                "celltype": interaction.type,
                "location": interaction.latticeloc,
                "legs": len(interaction.sources),
                "gluamine": interaction.gluamine,
                "label": interaction.label,
                "state": interaction.state
            })
            for ordinal, src in enumerate(interaction.sources):
                if src != -1:
                    links.append({
                        'source': src,
                        'target': interaction.location,
                        **interaction.linkdata[ordinal]
                    })

        return {
            'directed': True,
            'multigraph': True,
            'nodes': nodes,
            'links': links
        }

    def _repr_svg_(self):
        g = DotRenderer.rendergraph(self)
        
        if isinstance(g, str):
            return g

        return g._repr_svg_()

    @staticmethod
    def _get_interaction(data: dict) -> _feyn.Interaction:
        interaction = _feyn.Interaction(data["celltype"], data["gluamine"], data["label"])
        interaction.latticeloc = data["location"]
        interaction.state = data["state"]
        interaction.set_source(0, -1)
        interaction.linkdata = [{}, {}]

        return interaction

    @staticmethod
    def _from_dict(gdict):
        sz = len(gdict["nodes"])
        graph = Graph(sz)
        for ix, node in enumerate(gdict["nodes"]):
            interaction = Graph._get_interaction(node)
            graph.set_interaction(ix, interaction)

        for edge in gdict["links"]:
            interaction = graph.get_interaction(edge["target"])
            ord = edge["ord"]
            interaction.set_source(ord, edge["source"])
            interaction.linkdata[ord] = edge
        return graph
