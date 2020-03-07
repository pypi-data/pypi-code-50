from enum import Enum
import pickle
import numpy as np


class ModelTraining(Enum):
    FE = "./models/FE12K_MLP"
    DE = "./models/DE12K_MLP"


class Model:

    def __init__(self, model_training_type: ModelTraining):
        self.model = None
        self.__load_model(model_training_type)
        self.classes = {0: "ball", 1: "inner_race", 2: "out_race", 3: "normal"}

    def __load_model(self, model_training_type: ModelTraining):
        self.model = pickle.load(open(model_training_type.value, 'rb'))

    def predict(self, x: np.array):
        if self.model is not None:
            predictions = self.model.predict(x)
            unique, counts = np.unique(predictions, return_counts=True)
            dictionary = dict(zip(unique, counts))
            predominant_class = max(dictionary, key=dictionary.get)
            confidence_percentage = (dictionary[max(dictionary, key=dictionary.get)] / predictions.shape) * 100

            return self.classes[predominant_class], confidence_percentage
