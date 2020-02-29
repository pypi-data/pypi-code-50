import pytest

class Flo:
    """Checks command line input/output flow
    Supplies print and input methods that are meant to be injected into command line applications

    Will confirm that the prints/inputs/responses all match the given list of interactions
    """
    def __init__(self, interactions=None):

        if interactions is None:
            interactions = []
        self.interactions = interactions

    def add_print(self, text):
        self.interactions += [{"text":text,"type":"print"}]


    def add_input(self, text, response):
        self.interactions += [{"text":text,"type":"input","response":response}]


    def add_interactions(self, interactions):
        self.interactions += interactions

    def print(self, *args):
        interaction = self.interactions.pop(0)
        assert interaction["type"] == "print"
        assert interaction["text"] == args[0]

    def input(self, *args):
        interaction = self.interactions.pop(0)
        assert interaction["type"] == "input"
        assert interaction["text"] == args[0]
        return interaction["response"]

    def exit(self):
        return len(self.interactions) == 0


@pytest.fixture
def flo():
    return Flo()
