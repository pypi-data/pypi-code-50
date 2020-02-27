import unittest

import pytest

from kisters.water.time_series.tso import TSOStore


@pytest.mark.skip("Waiting for new TSO test system")
class Test(unittest.TestCase):
    start = "2019-01-01T00:00Z"
    end = "2019-01-27T00:00Z"
    ts_id = "0635fa9d-0806-4ccf-b2f9-78c61597b813"
    ts_path = "RethelStation/testPrst"
    ts_name = "testPrst"
    ts_filter = "RethelStation/*"

    @classmethod
    def setUpClass(cls):
        base_url = "http://tso-test.kisters.de/KiWebPortal/rest/"
        cls.tso = TSOStore(base_url=base_url, user="PythonTest@kisters.de", password="Python3!")

    def test_01_get_by_path(self):
        self.assertEqual(self.tso.get_by_path(self.ts_path).id, self.ts_id)

    def test_02_get_by_id(self):
        self.assertEqual(self.tso.get_by_id(self.ts_id).path, self.ts_path)

    def test_03_get_by_filter(self):
        self.assertGreater(len(list(self.tso.get_by_filter(self.ts_filter))), 2)

    def test_04_ts_attributes(self):
        ts = self.tso.get_by_id(self.ts_id)
        meta = ts.to_dict()
        self.assertIsNotNone(meta)
        self.assertIn("id", meta)
        self.assertIn("name", meta)
        self.assertIn("tsPath", meta)
        self.assertIn("locationId", meta)

    def test_05_read_data_frame(self):
        self.assertEqual(
            self.tso.get_by_id(self.ts_id).read_data_frame(start=self.start, end=self.end).shape[0], 624
        )


if __name__ == "__main__":
    unittest.main()
