import unittest
import collections
import numpy as np
import gammalearn.datasets as dsets


class TestDL1DHDataset(unittest.TestCase):

    def setUp(self) -> None:
        self.data_file = '../../share/data/gamma_example.h5'
        self.camera_type = 'LST_LSTCam'
        self.targets = collections.OrderedDict({
            'energy': {
                'output_shape': 1,
                'unit': 'log10(TeV)',
            },
            'impact': {
                'output_shape': 2,
                'unit': 'km',
            },
            'direction': {
                'output_shape': 2,
                'unit': 'radian',
            },
            'class': {
                'output_shape': 2,
                'label_shape': 1,
                'unit': None,
            },
        })
        self.group_by_image = {
            0: {
                'image_0': np.float32(2.9275095),
                'image_950': np.float32(4.3886013),
                'image_1854': np.float32(-2.5380642),
                'time_0': np.float32(4.),
                'time_950': np.float32(18.),
                'time_1854': np.float32(20.),
                'labels': {
                    'energy': np.float32(0.01640345),
                    'corex': np.float32(-40.23255),
                    'corey': np.float32(-207.50215),
                    'alt': np.float32(1.2172362),
                    'az': np.float32(3.2659276)
                },
                'telescope': {
                    'alt': np.float32(1.2217305),
                    'az': np.float32(3.1415927),
                    'position': np.array([30.91, -64.54, 43.])
                }
            },
            16: {
                'image_0': np.float32(-1.663076),
                'image_950': np.float32(1.2384766),
                'image_1854': np.float32(.16535203),
                'time_0': np.float32(13.),
                'time_950': np.float32(14.),
                'time_1854': np.float32(31.),
                'labels': {
                    'energy': np.float32(0.03191287),
                    'corex': np.float32(-60.348785),
                    'corey': np.float32(40.010925),
                    'alt': np.float32(1.2556471),
                    'az': np.float32(3.1234822)
                },
                'telescope': {
                    'alt': np.float32(1.2217305),
                    'az': np.float32(3.1415927),
                    'position': np.array([30.91, -64.54, 43.])
                }
            },
        }

        self.group_by_all = {
            10: {
                'image_0': np.float32(-1.663076),
                'image_950': np.float32(1.2384766),
                'image_1854': np.float32(.16535203),
                'time_0': np.float32(13.),
                'time_950': np.float32(14.),
                'time_1854': np.float32(31.),
                'labels': {
                    'energy': np.float32(0.03191287),
                    'corex': np.float32(-60.348785),
                    'corey': np.float32(40.010925),
                    'alt': np.float32(1.2556471),
                    'az': np.float32(3.1234822)
                },
                'telescope': {
                    'alt': np.float32(1.2217305),
                    'az': np.float32(3.1415927),
                    'position': np.array([30.91, -64.54, 43.])
                }
            },
        }

        self.group_by_triggered = {
            12: {
                'image_0_0': np.float32(-1.6636664),
                'image_0_950': np.float32(-0.36771095),
                'image_0_1854': np.float32(-1.7226539),
                'time_0_0': np.float32(38.),
                'time_0_950': np.float32(8.),
                'time_0_1854': np.float32(10.),
                'image_1_0': np.float32(0.18670945),
                'image_1_950': np.float32(-0.013801108),
                'image_1_1854': np.float32(-2.0320477),
                'time_1_0': np.float32(0.),
                'time_1_950': np.float32(11.),
                'time_1_1854': np.float32(29.),
                'labels': {
                    'energy': np.float32(0.02468489),
                    'corex': np.float32(75.495895),
                    'corey': np.float32(-66.52175),
                    'alt': np.float32(1.1956633),
                    'az': np.float32(3.2049599)
                },
                'telescope': {
                    'alt': np.float32(1.2217305),
                    'az': np.float32(3.1415927),
                }
            },
        }

    def test_mono(self):

        dataset = dsets.DL1DHDataset(self.data_file, self.camera_type, 'image', self.targets, use_time=True)
        sample_0 = dataset[0]

        assert sample_0['image'][0, 0] == self.group_by_image[0]['image_0']
        assert sample_0['image'][0, 950] == self.group_by_image[0]['image_950']
        assert sample_0['image'][0, 1854] == self.group_by_image[0]['image_1854']
        assert sample_0['image'][1, 0] == self.group_by_image[0]['time_0']
        assert sample_0['image'][1, 950] == self.group_by_image[0]['time_950']
        assert sample_0['image'][1, 1854] == self.group_by_image[0]['time_1854']
        assert np.isclose(sample_0['label'][0], np.log10(self.group_by_image[0]['labels']['energy']))
        assert np.isclose(sample_0['mc_energy'], np.log10(self.group_by_image[0]['labels']['energy']))
        assert np.isclose(sample_0['label'][1], (self.group_by_image[0]['labels']['corex'] -
                                                 self.group_by_image[0]['telescope']['position'][0])/1000)
        assert np.isclose(sample_0['label'][2], (self.group_by_image[0]['labels']['corey'] -
                                                 self.group_by_image[0]['telescope']['position'][1]) / 1000)

        assert np.isclose(sample_0['label'][3], (self.group_by_image[0]['labels']['alt'] -
                                                 self.group_by_image[0]['telescope']['alt']))
        assert np.isclose(sample_0['label'][4], (self.group_by_image[0]['labels']['az'] -
                                                 self.group_by_image[0]['telescope']['az']))

        sample_16 = dataset[16]

        assert sample_16['image'][0, 0] == self.group_by_image[16]['image_0']
        assert sample_16['image'][0, 950] == self.group_by_image[16]['image_950']
        assert sample_16['image'][0, 1854] == self.group_by_image[16]['image_1854']
        assert sample_16['image'][1, 0] == self.group_by_image[16]['time_0']
        assert sample_16['image'][1, 950] == self.group_by_image[16]['time_950']
        assert sample_16['image'][1, 1854] == self.group_by_image[16]['time_1854']
        assert np.isclose(sample_16['label'][0], np.log10(self.group_by_image[16]['labels']['energy']))
        assert np.isclose(sample_16['mc_energy'], np.log10(self.group_by_image[16]['labels']['energy']))
        assert np.isclose(sample_16['label'][1], (self.group_by_image[16]['labels']['corex'] -
                                                  self.group_by_image[16]['telescope']['position'][0]) / 1000)
        assert np.isclose(sample_16['label'][2], (self.group_by_image[16]['labels']['corey'] -
                                                  self.group_by_image[16]['telescope']['position'][1]) / 1000)

        assert np.isclose(sample_16['label'][3], (self.group_by_image[16]['labels']['alt'] -
                                                  self.group_by_image[16]['telescope']['alt']))
        assert np.isclose(sample_16['label'][4], (self.group_by_image[16]['labels']['az'] -
                                                  self.group_by_image[16]['telescope']['az']))

    def test_stereo_all(self):
        dataset = dsets.DL1DHDataset(self.data_file, self.camera_type, 'event_all_tels', self.targets, use_time=True)
        sample_10 = dataset[10]

        assert sample_10['image'][6, 0] == self.group_by_all[10]['image_0']
        assert sample_10['image'][6, 950] == self.group_by_all[10]['image_950']
        assert sample_10['image'][6, 1854] == self.group_by_all[10]['image_1854']
        assert sample_10['image'][7, 0] == self.group_by_all[10]['time_0']
        assert sample_10['image'][7, 950] == self.group_by_all[10]['time_950']
        assert sample_10['image'][7, 1854] == self.group_by_all[10]['time_1854']
        assert np.isclose(sample_10['label'][0], np.log10(self.group_by_all[10]['labels']['energy']))
        assert np.isclose(sample_10['mc_energy'], np.log10(self.group_by_all[10]['labels']['energy']))
        assert np.isclose(sample_10['label'][1], (self.group_by_all[10]['labels']['corex']) / 1000)
        assert np.isclose(sample_10['label'][2], (self.group_by_all[10]['labels']['corey']) / 1000)
        assert np.isclose(sample_10['label'][3], (self.group_by_all[10]['labels']['alt'] -
                                                  self.group_by_all[10]['telescope']['alt']))
        assert np.isclose(sample_10['label'][4], (self.group_by_all[10]['labels']['az'] -
                                                  self.group_by_all[10]['telescope']['az']))

    def test_stereo_triggered(self):
        dataset = dsets.DL1DHDataset(self.data_file, self.camera_type, 'event_triggered_tels', self.targets, use_time=True)
        sample_12 = dataset[12]

        assert sample_12['image'][0, 0] == self.group_by_triggered[12]['image_0_0']
        assert sample_12['image'][0, 950] == self.group_by_triggered[12]['image_0_950']
        assert sample_12['image'][0, 1854] == self.group_by_triggered[12]['image_0_1854']
        assert sample_12['image'][1, 0] == self.group_by_triggered[12]['time_0_0']
        assert sample_12['image'][1, 950] == self.group_by_triggered[12]['time_0_950']
        assert sample_12['image'][1, 1854] == self.group_by_triggered[12]['time_0_1854']
        assert sample_12['image'][2, 0] == self.group_by_triggered[12]['image_1_0']
        assert sample_12['image'][2, 950] == self.group_by_triggered[12]['image_1_950']
        assert sample_12['image'][2, 1854] == self.group_by_triggered[12]['image_1_1854']
        assert sample_12['image'][3, 0] == self.group_by_triggered[12]['time_1_0']
        assert sample_12['image'][3, 950] == self.group_by_triggered[12]['time_1_950']
        assert sample_12['image'][3, 1854] == self.group_by_triggered[12]['time_1_1854']
        assert np.isclose(sample_12['label'][0], np.log10(self.group_by_triggered[12]['labels']['energy']))
        assert np.isclose(sample_12['mc_energy'], np.log10(self.group_by_triggered[12]['labels']['energy']))
        assert np.isclose(sample_12['label'][1], (self.group_by_triggered[12]['labels']['corex']) / 1000)
        assert np.isclose(sample_12['label'][2], (self.group_by_triggered[12]['labels']['corey']) / 1000)
        assert np.isclose(sample_12['label'][3], (self.group_by_triggered[12]['labels']['alt'] -
                                                  self.group_by_triggered[12]['telescope']['alt']))
        assert np.isclose(sample_12['label'][4], (self.group_by_triggered[12]['labels']['az'] -
                                                  self.group_by_triggered[12]['telescope']['az']))


if __name__ == '__main__':
    unittest.main()
