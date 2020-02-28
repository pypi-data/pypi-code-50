from easydict import EasyDict as edict

__C = edict()

cfg = __C

# the latest supported opset
__C.LATEST_OPSET = 10

# the opsets to test
__C.TO_TEST_OPSETS = [7, 8, 9, 10]