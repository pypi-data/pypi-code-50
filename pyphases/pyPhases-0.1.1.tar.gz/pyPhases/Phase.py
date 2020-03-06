import os
from pyPhases import Project
from pyPhases.util.Logger import classLogger
from pyPhases.util.Optionizable import Optionizable


class Phase(Optionizable):
    name = ""
    config = {}
    metrics = {}
    summary = {}
    inputs = []
    model = None
    runMethod = "main"
    project: Project = None
    exportData = []
    decorators = None

    def __init__(self, name = "undefined"):
        self.name = name

    def getDecorators(self):
        if not self.decorators == None:
            return self.decorators

        self.decorators = []
        for decorator in self.project.decorators:
            if(decorator.filter(self)):
                self.decorators.append(decorator)

        return self.decorators

    def run(self):
        self.log("RUN Phase: " + self.name)

        def methodNotFound():
            self.logError("The Current Phase needs the followin method defined: " +
                      self.runMethod)

        method = getattr(self, self.runMethod, methodNotFound)
        decorators = self.getDecorators()

        for decorator in decorators:
            decorator.before(self)

        method()

        for decorator in decorators:
            decorator.after(self)
