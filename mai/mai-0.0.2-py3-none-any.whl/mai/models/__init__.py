'''
各种模型的实现

'''
from .resnet import resnet18
from .resnet import resnet34
from .resnet import resnet50
from .resnet import resnet101
from .resnet import resnet152
from .resnet import resnext50_32x4d
from .resnet import resnext101_32x8d
from .resnetxt_wsl import resnext101_32x8d_wsl
from .resnetxt_wsl import resnext101_32x16d_wsl
from .resnetxt_wsl import resnext101_32x32d_wsl
from .resnetxt_wsl import resnext101_32x48d_wsl
from .senet import se_resnet50
from .senet import se_resnet101
from .senet import se_resnet152
from .senet import se_resnext50_32x4d
from .senet import se_resnext101_32x4d
from .senet import senet154

from . import detection
from . import segmentation
from . import twin