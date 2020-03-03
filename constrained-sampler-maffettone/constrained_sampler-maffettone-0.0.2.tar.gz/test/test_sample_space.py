import unittest
import os
import time
from constrained_sampler.sample_space import SampledSpace

class SampledSpaceTestCase(unittest.TestCase):
    def setUp(self):
        self.space = SampledSpace(os.path.join(os.path.dirname(__file__), '../examples/mixture.txt'), random_state=1234)
        self.example = self.space.current

    def test_len(self):
        self.assertEqual(len(self.space), 1)

    def test_empty(self):
        self.assertFalse(self.space.empty)

    def test_valid(self):
        self.assertTrue(self.space.valid(self.example))

    def test_redundant(self):
        self.space.register(self.example)
        self.assertEqual(len(self.space), 1)

    def test_register(self):
        self.space.register([0.25, 0.25])
        self.assertEqual(len(self.space), 2)

    def test_timeout(self):
        start = time.time()
        self.space.adaptive_displacement(total_steps=10**5, feedback_rate=1, timeout=1/60)
        finish = time.time() - start
        self.assertLessEqual(finish, 2.)
        self.space._cache = set()
        self.space.register(self.example)

    def test_sample_warn(self):
        with self.assertWarns(UserWarning):
            self.space.sample_space(100)

if __name__ == '__main__':
    unittest.main()
