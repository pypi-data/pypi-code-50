from numpy import isclose
import numpy as np
from pyqcs import State, H, sample


def test_avg_preseved_nsample100():
    state = H(0) * State.new_zero_state(10)

    results = sample(state, 0b1, 100)

    assert isclose(results[0]/100, 1/2, atol=(1/4) / 100**0.5)

def test_avg_preseved_nsample10000():
    #np.random.seed(0xdeadbee)
    state = H(0) * State.new_zero_state(10)

    results = sample(state, 0b1, 10000)

    assert isclose(results[0]/10000, 1/2, atol=(1/4) / (10000**0.5 - 2))
