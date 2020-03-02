"""High level functions for analyses"""

import numpy as np
import cv2

from typing import List, Dict

from histographer.analysis.image.color import rgb2hed, normalize_channels, channel_metrics
from histographer.analysis.image.segment import segment_sample


def coloring_stats(rgb_images: List[np.ndarray]) -> List[Dict]:
    """Perform image segmentation and get coloring information for segmented areas.
    :param rgb_images: List of numpy arrays containing RGB images
    :return: List of dictionaries with results
    """
    results = []
    for image in rgb_images:
        image_results = {}

        # Convert RGB image to HED and normalize channels
        hed = rgb2hed(image)
        hed_n = normalize_channels(image)

        # Segment image into (nuclei, tissue, no_class)
        segments = segment_sample(hed_n)

        for name, seg in zip(('Nuclei H', 'Tissue E'), segments):
            metrics = channel_metrics(hed[seg])
            image_results[name] = metrics

        results.append(image_results)

    return results


if __name__ == '__main__':
    image = cv2.imread('../data/muscular_tissue.png')
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(coloring_stats([rgb_image]))
