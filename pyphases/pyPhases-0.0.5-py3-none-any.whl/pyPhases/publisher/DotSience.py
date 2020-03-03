from abc import ABC, abstractmethod
from ..Phase import Phase
from .Publisher import Publisher

import os
import dotscience


class DotSience(Publisher):
    connected = False

    def publish(self, phase: Phase):
        if (DotSience.connected == False):
            DotSience.connected = True
            dotscience.connect(
                phase.getOption("username"),
                phase.getOption("apikey"),
                phase.getOption("projectname"),
                phase.getOption("url"),
            )

        MODEL_DIR = "./dist/model"

        def printLog(msg):
            logPre = "[DotScience] "
            print(logPre + msg)

        if (phase.config):
            for (value, name) in enumerate(phase.config):
                value = phase.config[name]
                printLog("add parameter: " + name + " = " + str(value))
                dotscience.parameter(name, value)
        if (phase.metrics):

            for (value, name) in enumerate(phase.metrics):
                value = phase.metrics[name]
                printLog("add metric: " + name + " = " + str(value))
                dotscience.metric(name, value)

        if (phase.summary):
            for (value, name) in enumerate(phase.summary):
                value = phase.summary[name]
                printLog("add summary: " + name + " = " + str(value))
                dotscience.summary(name, value)

        if (phase.inputs):
            for value in enumerate(phase.inputs):
                printLog("add input: " + str(value))
                dotscience.input(value)

        if (phase.model):
            if not os.path.isdir(MODEL_DIR):
                os.makedirs(MODEL_DIR)

            export_path = os.path.join(MODEL_DIR)

            phase.model.save(export_path + "/" + phase.modelName)
            printLog("export model")
            dotscience.model("tensorflow-model", phase.modelName, MODEL_DIR)
            dotscience.publish("training for " + phase.modelName, deploy=False)
            printLog("publish finished")
