import json
from random import choice


class RandomWords:
    def __init__(self):
        with open('animals.json') as f:
            self.data_store = json.load(f)

    def get_word(self):
        return choice(self.data_store)
