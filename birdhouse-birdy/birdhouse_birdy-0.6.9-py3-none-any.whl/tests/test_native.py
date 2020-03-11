import pytest
import json
from birdy import native_client


@pytest.mark.online
def test_birdymod_asref():
    m = native_client(url="http://localhost:5000/wps")
    assert m.hello('david') == 'Hello david'
    assert m.binaryoperatorfornumbers(inputa=1, inputb=2, operator='add') == 3.0
    assert m.dummyprocess(10, 20) == ['11', '19']

    txt, ref = m.multiple_outputs(2)

    assert type(txt) == str
    assert type(ref) == str

@pytest.mark.online
def test_birdymod_asobj():
    m = native_client(url="http://localhost:5000/wps", asobject=True)
    assert m.hello('david') == 'Hello david'
    assert m.binaryoperatorfornumbers(inputa=1, inputb=2, operator='add') == 3.0
    assert m.dummyprocess(10, 20) == ['11', '19']

    txt, ref = m.multiple_outputs(2)

    assert type(txt) == str
    assert type(ref) == dict


@pytest.mark.online
def test_only_one():
    m = native_client(url="http://localhost:5000/wps", processes=['nap'])
    assert len(dir(m)) == 1

    m = native_client(url="http://localhost:5000/wps", processes='nap')
    assert len(dir(m)) == 1

