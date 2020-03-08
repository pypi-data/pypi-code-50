import tensorflow as tf
import keras_sparsity_pattern as spat


class TestSparsityPattern(tf.test.TestCase):
    def test1(self):
        sp = spat.get('diag', 3)
        target = [(0, 0), (1, 1), (2, 2)]
        self.assertAllEqual(sp, target)

    def test2(self):
        sp = spat.get('dense', 2)
        target = [(0, 0), (0, 1), (1, 0), (1, 1)]
        self.assertAllEqual(sp, target)

    def test3(self):
        sp = spat.get('dense', 2, 3)
        target = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
        self.assertAllEqual(sp, target)

    def test4(self):
        sp = spat.get('nodiag', 3)
        target = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
        self.assertAllEqual(sp, target)

    def test5(self):
        sp = spat.get('nodiag', 2, 3)
        target = [(0, 1), (0, 2), (1, 0), (1, 2)]
        self.assertAllEqual(sp, target)

    def test6(self):
        sp = spat.get('block', 4, 2)
        target = [(0, 0), (0, 1), (1, 0), (1, 1),
                  (2, 2), (2, 3), (3, 2), (3, 3)]
        self.assertAllEqual(sp, target)

    def test7(self):
        sp = spat.get('block', 3, [2, 2])
        target = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2)]
        self.assertAllEqual(sp, target)

    def test8(self):
        sp = spat.get('circle', 5, [1, 1])
        target = [(0, 4), (1, 0), (2, 1), (3, 2), (4, 3)]
        self.assertAllEqual(sp, target)


if __name__ == "__main__":
    tf.test.main()
