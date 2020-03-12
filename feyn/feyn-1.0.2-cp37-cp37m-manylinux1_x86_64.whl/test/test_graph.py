import unittest
import feyn
import _feyn

import numpy as np
import io

# NOTE: Label vs latticeloc for registers.. Seems like two ways of expressing the same thing.
#       Would it make sense, to let the lattice deal with label-to-loc mapping,
#       so a client cannot screw this up?


class TestGraph(unittest.TestCase):
    def _create_graph(self):
        # It was not easy to figure out how to create this programatically.
        # So I have just grabbed an example from a notebook.
        # TODO: Create this programatically, so the test does not break on
        # changes in _from_dict.
        return feyn.Graph._from_dict({
            'directed': True,
            'multigraph': True,
            'nodes': [{
                'id': 0,
                'celltype': 'cont',
                'location': (0, -1, -1),
                'legs': 1,
                'gluamine': 0,
                'label': 'in',
                'state': {
                    'variance': 13206.6435546875,
                    'absmax': 192.6171875,
                    'iabsmax': 1.0
                }
            }, {
                'id': 1,
                'celltype': 'lr',
                'location': (3, 13, 5),
                'legs': 1,
                'gluamine': 0,
                'label': 'lr',
                'state': {
                    'w0': -14.002081871032715,
                    'w1': 0.6808160543441772,
                    'bias': 4.349215984344482
                }
            }, {
                'id': 2,
                'celltype': 'gaussian',
                'location': (2, 13, 6),
                'legs': 1,
                'gluamine': 0,
                'label': 'gaussian',
                'state': {
                    'center0': 0.9357265830039978,
                    'center1': 0.9535694718360901,
                    'w0': 0.1639804095029831,
                    'w1': 0.10000000149011612
                }
            }, {
                'id': 3,
                'celltype': 'cont',
                'location': (2, -1, -1),
                'legs': 1,
                'gluamine': 0,
                'label': 'out',
                'state': {
                    'variance': 0.06923199445009232,
                    'absmax': 1.0,
                    'iabsmax': 0.9991648197174072
                }
            }],
            'links': [
                {'source': 0, 'target': 1, 'ord': 0, 'direction': 5},
                {'source': 1, 'target': 2, 'ord': 0, 'direction': 6},
                {'source': 2, 'target': 3, 'ord': 0}
            ]
        })

    def test_persist_and_rehydrate(self):
        # Arrange
        graph = self._create_graph()

        # Sanity check. Can I predict with this graph?
        predictions = graph.predict({"in": np.array([1, 2])})
        self.assertEqual(len(predictions), 2)

        # Persist it
        file = io.StringIO()
        graph.save(file)

        with self.subTest("Should be loadable"):
            file.seek(0)
            rehydrated_graph = feyn.Graph.load(file)

        with self.subTest("Should be executable"):
            predictions = rehydrated_graph.predict({"in": np.array([1, 2])})
            self.assertEqual(len(predictions), 2)

        with self.subTest("Should include a version number"):
            file.seek(0)
            file_contents = file.read()
            self.assertRegex(file_contents, "version")

    def test_persist_accepts_file_and_string(self):
        graph = self._create_graph()

        with self.subTest("Can save and load with file-like objects"):
            file = io.StringIO()
            graph.save(file)

            file.seek(0)
            rehydrated_graph = feyn.Graph.load(file)
            self.assertEqual(graph, rehydrated_graph)

        with self.subTest("Can save and load with a string path"):
            import tempfile

            with tempfile.NamedTemporaryFile() as file:
                path = file.name
                graph.save(path)

                rehydrated_graph = feyn.Graph.load(path)
                self.assertEqual(graph, rehydrated_graph)


    def test_query_accepts_np(self):
        input = _feyn.Interaction("cont", label="input")
        input.set_source(0, -1)

        out = _feyn.Interaction("cont", label="out")
        out.set_source(0, 0)

        g = feyn.Graph(2)
        g.set_interaction(0, input)
        g.set_interaction(1, out)

        o = g.query(
            {"input": np.array([42.0, 24, 100, 50])},
            np.array([0.1, 0.3, 0.01, 0.8])
        )

        self.assertEqual(len(o), 4)

    def test_predict_accepts_dicts_with_lists(self):
        # Arrange
        g = self._create_graph()

        o = g.predict(
            {"in": [42.0, 24, 100, 50]}
        )

        self.assertEqual(len(o), 4)
        self.assertFalse(np.isnan(o).any(), "There should be no nans")

    @unittest.skip("c powers not strong enough to find a smart solution, yet!")
    def test_segfault(self):
        """
        The offending statement is: if (interaction->sources[0]!=-1) continue;
        around line 166 in query in pygraph.c.

        sources is un-initialized or something, and im not sure where to init it!
        """
        graph = feyn.Graph(1)
        graph.predict({"in": np.array([1, 2])})
