import unittest
import gammalearn.utils as utils
import numpy as np


class MockDataset(object):

    def __init__(self):

        self.images = np.array([np.full(1855, 0.001),
                                np.full(1855, 1),
                                np.full(1855, 0.0001),
                                np.full(1855, 0.1)])
        self.images[3, 903:910] = 30
        # self.images[2, 903:910] = 10
        self.images[2, 1799:1806] = 10  # for cleaning and leakage
        self.energies = np.array([0.010, 2.5, 0.12, 0.8])
        self.group_by = 'image'
        self.camera_type = 'LST_LSTCam'
        self.particle_types = np.array([1, 1, 1, 1])
        self.telescope_ids = np.array([1, 1, 2, 1])

    def __len__(self):
        return len(self.images)


class TestUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.dataset = MockDataset()

        self.amplitude_filter_parameters = [300, np.inf]
        self.amplitude_true_ids = [1, 3]

        self.cleaning_filter_parameters = {'apply_cleaning': False, 'picture_thresh': 6, 'boundary_thresh': 3,
                                           'keep_isolated_pixels': False, 'min_number_picture_neighbors': 2}
        self.cleaning_true_ids = [2, 3]

        self.leakage_parameters = {'leakage2_cut': 0.2, 'picture_thresh': 6, 'boundary_thresh': 3,
                                   'keep_isolated_pixels': False, 'min_number_picture_neighbors': 2}
        self.leakage_true_ids = [3]

        self.energy_parameters = {'energy': [0.02, 2], 'filter_only_gammas': True}
        self.energy_true_ids = [2, 3]

        self.telescope_id_parameters = {'tel_id': 1}
        self.tel_true_ids = [0, 1, 3]

    def test_amplitude(self):
        assert np.all(utils.amplitude_filter(self.dataset, self.amplitude_filter_parameters) == self.amplitude_true_ids)

    def test_cleaning(self):
        assert np.all(utils.cleaning_filter(self.dataset, **self.cleaning_filter_parameters) == self.cleaning_true_ids)

    def test_leakage(self):
        assert np.all(utils.leakage_filter(self.dataset, **self.leakage_parameters) == self.leakage_true_ids)

    def test_energy(self):
        assert np.all(utils.energyband_filter(self.dataset, **self.energy_parameters) == self.energy_true_ids)

    def test_telescope_id(self):
        assert np.all(utils.telescope_id_filter(self.dataset, **self.telescope_id_parameters) == self.tel_true_ids)


if __name__ == '__main__':
    unittest.main()
