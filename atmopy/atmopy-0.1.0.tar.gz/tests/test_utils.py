""" Tests on atmopy utilities """

import pytest

from atmopy.utils import AltitudeValueError, check_altitude

def test_altitude_custom_exception():
    """ Test on custom altitude exception """
    with pytest.raises(AltitudeValueError) as execinfo:
        raise AltitudeValueError(0, 1000)

    assert execinfo.value.args[0] == "Altitude must be within range [0, 1000] meters"
    assert str(execinfo.value) == "Altitude must be within range [0, 1000] meters"

def test_check_altitude_raises_exception():
    """ Test if altitude within range """
    alt, min_alt, max_alt = -500, 0, 1000
    with pytest.raises(AltitudeValueError) as execinfo:
        check_altitude(alt, min_alt, max_alt)
