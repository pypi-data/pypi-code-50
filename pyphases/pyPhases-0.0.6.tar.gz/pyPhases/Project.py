# from .Phase import Phase
from typing import Dict
from pyPhases.storage.Storage import DataNotFound
from pyPhases.decorator.ExportValidator import ExportValidator
from pyPhases.util.Logger import classLogger, Logger, LogLevel

@classLogger
class Project:
    """
    Represents a whole project with several phases

    Parameters
    ----------
    name : string
        name of the project
    namespace : string
        namespace of the project e.e tud.ibmt
    dataStorage : storage
        the storage engine that should be used for storing all kinds of data
        (the default is a Filestorage pointing to the data/ directory)
    """

    phases = {}
    name = "myProject"
    namespace = ""
    stages = []
    classes = []
    exporters = []
    classesMap = {}
    registeredData = {}
    config = {}
    dataStorage = []
    stageIndex = 0
    phaseIndex = 0
    decorators = []

    def debug(self):
        Logger.verboseLevel = LogLevel.DEBUG

    def __init__(self):
        self.registerDecorator(ExportValidator())

    def addStorage(self, storage):
        self.dataStorage.append(storage)

    def registerDecorator(self, decorator):
        self.logDebug("Register Decorator: " + type(decorator).__name__)
        self.decorators.append(decorator)

    def registerPublisher(self, publisher):
        self.logDebug("Register Publisher: " + type(publisher).__name__)
        self.registerDecorator(publisher)

    def registerExporter(self, exporter):
        self.logDebug("Register Exporter: " + type(exporter).__name__)
        self.exporters.append(exporter)

    def setClasses(self, classes):
        self.classes = classes
        for index, className in enumerate(self.classes):
            self.classesMap[className] = index

    def addStage(self, stageName: str):
        """ creates a stage for the project, a stage is a sequential list of phases
        Parameters
        ----------
        stageName : str
            a unique name of the stage that should be created
        """
        self.stages += [stageName]
        self.phases[stageName] = []

    def getDataId(self, dataName: str, version: str = "current"):
        return dataName + "-" + version

    def getExporterForIntsance(self, instance):
        self.logDebug("Get Exporter For: " + type(instance).__name__)
        return self.getExporterForType(type(instance))

    def getExporterForType(self, theType):
        for exporter in self.exporters:
            self.logDebug("Check: " + type(exporter).__name__)
            if exporter.checkType(theType):
                self.logDebug("Found exporter")
                return exporter
        return None

    def getData(self,
                dataName: str,
                expectedReturnType,
                version: str = "current"):
        dataId = self.getDataId(dataName, version)
        self.logDebug("Try to get DAta: " + dataId)

        # just generated Data
        if dataId in self.registeredData:
            self.logDebug("Data in memory: " + dataId)
            return self.registeredData[dataId]

        # load from storage layer
        for storage in self.dataStorage:
            try:
                self.logDebug("Check storage: " + type(storage).__name__)
                dataBytes = storage.read(dataId)
                self.logDebug("Data in storage: " + type(storage).__name__)
                exporter = self.getExporterForType(expectedReturnType)
                return exporter.importData(dataBytes)

            except DataNotFound:
                pass

        # regenerate from previous stage/s
        if (version == "current"):
            self.logWarning("Data " + dataId +
                  " was not found, rerunning previous stages for current data")

            for phase in self.getPhases():
                if dataName in phase.exportData:
                    phase.run()
                    return self.getData(dataName, expectedReturnType, version)

        raise Exception("Data " + dataId + " was not found")

    def registerData(self,
                     dataName: str,
                     data: str,
                     version: str = "current",
                     save: bool = True):
        dataId = self.getDataId(dataName, version)

        # save to runtime project
        self.registeredData[dataId] = data

        if (save == False):
            return

        if (self.dataStorage == None):
            self.logWarning("There was no datastorage registerd")
            return

        # save to storage layer
        exporter = self.getExporterForIntsance(data)

        if (exporter == None):
            self.logWarning("No exporter for datatype (" + type(data).__name__ +
                    ") the data " + dataName + " will not be automaticly save")
            return

        dataBytes = exporter.export(data)
        for storage in self.dataStorage:
            storage.write(dataId, dataBytes)

    def getConfig(self, name: str) -> str:
        return self.config[name]

    def addConfig(self, config) -> None:
        for name in config:
            if (name in self.config):
                Warning(
                    "The config name " + name +
                    " was specified in multiple phases and was overwritten by the latest!"
                )

            self.config[name] = config[name]

    def addPhase(self, phase, stage: str = "", name: str = None):
        if (name != None):
            phase.name = name

        self.addConfig(phase.config)
        phase.project = self

        if (not stage in self.phases):
            raise Exception('The stage to this phase was not added before!')

        self.phases[stage] += [phase]

    def runAllStages(self):
        for stageName in self.stages:
            self.runStage(stageName)

    def runStage(self, stageName):
        print("RUN stage " + stageName)
        for phase in self.phases[stageName]:
            phase.run()

    def run(self, stageName=None):
        if (stageName == None):
            self.runAllStages()
        else:
            self.runStage(stageName)

    def getPhases(self):
        for stageName in self.stages:
            for phase in self.phases[stageName]:
                yield phase
