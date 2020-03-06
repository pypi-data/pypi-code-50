"""
Create a new Project
"""
import os
from pathlib import Path
from json import dumps
from .base import Base
from inspect import getmembers
import sys
from distutils.dir_util import copy_tree
from ..util.Logger import classLogger, LogLevel

import yaml
import pystache
import pyPhases


class Misconfigured(Exception):
    pass


@classLogger
class Create(Base):
    """create a Phase-Project"""

    config = None
    outputDir = None
    templateDir = "generate-template/"
    staticFilesDir = "static-template/"
    projectFileName = "project.yaml"
    packagePath = os.path.dirname(sys.modules["phases"].__file__)
    forceWrite = False

    def parseRunOptions(self):
        if (self.options['-o']):
            self.outputDir = self.options['-o']
            self.logDebug("Set Outputdir: %s" % (self.outputDir))
        if (self.options['-p']):
            self.projectFileName = self.options['-p']
            self.logDebug("Set Projectfile: %s" % (self.projectFileName))
        if (self.options['-f']):
            self.forceWrite = True

    def beforeRun(self):
        self.parseRunOptions()
        self.templateDir = self.getPackagePath(self.templateDir)
        self.staticFilesDir = self.getPackagePath(self.staticFilesDir)

    def getPackagePath(self, path):
        d = os.path.dirname(sys.modules["phases"].__file__)
        return os.path.join(d, path)

    def validateConfig(self, config):
        # check required fields
        required = ['name', 'namespace', 'phases']
        for field in required:
            if (not field in config):
                raise Misconfigured(
                    u"%s is required in the project yaml file" % (field))

        # set default values
        defaultValues = {
            'storage': ['FileStorage'],
            'publisher': [],
            'exporter': ['ObjectExporter'],
            'usedClasses': [],
        }
        # for field in defaultValues:
        for field in defaultValues:
            if (not field in config):
                config[field] = defaultValues[field]

    def normalizeDict(self, dictObj):
        arrayForTemplate = []

        for (__, name) in enumerate(dictObj):
            arrayForTemplate.append({"name": name, "value": dictObj[name]})
        return arrayForTemplate

    def normalizeDataArray(self, objectOrString):
        if (isinstance(objectOrString, str)):
            return {"name": objectOrString, "description": ""}

        if (not "name" in objectOrString):
            raise Exception("One Object does not have a name")

        if ("config" in objectOrString):
            objectOrString["config"]["items"] = self.normalizeDict(
                objectOrString["config"])

        return objectOrString

    def normalizeConfigArrays(self):
        arrayFields = ["publisher", "storage", "exporter"]
        for field in arrayFields:
            for index, arrayOrString in enumerate(self.config[field]):
                obj = self.normalizeDataArray(arrayOrString)
                obj = self.registerClassName(obj, field)
                self.config[field][index] = obj

    def checkIfClassExistsInPyPhases(self, className, package):
        if (not package in dir(pyPhases)):
            return False

        return className in dir(pyPhases.__dict__[package])

    def preparePhases(self):
        # flatten phases and extract stages
        self.config['stages'] = []
        self.config['userPhases'] = []
        self.config['phaseClasses'] = []
        lastPhase = None
        for stageName in self.config['phases']:
            self.config['stages'].append(stageName)
            for phase in self.config['phases'][stageName]:
                phase['stage'] = stageName
                self.config['userPhases'].append(phase)
                self.registerClassName(phase, "phases")
                if (lastPhase != None):
                    lastPhase["next"] = phase
                lastPhase = phase
        self.config["phases"] = self.config['userPhases']

    def registerClassName(self, classObj, package):
        className = classObj["name"]
        ucFirstClassname = className[0].upper() + className[1:]
        userClassName = "user" + ucFirstClassname
        systemClassName = "system" + ucFirstClassname

        self.config[userClassName] = []
        self.config[systemClassName] = []

        systemclass = self.checkIfClassExistsInPyPhases(className, package)
        if (systemclass):
            packagePre = 'pyPhases.'
        else:
            packagePre = ''

        classObj['package'] = packagePre + package
        classObj['packageName'] = package
        classObj['system'] = systemclass

        if (systemclass):
            self.config[systemClassName].append(classObj)
        else:
            self.config[userClassName].append(classObj)
        self.config['usedClasses'].append(classObj)
        return classObj

    def run(self):
        self.beforeRun()
        projectFile = open(self.projectFileName, "r")
        yamlContent = projectFile.read()
        projectConfig = yaml.load(yamlContent, Loader=yaml.SafeLoader)

        # self.log("validate config")
        self.validateConfig(projectConfig)
        if (self.outputDir == None):
            self.outputDir = projectConfig["name"]
        self.config = projectConfig
        self.normalizeConfigArrays()

        self.preparePhases()
        self.preparePackageConfig()

        self.copyStaticFiles()
        self.generateInitFiles()
        self.generateFilesFromConfig()

    def preparePackageConfig(self):
        self.config['packages'] = []
        packages = {}
        for classObj in self.config['usedClasses']:
            if not classObj["system"]:
                if (classObj["packageName"] in packages):
                    packages[classObj["packageName"]]["imports"].append(
                        classObj["name"])
                else:
                    packages[classObj["packageName"]] = {
                        'name': classObj["packageName"],
                        'imports': [classObj["name"]]
                    }
        for name in packages:
            self.config['packages'].append(packages[name])

    def copyStaticFiles(self):
        self.log("Copy static files")
        self.log(
            "Copy static files from %s to %s" %
            (self.staticFilesDir, self.outputDir), LogLevel.DEBUG)

        copy_tree(self.staticFilesDir, self.outputDir)

    def generateInitFiles(self):
        # this method assumes the python files will be saved in {{name}}
        self.log("Generate init Files")
        for package in self.config["packages"]:
            templateFile = open(self.templateDir + "packages.m", "r")
            templateContent = templateFile.read()

            path = self.outputDir + '/' + self.config["name"] + "/" + package[
                "name"] + "/"

            self.writeTemplateFile(path, '__init__.py', templateContent,
                                   package)

    def generateFilesFromConfig(self):
        self.log("Generate files for the project with template files")
        outputDir = self.outputDir
        # iterate all template files (*.m files are for manual use)
        pathlist = Path(self.templateDir).glob('**/*.mustache')
        for path in pathlist:
            templateFile = open(path, "r")
            templateContent = templateFile.read()
            pathDiff = os.path.relpath(path.parent, Path(self.templateDir))

            fileName = pystache.render(path.stem, self.config)
            pathDiff = pystache.render(pathDiff, self.config)
            relPath = os.path.join(outputDir, pathDiff)

            self.logDebug("write template %s to path to %s" %
                          (path.stem, relPath))

            if (not fileName in self.config):
                self.writeTemplateFile(relPath, fileName, templateContent)
            else:
                for obj in self.config[fileName]:
                    if (not obj["system"]):
                        self.log("Create stub for %s/%s" %
                                 (fileName, obj["name"]))
                        self.writeTemplateFile(relPath + '/' + fileName,
                                               obj["name"] + '.py',
                                               templateContent, obj)

    def writeTemplateFile(self, path, filename, tplString,
                          templateObject=None):
        if templateObject == None:
            templateObject = self.config

        if not os.path.exists(path):
            os.makedirs(path)

        fullPath = path + '/' + filename
        self.logDebug("Write file %s" % (fullPath))
        if self.forceWrite or not os.path.isfile(fullPath):
            fileContent = pystache.render(tplString, templateObject)
            file = open(fullPath, "w")
            file.write(fileContent)
            file.close()
        else:
            self.logWarning(
                "File %s allready exists and was not overwritten, use the option -f to force to overwrite it "
                % (fullPath))
