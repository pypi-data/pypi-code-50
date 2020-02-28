from unittest import TestCase
from pyPhases import Project
from pyPhases.exporter import ObjectExporter
from pyPhases.storage import FileStorage
# from pyPhases.exporter.ObjectExporter import ObjectExporter
# import pyPhases


class PhaseTest(TestCase):
    # def test_addPhases(self):
    #     self.assertEqual(expected, actual)

    def test_project(self):

        # pyPhases.Project.Project()
        # Project setup
        project = Project()
        project.registerExporter(ObjectExporter())

        project.name = 'sleepClassificationCNN'
        project.namespace = 'tud.ibmt'
        project.setClasses(['Wach', 'Leichter Schlaf', 'Tiefer Schlaf', 'REM'])

        # stages
        project.addStage('prepareData')
        project.addStage('train')
        project.addStage('evaluate')


        # add filestorage and data exporter
        project.dataStorage = FileStorage("data/")

