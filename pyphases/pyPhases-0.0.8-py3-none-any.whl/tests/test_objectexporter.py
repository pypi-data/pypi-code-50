from unittest import TestCase
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from pyPhases.exporter import ObjectExporter


class ObjectExporterTest(TestCase):

    def test_kerasSequential(self):
        model = Sequential()
        model.add(Dense(32, input_dim=784))
        model.add(Activation('relu'))

        exporter = KerasExporter()

        self.assertEqual(exporter.checkType(model), True)

        string = exporter.export(model)

        self.assertEqual(isinstance(string, str), True)
        importedModel = exporter.importData(string)

        self.assertEqual(isinstance(importedModel, keras.Model), True)
        self.assertEqual(isinstance(importedModel, Sequential), True)




