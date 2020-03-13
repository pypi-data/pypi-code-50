import random


class Event:
	def __init__(self, prob, amount_percent):
		self.prob = prob
		self.amount = amount_percent


class Events:
	houses = Event(0.1, (0.05, 0.2))
