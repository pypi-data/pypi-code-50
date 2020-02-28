import unittest
import keras
import onnx
import os

from .._utils import *
from winmltools.config import cfg
models_dir = os.path.dirname(os.path.abspath(__file__)) + '/../models'

class TestKeras(unittest.TestCase):
    def test_LSTM(self):
        model = keras.models.load_model(os.path.join(models_dir, 'keras', 'LSTM.keras'))
        convert_and_validate_helper(model, 'keras-lstm', self.assertEqual, disable_assert=True)

    def test_Conv2D(self):
        model = keras.models.load_model(os.path.join(models_dir, 'keras', 'Conv2D.keras'))
        convert_and_validate_helper(model, 'keras-conv2d', self.assertEqual, disable_assert=True)

    def test_tanh(self):
        model = keras.models.load_model(os.path.join(models_dir, 'keras', 'tanh.keras'))
        convert_and_validate_helper(model, 'keras-tanh', self.assertEqual, disable_assert=True)
