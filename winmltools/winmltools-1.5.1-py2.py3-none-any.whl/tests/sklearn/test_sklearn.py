import unittest
from sklearn import linear_model
import winmltools
from winmltools.config import cfg
from .._utils import run_model, temp_model_path
import numpy as np
import onnx

from onnxconverter_common.data_types import FloatTensorType, Int64TensorType

import os

class TestSklearn(unittest.TestCase):
    def test_linear_regression(self):
        regr = linear_model.LinearRegression()
        X = np.asarray([1,2,3,4,5])
        Y = np.asarray([10, 21, 29, 42, 53])
        X = X.reshape(-1, 1)

        regr.fit(X, Y)
        initial_type = [('float_input', FloatTensorType([1, 5]))]
        for op_set in cfg.TO_TEST_OPSETS:
            model = winmltools.convert.convert_sklearn(regr, op_set, initial_types=initial_type)
            model_path = os.path.join(temp_model_path, 'sklearn-linreg_' + str(op_set) + '.onnx')
            if not os.path.isdir(temp_model_path):
                os.makedirs(temp_model_path)
            onnx.save_model(model, model_path)
            self.assertEqual(run_model(model_path), 0)