from waky.core.device import Device


# content of test_sample.py
def test_device_localhost():
    localhost = Device("localhost")
    assert localhost.hostname == "localhost"
