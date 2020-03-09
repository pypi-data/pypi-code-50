from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import six
import os
import random
import re
import numpy as np
import math
from skimage import exposure
from skimage import morphology
from skimage import color
from skimage import  transform,exposure
from skimage.filters import *
from scipy import misc,ndimage
from ..backend.common import *
from itertools import repeat

__all__ = ['']


_session=get_session()
_backend=_session.backend
_image_backend=_session.image_backend

if _image_backend=='opencv':
    from ..backend.opencv_backend import *
else:
    from ..backend.pillow_backend import *

from ..backend.load_backend import get_backend

if get_backend()=='pytorch':
    from ..backend.pytorch_backend import to_numpy,to_tensor
elif get_backend()=='tensorflow':
    from ..backend.tensorflow_backend import  to_numpy,to_tensor
elif get_backend()=='cntk':
    from ..backend.cntk_backend import  to_numpy,to_tensor

__all__ = ['mask2trimap']

def mask2trimap(kernal_range=(7,15)):
    def img_op(mask: np.ndarray):
        trimap=mask.copy().astype(np.float32)
        trimap[trimap>0]=255.0
        k_size = random.choice(range(*kernal_range))
        trimap[np.where((ndimage.grey_dilation(mask[:,:],size=(k_size,k_size)) - ndimage.grey_erosion(mask[:,:],size=(k_size,k_size)))!=0)] = 128
        return trimap
    return img_op