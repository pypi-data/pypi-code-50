import os
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET

from livesplit_id_normalizer import normalizer

TESTS_PATH = os.path.dirname(os.path.realpath(__file__))
FIXTURES_PATH = os.path.join(TESTS_PATH, "fixtures")
RUN1_PATH = os.path.join(FIXTURES_PATH, "run1.xml")


class TestLivesplitIdNormalizer(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.root = ET.parse(RUN1_PATH).getroot()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_find_initial_run(self):
        self.assertEqual(3, normalizer.find_initial_run(self.root))

    def test_normalize(self):
        output_path = os.path.join(self.temp_dir, "tmp.xml")
        normalizer.normalize(RUN1_PATH, output_path=output_path)
        root = ET.parse(output_path).getroot()
        self.assertEqual(1, normalizer.find_initial_run(root))
