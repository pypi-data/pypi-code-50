from .common.batch_op_3 import _SummarizerBatchOp
from .common.batch_op_1 import _ChiSqSelectorBatchOp, _ChiSquareTestBatchOp, _EvalBinaryClassBatchOp, \
    _EvalClusterBatchOp, _EvalRegressionBatchOp, _EvalMultiClassBatchOp, _CorrelationBatchOp
from ..converters import j_value_to_py_value
from ..with_params import JavaObjectWrapper


class Metrics(JavaObjectWrapper):
    def __init__(self, j_obj):
        self.j_obj = j_obj

    def get_j_obj(self):
        return self.j_obj

    def __dir__(self):
        keys = self.get_j_obj().__dir__()
        return keys

    def __getattr__(self, func_name):
        def wrapped_func(func):
            def inner(*args, **kwargs):
                retval = func(*args, **kwargs)
                return j_value_to_py_value(retval)
            return inner
        # assume all access are functions
        func = self.get_j_obj().__getattr__(func_name)
        return wrapped_func(func)


class ChiSquareTestResult(JavaObjectWrapper):
    def get_j_obj(self):
        return self._j_obj

    def __init__(self, j_obj):
        self._j_obj = j_obj
        self.df = j_obj.df
        self.p = j_obj.p
        self.value = j_obj.value
        self.comment = j_obj.comment


class CorrelationResult(JavaObjectWrapper):
    def get_j_obj(self):
        return self._j_obj

    def __init__(self, j_obj):
        self._j_obj = j_obj
        self.colNames = j_obj.colNames
        self.correlation = j_obj.correlation

    def getCorrelation(self):
        retval = self.get_j_obj().getCorrelation()
        return [
            [col for col in retval[index]]
            for index, row in enumerate(retval)
        ]

    def getColNames(self):
        return list(self.get_j_obj().getColNames())

    def toString(self):
        return self.get_j_obj().toString()


class TableSummary(JavaObjectWrapper):
    def get_j_obj(self):
        return self._j_obj

    def __init__(self, j_obj):
        self._j_obj = j_obj

    def __dir__(self):
        keys = self.get_j_obj().__dir__()
        return keys

    def __getattr__(self, func_name, *args):
        # assume all access are functions
        retval = self.get_j_obj().__getattr__(func_name, *args)
        return j_value_to_py_value(retval)


class EvalBinaryClassBatchOp(_EvalBinaryClassBatchOp):
    def collectMetrics(self):
        return Metrics(self.get_j_obj().collectMetrics())


class EvalClusterBatchOp(_EvalClusterBatchOp):
    def collectMetrics(self):
        return Metrics(self.get_j_obj().collectMetrics())


class EvalRegressionBatchOp(_EvalRegressionBatchOp):
    def collectMetrics(self):
        return Metrics(self.get_j_obj().collectMetrics())


class EvalMultiClassBatchOp(_EvalMultiClassBatchOp):
    def collectMetrics(self):
        return Metrics(self.get_j_obj().collectMetrics())


class ChiSquareTestBatchOp(_ChiSquareTestBatchOp):
    def collectChiSquareTestResult(self):
        return map(lambda d: ChiSquareTestResult(d), self.get_j_obj().collectChiSquareTestResult())


class CorrelationBatchOp(_CorrelationBatchOp):
    def collectCorrelationResult(self):
        return CorrelationResult(self.get_j_obj().collectCorrelationResult())


class SummarizerBatchOp(_SummarizerBatchOp):
    def collectSummary(self):
        return TableSummary(self.get_j_obj().collectSummary())


class ChiSqSelectorBatchOp(_ChiSqSelectorBatchOp):
    def collectResult(self):
        return list(self.get_j_obj().collectResult())
