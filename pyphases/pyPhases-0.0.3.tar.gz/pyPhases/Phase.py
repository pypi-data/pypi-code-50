import os
from .Project import Project


def publishafterwards(func):
    def wrapper(self, *args):
        val = func(self, *args)
        self.publish()
        return val

    return wrapper


class Phase:
    name = ""
    config = {}
    metrics = {}
    summary = {}
    inputs = []
    model = None
    runMethod = "main"
    project: Project = None
    exportData = []
    decorators = []

    def __init__(self, name = "undefined"):
        self.name = name

    def run(self):
        print("RUN Phase: " + self.name)

        def methodNotFound():
            Exception("The Current Phase needs the followin method defined: " +
                      self.runMethod)

        method = getattr(self, self.runMethod, methodNotFound)

        for decorator in self.decorators:
            decorator.before(self)

        method()

        for decorator in self.decorators:
            decorator.before(self)
