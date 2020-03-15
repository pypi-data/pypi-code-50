import model_loads as lo
import torchvision.models as models

model = models.MobileNetV2()
model_path = "../examples/models/pth/mobilenet_v2-b0353104.pth"
lo.load_models(model_path, model, use_gpu=True)
print(model)
print(type(model))

from models.tar.mobilenet_v2 import MobileNetV2

model = MobileNetV2()
model_path = "models/tar/checkpoint.pth.tar"
# load_multi_gpu_models2_single_gpu(model_path, model)
lo.load_models(model_path, model)
print(model)

import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""

model = models.MobileNetV2()
model_path = "models/pth/mobilenet_v2-b0353104.pth"
lo.load_models(model_path, model, use_gpu=True)
print(model)
print(type(model))