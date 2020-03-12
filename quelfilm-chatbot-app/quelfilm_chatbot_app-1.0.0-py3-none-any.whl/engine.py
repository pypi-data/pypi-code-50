import os
from nlp_tools.preprocessing import Preprocessing
from nlp_tools.loaders import MdLoader
from nlp_tools.representations import MergedMatrixRepresentation
from nlp_tools.classifiers import ClassificationProcessor, NaiveBayseTfIdfClassifier
from nlp_tools.utils import get_random_message

from quelfilm.settings import *


def build_classifier():
    loader = MdLoader(os.path.join('', TRAINING_PATH))
    processor = Preprocessing(loader)
    repres = MergedMatrixRepresentation(processor.data)
    classifier = ClassificationProcessor(NaiveBayseTfIdfClassifier(), repres.data)
    classifier.train()

    def predict(text: str):
        message = repres.process_new_data(processor.process_sentence(text))
        intent, score = classifier.predict(message)
        response = get_random_message(processor.responses[intent])
        return intent, score, response
    return predict


class Classifier:
    def __init__(self):
        self.predict = build_classifier()
