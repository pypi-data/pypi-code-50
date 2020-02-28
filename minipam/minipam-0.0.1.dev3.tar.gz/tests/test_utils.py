import pytest
from minipam import isip, ismac, format_mac


class TestIsIP:
    def test_isip_format(self):
        assert isip('127.0.0.1') is True
        assert isip('127.0.1') is False

    def test_isip_errors(self):
        with pytest.raises(TypeError):
            isip(1)
        with pytest.raises(TypeError):
            isip(())
        with pytest.raises(TypeError):
            isip([])
        with pytest.raises(TypeError):
            isip({})


class TestIsMAC:
    def test_ismac_format(self):
        assert ismac('1234567890ab') is True
        assert ismac('1234567890a') is False

    def test_ismac_errors(self):
        with pytest.raises(TypeError):
            ismac(1)
        with pytest.raises(TypeError):
            ismac(())
        with pytest.raises(TypeError):
            ismac([])
        with pytest.raises(TypeError):
            ismac({})


class TestFormatMAC:
    def test_format_mac_format(self):
        assert format_mac('1234567890ab') == '12:34:56:78:90:ab'
        assert format_mac('1234567890ab', delimiter='.') == '12.34.56.78.90.ab'
        assert format_mac('1234567890ab', upper=True) == '12:34:56:78:90:AB'

    def test_format_mac_errors(self):
        with pytest.raises(TypeError):
            format_mac(1)
        with pytest.raises(TypeError):
            format_mac(())
        with pytest.raises(TypeError):
            format_mac([])
        with pytest.raises(TypeError):
            format_mac({})

        with pytest.raises(ValueError):
            format_mac('1234567890a', delimiter='*')
        with pytest.raises(ValueError):
            format_mac('12*34*56*78*90*ab', delimiter=5)

        with pytest.raises(ValueError):
            format_mac('1234567890ab', delimiter='*')
        with pytest.raises(ValueError):
            format_mac('1234567890ab', delimiter=5)
