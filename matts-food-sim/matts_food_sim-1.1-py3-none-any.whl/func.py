import random


def rand_range_float(_range):
	""" Generate a random float between a tuple range """
	return round(random.uniform(_range[0], _range[1]), 2)


def rand_range_int(_range):
	""" Generate a random int between a tuple range """
	return random.randint(_range[0], _range[1])


def round_pence(_float):
	return round(_float, 2)
