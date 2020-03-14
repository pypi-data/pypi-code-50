import unittest
import shutil
from pathlib import Path
import logging
from yalow import Yalow


class YalowTest(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).parent.parent
        self.log_dir = Path(__file__).parent.parent/'log'
        self.yalow = Yalow(root_path=self.project_root, project_name='yalowtest')

    def tearDown(self):
        self.yalow.handler.close()
        self.yalow.logger.removeHandler(self.yalow.handler)
        del self.yalow
        shutil.rmtree(self.log_dir)

    def test_yalow_logger(self):
        self.assertIsInstance(self.yalow.logger, logging.Logger)

    def test_yalow_log_filepath(self):
        self.assertIsInstance(self.yalow.log_filepath, Path)

    def test_yalow_handler(self):
        self.assertIsInstance(self.yalow.handler, logging.FileHandler)

    def test_yalow_formatter(self):
        self.assertIsInstance(self.yalow.formatter, logging.Formatter)
