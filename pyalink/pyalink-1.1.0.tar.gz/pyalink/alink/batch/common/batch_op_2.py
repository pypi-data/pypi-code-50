#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..base import BatchOperator, BaseSinkBatchOp


class IndexToStringPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.IndexToStringPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IndexToStringPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setModelName(self, val):
        return self._add_param('modelName', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class IntersectAllBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.IntersectAllBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IntersectAllBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class IntersectBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.IntersectBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IntersectBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class IsotonicRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.IsotonicRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IsotonicRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class IsotonicRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.IsotonicRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IsotonicRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setFeatureCol(self, val):
        return self._add_param('featureCol', val)

    def setIsotonic(self, val):
        return self._add_param('isotonic', val)

    def setFeatureIndex(self, val):
        return self._add_param('featureIndex', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class JoinBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.JoinBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(JoinBatchOp, self).__init__(*args, **kwargs)
        pass

    def setJoinPredicate(self, val):
        return self._add_param('joinPredicate', val)

    def setSelectClause(self, val):
        return self._add_param('selectClause', val)

    def setType(self, val):
        return self._add_param('type', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class JsonValueBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.JsonValueBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(JsonValueBatchOp, self).__init__(*args, **kwargs)
        pass

    def setJsonPath(self, val):
        return self._add_param('jsonPath', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setSkipFailed(self, val):
        return self._add_param('skipFailed', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class KMeansPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.KMeansPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(KMeansPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDistanceCol(self, val):
        return self._add_param('predictionDistanceCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class KMeansTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.KMeansTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(KMeansTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setDistanceType(self, val):
        return self._add_param('distanceType', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setInitMode(self, val):
        return self._add_param('initMode', val)

    def setInitSteps(self, val):
        return self._add_param('initSteps', val)

    def setK(self, val):
        return self._add_param('k', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LassoRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.LassoRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LassoRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LassoRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.LassoRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LassoRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setLambda(self, val):
        return self._add_param('lambda', val)

    def setOptimMethod(self, val):
        return self._add_param('optimMethod', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setStandardization(self, val):
        return self._add_param('standardization', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LdaPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.LdaPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LdaPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LdaTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.LdaTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LdaTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setTopicNum(self, val):
        return self._add_param('topicNum', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setAlpha(self, val):
        return self._add_param('alpha', val)

    def setBeta(self, val):
        return self._add_param('beta', val)

    def setMethod(self, val):
        return self._add_param('method', val)

    def setOnlineLearningOffset(self, val):
        return self._add_param('onlineLearningOffset', val)

    def setLearningDecay(self, val):
        return self._add_param('learningDecay', val)

    def setSubsamplingRate(self, val):
        return self._add_param('subsamplingRate', val)

    def setOptimizeDocConcentration(self, val):
        return self._add_param('optimizeDocConcentration', val)

    def setNumIter(self, val):
        return self._add_param('numIter', val)

    def setVocabSize(self, val):
        return self._add_param('vocabSize', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LeftOuterJoinBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.LeftOuterJoinBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LeftOuterJoinBatchOp, self).__init__(*args, **kwargs)
        pass

    def setJoinPredicate(self, val):
        return self._add_param('joinPredicate', val)

    def setSelectClause(self, val):
        return self._add_param('selectClause', val)

    def setType(self, val):
        return self._add_param('type', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LibSvmSinkBatchOp(BaseSinkBatchOp):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sink.LibSvmSinkBatchOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LibSvmSinkBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setOverwriteSink(self, val):
        return self._add_param('overwriteSink', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LibSvmSourceBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.source.LibSvmSourceBatchOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LibSvmSourceBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.LinearRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.LinearRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setOptimMethod(self, val):
        return self._add_param('optimMethod', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setStandardization(self, val):
        return self._add_param('standardization', val)

    def setL1(self, val):
        return self._add_param('l1', val)

    def setL2(self, val):
        return self._add_param('l2', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearSvmPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.LinearSvmPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearSvmPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearSvmTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.LinearSvmTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearSvmTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setC(self, val):
        return self._add_param('C', val)

    def setOptimMethod(self, val):
        return self._add_param('optimMethod', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setStandardization(self, val):
        return self._add_param('standardization', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LogisticRegressionPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.LogisticRegressionPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LogisticRegressionPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LogisticRegressionTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.LogisticRegressionTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LogisticRegressionTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setOptimMethod(self, val):
        return self._add_param('optimMethod', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setStandardization(self, val):
        return self._add_param('standardization', val)

    def setL1(self, val):
        return self._add_param('l1', val)

    def setL2(self, val):
        return self._add_param('l2', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MaxAbsScalerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MaxAbsScalerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MaxAbsScalerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MaxAbsScalerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MaxAbsScalerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MaxAbsScalerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MinMaxScalerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MinMaxScalerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MinMaxScalerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MinMaxScalerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MinMaxScalerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MinMaxScalerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMin(self, val):
        return self._add_param('min', val)

    def setMax(self, val):
        return self._add_param('max', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MinusAllBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.MinusAllBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MinusAllBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MinusBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.MinusBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MinusBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MultiStringIndexerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MultiStringIndexerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultiStringIndexerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MultiStringIndexerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.MultiStringIndexerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultiStringIndexerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setStringOrderType(self, val):
        return self._add_param('stringOrderType', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MultilayerPerceptronPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.MultilayerPerceptronPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultilayerPerceptronPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MultilayerPerceptronTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.MultilayerPerceptronTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultilayerPerceptronTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLayers(self, val):
        return self._add_param('layers', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setBlockSize(self, val):
        return self._add_param('blockSize', val)

    def setInitialWeights(self, val):
        return self._add_param('initialWeights', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setL1(self, val):
        return self._add_param('l1', val)

    def setL2(self, val):
        return self._add_param('l2', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MySqlSinkBatchOp(BaseSinkBatchOp):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sink.MySqlSinkBatchOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MySqlSinkBatchOp, self).__init__(*args, **kwargs)
        pass

    def setDbName(self, val):
        return self._add_param('dbName', val)

    def setIp(self, val):
        return self._add_param('ip', val)

    def setPassword(self, val):
        return self._add_param('password', val)

    def setPort(self, val):
        return self._add_param('port', val)

    def setUsername(self, val):
        return self._add_param('username', val)

    def setOutputTableName(self, val):
        return self._add_param('outputTableName', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MySqlSourceBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.source.MySqlSourceBatchOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MySqlSourceBatchOp, self).__init__(*args, **kwargs)
        pass

    def setDbName(self, val):
        return self._add_param('dbName', val)

    def setIp(self, val):
        return self._add_param('ip', val)

    def setPassword(self, val):
        return self._add_param('password', val)

    def setPort(self, val):
        return self._add_param('port', val)

    def setUsername(self, val):
        return self._add_param('username', val)

    def setInputTableName(self, val):
        return self._add_param('inputTableName', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class NGramBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.NGramBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NGramBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setN(self, val):
        return self._add_param('n', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class NaiveBayesTextPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.NaiveBayesTextPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NaiveBayesTextPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class NaiveBayesTextTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.NaiveBayesTextTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NaiveBayesTextTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setModelType(self, val):
        return self._add_param('modelType', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setSmoothing(self, val):
        return self._add_param('smoothing', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class NumericalTypeCastBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.NumericalTypeCastBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NumericalTypeCastBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setTargetType(self, val):
        return self._add_param('targetType', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class OneHotPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.OneHotPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(OneHotPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setEncode(self, val):
        return self._add_param('encode', val)

    def setDropLast(self, val):
        return self._add_param('dropLast', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class OneHotTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.OneHotTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(OneHotTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setDiscreteThresholds(self, val):
        return self._add_param('discreteThresholds', val)

    def setDiscreteThresholdsArray(self, val):
        return self._add_param('discreteThresholdsArray', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class OrderByBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.OrderByBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(OrderByBatchOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setFetch(self, val):
        return self._add_param('fetch', val)

    def setLimit(self, val):
        return self._add_param('limit', val)

    def setOffset(self, val):
        return self._add_param('offset', val)

    def setOrder(self, val):
        return self._add_param('order', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class PcaPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.PcaPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PcaPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setTransformType(self, val):
        return self._add_param('transformType', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class PcaTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.PcaTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PcaTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setK(self, val):
        return self._add_param('k', val)

    def setCalculationType(self, val):
        return self._add_param('calculationType', val)

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setWithMean(self, val):
        return self._add_param('withMean', val)

    def setWithStd(self, val):
        return self._add_param('withStd', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class PrefixSpanBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.associationrule.PrefixSpanBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PrefixSpanBatchOp, self).__init__(*args, **kwargs)
        pass

    def setItemsCol(self, val):
        return self._add_param('itemsCol', val)

    def setMinSupportCount(self, val):
        return self._add_param('minSupportCount', val)

    def setMinSupportPercent(self, val):
        return self._add_param('minSupportPercent', val)

    def setMinConfidence(self, val):
        return self._add_param('minConfidence', val)

    def setMaxPatternLength(self, val):
        return self._add_param('maxPatternLength', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class PrintBatchOp(BaseSinkBatchOp):
    CLS_NAME = 'com.alibaba.alink.operator.batch.utils.PrintBatchOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PrintBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _PyBinaryScalarFunctionBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.executor.udf.python.PyBinaryScalarFunctionBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_PyBinaryScalarFunctionBatchOp, self).__init__(*args, **kwargs)
        pass

    def setClassObject(self, val):
        return self._add_param('classObject', val)

    def setClassObjectType(self, val):
        return self._add_param('classObjectType', val)

    def setResultType(self, val):
        return self._add_param('resultType', val)

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _PyBinaryTableFunctionBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.executor.udf.python.PyBinaryTableFunctionBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_PyBinaryTableFunctionBatchOp, self).__init__(*args, **kwargs)
        pass

    def setClassObject(self, val):
        return self._add_param('classObject', val)

    def setClassObjectType(self, val):
        return self._add_param('classObjectType', val)

    def setResultTypes(self, val):
        return self._add_param('resultTypes', val)

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class QuantileDiscretizerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.QuantileDiscretizerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(QuantileDiscretizerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setEncode(self, val):
        return self._add_param('encode', val)

    def setDropLast(self, val):
        return self._add_param('dropLast', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class QuantileDiscretizerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.QuantileDiscretizerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(QuantileDiscretizerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setNumBuckets(self, val):
        return self._add_param('numBuckets', val)

    def setNumBucketsArray(self, val):
        return self._add_param('numBucketsArray', val)

    def setLeftOpen(self, val):
        return self._add_param('leftOpen', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class RandomForestPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.RandomForestPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(RandomForestPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)

