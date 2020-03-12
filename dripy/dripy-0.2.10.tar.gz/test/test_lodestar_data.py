import os
from time import time
import unittest

from numpy import array, argmax, interp

from dripy.lodestar import LodeStarData
from test import TEST_LODESTAR_DATA, compare_objects


class Test_LodeStarData(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        t_1 = time()
        cls.lodestar = LodeStarData(TEST_LODESTAR_DATA)                        
        t_2 = time()
        cls.lodestar_from_pickle = LodeStarData(TEST_LODESTAR_DATA)        
        t_3 = time()
        
        print('Load time without pickle\t|\t{}\nLode time with pickle\t|\t{}'.format(t_2-t_1, t_3-t_2))
        
        cls.pickle_filename = os.path.join(os.path.dirname(TEST_LODESTAR_DATA), '.' + os.path.splitext(os.path.split(TEST_LODESTAR_DATA)[-1])[0] + '.pkl')        

    def test_pickle_file_created(self):
        self.assertTrue(os.path.isfile(self.pickle_filename))
    
    def test_came_from_pickle(self):
        self.assertTrue(self.lodestar_from_pickle._came_from_pickle)
    
    def test_not_came_from_pickle(self):
        self.assertFalse(self.lodestar._came_from_pickle)
    
    def test_original_same_as_depickled(self):        
        self.assertListEqual(compare_objects(self.lodestar, self.lodestar_from_pickle), ['Value of _came_from_pickle attribute differs. object_1._came_from_pickle = False, object_2._came_from_pickle = True'])
    
    def test_slicing(self):
        sliced_lodestar = self.lodestar_from_pickle.slice_at_indices(5,10)
        self.assertTrue(True)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(cls.pickle_filename)

class Test_LodeStarDataResample(unittest.TestCase):

    def setUp(self):
        self.resampled_lodestar = LodeStarData(TEST_LODESTAR_DATA, write_pickle=False, resample_time=.021)

    def test_resampled_time(self):
        expected_times = [0, 0.021, 0.042]
        self.assertListEqual(self.resampled_lodestar.data.index.values[:3], expected_times)
    
    def test_resampled_rpm(self):

        lodestar = LodeStarData(TEST_LODESTAR_DATA, write_pickle=False)

        rpm_int = []
        rpm_test = []

        for i in [3, 6]:
            rpm_int.append(round(interp(self.resampled_lodestar.data.index.values[i], lodestar.data.index.values, lodestar.rpm), 4))
            rpm_test.append(round(self.resampled_lodestar.rpm[i], 3))

        self.assertListEqual(rpm_test, rpm_int)

    def tearDown(self):
        return
