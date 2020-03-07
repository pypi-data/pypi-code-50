from Model import Model, ModelTraining
from Preprocess import Preprocess, FitType


class BearingClassifier:
    def __init__(self, model_training_type: ModelTraining = ModelTraining.DE, fit_type: FitType = FitType.MFCC):
        self.preprocess = Preprocess(fit_type)
        self.model = Model(model_training_type)

    def load_wav(self):
        self.preprocess.load_wav()
        self.preprocess.compute()

    def predict_wav(self):
        return self.model.predict(self.preprocess.processed_data)
