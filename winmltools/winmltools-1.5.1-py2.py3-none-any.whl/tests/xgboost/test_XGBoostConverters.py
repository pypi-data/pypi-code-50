"""
Tests scilit-learn's tree-based methods' converters.
"""
import pickle
import onnx
import os
import unittest
from sklearn.datasets import load_iris
from xgboost import XGBRegressor, XGBClassifier
from winmltools.convert import convert_xgboost

from winmltools.convert.common.data_types import FloatTensorType
from .._utils import *

class TestXGBoostModels(unittest.TestCase):
    
    def test_xgb_regressor(self):
        iris = load_iris()
        X = iris.data[:, :2]
        y = iris.target

        xgb = XGBRegressor()
        xgb.fit(X, y)
        
        convert_and_validate_helper(xgb, 'XGBRegressor', self.assertEqual, input_types=[('input', FloatTensorType(shape=[1, 'None']))])
        
        
    def test_xgb_classifier(self):
        iris = load_iris()
        X = iris.data[:, :2]
        y = iris.target
        y[y == 2] = 0

        xgb = XGBClassifier()
        xgb.fit(X, y)
        
        convert_and_validate_helper(xgb, 'XGBClassifier', self.assertEqual, input_types=[('input', FloatTensorType(shape=[1, 'None']))])
 
    def test_xgb_classifier_multi(self):
        iris = load_iris()
        X = iris.data[:, :2]
        y = iris.target

        xgb = XGBClassifier()
        xgb.fit(X, y)
        
        convert_and_validate_helper(xgb, 'XGBClassifier-multi', self.assertEqual, input_types=[('input', FloatTensorType(shape=[1, 'None']))])


    def test_xgboost_unpickle_06(self):
        # Unpickle a model trained with an old version of xgboost.
        this = os.path.dirname(__file__)
        with open(os.path.join(this, "xgboost10day.pickle.dat"), "rb") as f:
            xgb = pickle.load(f)
        
        convert_and_validate_helper(xgb, 'XGBClassifier-multi', self.assertEqual, input_types=[('input', FloatTensorType([1, 10000]))])

if __name__ == '__main__':
    unittest.main()
                