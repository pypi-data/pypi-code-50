import unittest
import os
from constrained_sampler.constraints import Constraint


class ConstraintTestCase(unittest.TestCase):
    def setUp(self):
        self.constraint = Constraint(os.path.join(os.path.dirname(__file__), '../examples/mixture.txt'))

    def test_example(self):
        self.assertListEqual([0., 0.], self.constraint.get_example())

    def test_ndim(self):
        self.assertEqual(self.constraint.get_ndim(), 2)

    def test_apply(self):
        self.assertTrue(self.constraint.apply(self.constraint.get_example()))
        self.assertFalse(self.constraint.apply([1., 1.]))


if __name__ == '__main__':
    unittest.main()
