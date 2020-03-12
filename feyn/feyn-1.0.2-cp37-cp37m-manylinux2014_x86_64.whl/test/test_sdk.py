import unittest
import pandas as pd
import numpy as np

from feyn import QLattice


class TestSDK(unittest.TestCase):

    def test_can_add_new_registers(self):
        lt = QLattice(reset=True)

        lt.add_register("Age", "cont")
        lt.add_register("Smoker", "cat")

        self.assertEqual(len(lt.registers), 2)

    def test_location_is_assigned_to_registers_automatically(self):
        lt = QLattice(reset=True)

        r1 = lt.add_register("Age", "cont")
        r2 = lt.add_register("Smoker", "cat")

        self.assertNotEqual(r1.location, r2.location)

    def test_register_is_reused(self):
        lt = QLattice(reset=True)

        lt.add_register("Age", "cont")
        lt.add_register("Smoker", "cat")

        self.assertEqual(len(lt.registers), 2)

        lt.add_register("Smoker", "cat")

        self.assertEqual(len(lt.registers), 2)

    def test_qlattice_extracts_qgraphs(self):
        lt = QLattice(reset=True)

        r1 = lt.add_register("Age", "cont")
        r2 = lt.add_register("Smoker", "cat")
        r3 = lt.add_register("insurable", "cat")

        qgraph = lt.get_qgraph([r1, r2], r3)

        qgraph._extract_graphs()

        self.assertGreater(len(qgraph.graphs), 0)

    def test_qgraph_tune(self):
        lt = QLattice(reset=True)

        r1 = lt.add_register("Age", "cont")
        r2 = lt.add_register("Smoker", "cont")
        r3 = lt.add_register("insurable", "cont")

        qgraph = lt.get_qgraph([r1, r2], r3)

        data = pd.DataFrame(np.array([
                [10, 16, 30, 60],
                [0, 1, 0, 1],
                [1, 1, 1, 0]
            ]).T,
            columns=["Age", "Smoker", "insurable"]).astype({
                "Age": "float32",
                "Smoker": "float32",
                "insurable": "float32"
            })

        X = data[["Age", "Smoker"]]
        Y = data["insurable"]

        qgraph.tune(X, Y)

    def test_can_fetch_graphs_after_updates(self):
        lt = QLattice(reset=True)

        r1 = lt.add_register("Age", "cont")
        r2 = lt.add_register("Smoker", "cat")
        r3 = lt.add_register("insurable", "cat")

        qgraph = lt.get_qgraph([r1, r2], r3)
        lt.update(qgraph.graphs[0])

        qgraph = lt.get_qgraph([r1, r2], r3)

        self.assertGreater(len(qgraph.graphs), 0)
