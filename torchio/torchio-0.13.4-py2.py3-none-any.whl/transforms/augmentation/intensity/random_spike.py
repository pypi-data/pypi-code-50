import warnings
from typing import Tuple, Optional, Union
import torch
import numpy as np
import SimpleITK as sitk
from ....utils import is_image_dict
from ....torchio import INTENSITY, DATA, AFFINE
from .. import RandomTransform


class RandomSpike(RandomTransform):
    def __init__(
            self,
            num_spikes_range: Union[int, Tuple[int, int]] = 1,
            intensity_range: Union[float, Tuple[float, float]] = (0.1, 1),
            proportion_to_augment: float = 1,
            seed: Optional[int] = None,
            verbose: bool = False,
            ):
        super().__init__(seed=seed, verbose=verbose)
        self.proportion_to_augment = self.parse_probability(
            proportion_to_augment,
            'proportion_to_augment',
        )
        self.intensity_range = self.parse_range(
            intensity_range, 'intensity_range')
        if isinstance(num_spikes_range, int):
            self.num_spikes_range = num_spikes_range, num_spikes_range
        else:
            self.num_spikes_range = num_spikes_range

    def apply_transform(self, sample: dict) -> dict:
        for image_name, image_dict in sample.items():
            if not is_image_dict(image_dict):
                continue
            if image_dict['type'] != INTENSITY:
                continue
            params = self.get_params(
                self.num_spikes_range,
                self.intensity_range,
                self.proportion_to_augment,
            )
            num_spikes_param, intensity_param, do_it = params
            sample[image_name]['random_spike_intensity'] = intensity_param
            sample[image_name]['random_spike_num_spikes'] = num_spikes_param
            sample[image_name]['random_spike_do'] = do_it
            if not do_it:
                return sample
            if (image_dict[DATA][0] < -0.1).any():
                # I use -0.1 instead of 0 because Python was warning me when
                # a value in a voxel was -7.191084e-35
                # There must be a better way of solving this
                message = (
                    f'Image "{image_name}" from "{image_dict["stem"]}"'
                    ' has negative values.'
                    ' Results can be unexpected because the transformed sample'
                    ' is computed as the absolute values'
                    ' of an inverse Fourier transform'
                )
                warnings.warn(message)
            image = self.nib_to_sitk(
                image_dict[DATA][0],
                image_dict[AFFINE],
            )
            image_dict[DATA] = self.add_artifact(
                image,
                num_spikes_param,
                intensity_param,
            )
            # Add channels dimension
            image_dict[DATA] = image_dict[DATA][np.newaxis, ...]
            image_dict[DATA] = torch.from_numpy(image_dict[DATA])
        return sample

    @staticmethod
    def get_params(
            num_spikes_range: Tuple[int, int],
            intensity_range: Tuple[float, float],
            probability: float,
            ) -> Tuple:
        ns_min, ns_max = num_spikes_range
        num_spikes_param = torch.randint(ns_min, ns_max + 1, (1,)).item()
        i_min, i_max = intensity_range
        intensity_param = torch.rand(1).item() * (i_max - i_min) + i_min
        do_it = torch.rand(1) < probability
        return num_spikes_param, intensity_param, do_it

    def add_artifact(
            self,
            image: sitk.Image,
            num_spikes: int,
            factor: float,
            ):
        array = sitk.GetArrayViewFromImage(image).transpose()
        spectrum = self.fourier_transform(array).ravel()
        for _ in range(num_spikes):
            index = torch.randint(0, len(spectrum), (1,))
            spectrum[index] = spectrum.max() * factor
        spectrum = spectrum.reshape(array.shape)
        result = self.inv_fourier_transform(spectrum)
        return result.astype(np.float32)
