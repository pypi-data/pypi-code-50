# Insert awesome code
import numpy as np

def semmo_function1(x):
	assert isinstance(x, str), "What up?? I only understand letters man"
	return "\\"*30+x+"/"*30

def semmo_function2(x):
	assert isinstance(x, float), "What up?? I only understand numbers man"
	return "The squareroot is:{}".format(np.sqrt(x))


