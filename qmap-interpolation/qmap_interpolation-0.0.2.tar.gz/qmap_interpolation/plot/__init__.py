try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError(f'Matplotlib is required for the visualization package. Please, install '
                      f'the latest version (official site: matplotlib.org).')

import numpy as np

from ..image import Image


def plot_image(img: Image):
    plt.imshow(np.ma.masked_where(img.detector_geometry.mask, img.raw_image))
    raise NotImplementedError
