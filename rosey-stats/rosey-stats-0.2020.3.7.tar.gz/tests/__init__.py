import pytest
import numpy as np
from rosey_stats import neg_log_p


def test_neg_log_p():
    np.testing.assert_allclose(
        neg_log_p([0.1, 0.01, 1e-6, 10]),
        [1, 2, 6, -1]
    )
