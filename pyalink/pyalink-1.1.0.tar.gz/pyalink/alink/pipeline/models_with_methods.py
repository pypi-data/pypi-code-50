from .common.pipeline_op_3 import _Word2VecModel
from .common.pipeline_op_1 import _GeneralizedLinearRegressionModel
from .base import BatchOperatorWrapper


class Word2VecModel(_Word2VecModel):
    def getVectors(self):
        return BatchOperatorWrapper(self.get_j_obj().getVectors())


class GeneralizedLinearRegressionModel(_GeneralizedLinearRegressionModel):
    def evaluate(self, data):
        return BatchOperatorWrapper(self.get_j_obj().evaluate(data.get_j_obj()))
