import numpy as np
from .utils import approx

from flatspin import SpinIce
from numpy.testing import assert_array_equal

def test_init_no_temp(opencl):
    si = SpinIce(thermal_std=0, **opencl)
    assert si.h_therm is 0
    assert_array_equal(si.thermal_fields(),np.zeros((si.spin_count,2)))
    assert np.all([(si.thermal_field(i) is 0) for i in si.indices()])

def test_init_temp(opencl):
    si = SpinIce(thermal_std=1, **opencl)
    assert isinstance(si.h_therm, np.ndarray)
    assert np.all([isinstance(si.thermal_field(i),np.ndarray) for i in si.indices()])

    assert not si.thermal_fields() == approx(0)

def test_flip(opencl):
    si = SpinIce(thermal_std=1, **opencl)
    tf1 = si.thermal_fields()

    for i in range(0, si.spin_count, 2):
        si.flip(i)
    tf2 = si.thermal_fields()

    #field same for unchanged magnets
    assert tf1[range(1, si.spin_count, 2)] == approx(tf2[range(1, si.spin_count, 2)])
    #field flipped for flipped magnets
    assert tf1[range(0, si.spin_count, 2)] == approx(-tf2[range(0, si.spin_count, 2)])

def test_relax(opencl):
    si = SpinIce(thermal_std=1, **opencl)
    tf1 = si.thermal_fields()
    si.relax()

    assert si.thermal_fields() != approx(tf1)

