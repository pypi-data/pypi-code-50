import unittest
from unittest.mock import patch
from livesplit_id_normalizer import cli


class TestCLI(unittest.TestCase):
    @patch("livesplit_id_normalizer.cli.normalize")
    @patch("livesplit_id_normalizer.cli.argparse")
    def test_start(self, argparse, normalize_mock):
        cli.start()
