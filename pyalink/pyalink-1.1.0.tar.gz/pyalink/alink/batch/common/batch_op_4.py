#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..base import BatchOperator, BaseSinkBatchOp


class Word2VecPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.Word2VecPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Word2VecPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setWordDelimiter(self, val):
        return self._add_param('wordDelimiter', val)

    def setPredMethod(self, val):
        return self._add_param('predMethod', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class Word2VecTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.Word2VecTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Word2VecTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setNumIter(self, val):
        return self._add_param('numIter', val)

    def setVectorSize(self, val):
        return self._add_param('vectorSize', val)

    def setAlpha(self, val):
        return self._add_param('alpha', val)

    def setWordDelimiter(self, val):
        return self._add_param('wordDelimiter', val)

    def setMinCount(self, val):
        return self._add_param('minCount', val)

    def setRandomWindow(self, val):
        return self._add_param('randomWindow', val)

    def setWindow(self, val):
        return self._add_param('window', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)

