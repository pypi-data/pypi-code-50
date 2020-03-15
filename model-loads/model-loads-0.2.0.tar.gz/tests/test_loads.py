import unittest

from examples.models.tar.mobilenet_v2 import MobileNetV2
from model_loads.loads import load_models

model = MobileNetV2()
model_path = "../examples/models/tar/checkpoint.pth.tar"


class MyTest(unittest.TestCase):
    def test_load_models(self, model_path, model):
        load_models(model_path, model)
        assert type(model) == "<class 'torchvision.models.mobilenet.MobileNetV2'>"
