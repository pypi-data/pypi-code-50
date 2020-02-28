import unittest
import coremltools
import onnx
import os
from winmltools.config import cfg

from .._utils import *

models_dir = os.path.dirname(os.path.abspath(__file__)) + '/../models'
      
class TestCoreml(unittest.TestCase):
    def test_LSTM(self):
        model = coremltools.models.MLModel(os.path.join(models_dir, 'coreml', 'LSTM.mlmodel'))
        convert_and_validate_helper(model, 'coreml-lstm', self.assertEqual, disable_assert=True)

    def test_mnist(self):
        model = coremltools.models.MLModel(os.path.join(models_dir, 'coreml', 'mnist.mlmodel'))
        convert_and_validate_helper(model, 'coreml-mnist', self.assertEqual, disable_assert=True)

    def test_simple_RNN(self):
        model = coremltools.models.MLModel(os.path.join(models_dir, 'coreml', 'SimpleRNN.mlmodel'))
        convert_and_validate_helper(model, 'coreml-rnn', self.assertEqual, disable_assert=True)
        