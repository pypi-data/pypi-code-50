import tempfile
import unittest
import os

from r3d3.db_logging import R3D3Logger


class TestDBLogging(unittest.TestCase):
    def test_logging(self):
        db_path = tempfile.mkstemp()[1]
        print(db_path)
        logger = R3D3Logger(db_path, 1, 1)

        logger.info("Hello")
        logger.error("Some error")
        logger.debug("Some debug")
        logger.warning("Some warning")

        df = logger.get_full_log()

        print(df)

        assert len(df) == 4

        os.remove(db_path)
