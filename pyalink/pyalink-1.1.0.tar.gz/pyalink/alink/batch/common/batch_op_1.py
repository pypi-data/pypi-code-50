#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..base import BatchOperator, BaseSinkBatchOp


class AftSurvivalRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.AftSurvivalRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AftSurvivalRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setQuantileProbabilities(self, val):
        return self._add_param('quantileProbabilities', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AftSurvivalRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.AftSurvivalRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AftSurvivalRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setCensorCol(self, val):
        return self._add_param('censorCol', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setL1(self, val):
        return self._add_param('l1', val)

    def setL2(self, val):
        return self._add_param('l2', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AlsPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.recommendation.AlsPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AlsPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setUserCol(self, val):
        return self._add_param('userCol', val)

    def setItemCol(self, val):
        return self._add_param('itemCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AlsTopKPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.recommendation.AlsTopKPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AlsTopKPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setUserCol(self, val):
        return self._add_param('userCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setTopK(self, val):
        return self._add_param('topK', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AlsTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.recommendation.AlsTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AlsTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setUserCol(self, val):
        return self._add_param('userCol', val)

    def setItemCol(self, val):
        return self._add_param('itemCol', val)

    def setRateCol(self, val):
        return self._add_param('rateCol', val)

    def setRank(self, val):
        return self._add_param('rank', val)

    def setLambda(self, val):
        return self._add_param('lambda', val)

    def setNonnegative(self, val):
        return self._add_param('nonnegative', val)

    def setImplicitPrefs(self, val):
        return self._add_param('implicitPrefs', val)

    def setAlpha(self, val):
        return self._add_param('alpha', val)

    def setNumBlocks(self, val):
        return self._add_param('numBlocks', val)

    def setNumIter(self, val):
        return self._add_param('numIter', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AppendIdBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.AppendIdBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AppendIdBatchOp, self).__init__(*args, **kwargs)
        pass

    def setAppendType(self, val):
        return self._add_param('appendType', val)

    def setIdCol(self, val):
        return self._add_param('idCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class ApproxVectorSimilarityJoinLSHBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.similarity.ApproxVectorSimilarityJoinLSHBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(ApproxVectorSimilarityJoinLSHBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLeftCol(self, val):
        return self._add_param('leftCol', val)

    def setRightCol(self, val):
        return self._add_param('rightCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setLeftIdCol(self, val):
        return self._add_param('leftIdCol', val)

    def setRightIdCol(self, val):
        return self._add_param('rightIdCol', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setDistanceType(self, val):
        return self._add_param('distanceType', val)

    def setNumHashTables(self, val):
        return self._add_param('numHashTables', val)

    def setNumProjectionsPerTable(self, val):
        return self._add_param('numProjectionsPerTable', val)

    def setSeed(self, val):
        return self._add_param('seed', val)

    def setProjectionWidth(self, val):
        return self._add_param('projectionWidth', val)

    def setDistanceThreshold(self, val):
        return self._add_param('distanceThreshold', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class ApproxVectorSimilarityTopNLSHBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.similarity.ApproxVectorSimilarityTopNLSHBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(ApproxVectorSimilarityTopNLSHBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLeftCol(self, val):
        return self._add_param('leftCol', val)

    def setRightCol(self, val):
        return self._add_param('rightCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setLeftIdCol(self, val):
        return self._add_param('leftIdCol', val)

    def setRightIdCol(self, val):
        return self._add_param('rightIdCol', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setDistanceType(self, val):
        return self._add_param('distanceType', val)

    def setNumHashTables(self, val):
        return self._add_param('numHashTables', val)

    def setNumProjectionsPerTable(self, val):
        return self._add_param('numProjectionsPerTable', val)

    def setSeed(self, val):
        return self._add_param('seed', val)

    def setProjectionWidth(self, val):
        return self._add_param('projectionWidth', val)

    def setTopN(self, val):
        return self._add_param('topN', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AsBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.AsBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AsBatchOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BinarizerBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.BinarizerBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BinarizerBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setThreshold(self, val):
        return self._add_param('threshold', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BisectingKMeansPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.BisectingKMeansPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BisectingKMeansPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BisectingKMeansTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.BisectingKMeansTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BisectingKMeansTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMinDivisibleClusterSize(self, val):
        return self._add_param('minDivisibleClusterSize', val)

    def setK(self, val):
        return self._add_param('k', val)

    def setDistanceType(self, val):
        return self._add_param('distanceType', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BucketizerBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.BucketizerBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BucketizerBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setCutsArray(self, val):
        return self._add_param('cutsArray', val)

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

    def setLeftOpen(self, val):
        return self._add_param('leftOpen', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _ChiSqSelectorBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.ChiSqSelectorBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_ChiSqSelectorBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setSelectorType(self, val):
        return self._add_param('selectorType', val)

    def setNumTopFeatures(self, val):
        return self._add_param('numTopFeatures', val)

    def setPercentile(self, val):
        return self._add_param('percentile', val)

    def setFpr(self, val):
        return self._add_param('fpr', val)

    def setFdr(self, val):
        return self._add_param('fdr', val)

    def setFwe(self, val):
        return self._add_param('fwe', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _ChiSquareTestBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.statistics.ChiSquareTestBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_ChiSquareTestBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _CorrelationBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.statistics.CorrelationBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_CorrelationBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMethod(self, val):
        return self._add_param('method', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class CsvSinkBatchOp(BaseSinkBatchOp):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sink.CsvSinkBatchOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(CsvSinkBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setFieldDelimiter(self, val):
        return self._add_param('fieldDelimiter', val)

    def setRowDelimiter(self, val):
        return self._add_param('rowDelimiter', val)

    def setQuoteChar(self, val):
        return self._add_param('quoteChar', val)

    def setOverwriteSink(self, val):
        return self._add_param('overwriteSink', val)

    def setNumFiles(self, val):
        return self._add_param('numFiles', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class CsvSourceBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.source.CsvSourceBatchOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(CsvSourceBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setSchemaStr(self, val):
        return self._add_param('schemaStr', val)

    def setFieldDelimiter(self, val):
        return self._add_param('fieldDelimiter', val)

    def setQuoteChar(self, val):
        return self._add_param('quoteChar', val)

    def setSkipBlankLine(self, val):
        return self._add_param('skipBlankLine', val)

    def setRowDelimiter(self, val):
        return self._add_param('rowDelimiter', val)

    def setIgnoreFirstLine(self, val):
        return self._add_param('ignoreFirstLine', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DCTBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.DCTBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DCTBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setInverse(self, val):
        return self._add_param('inverse', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DecisionTreePredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.DecisionTreePredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreePredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DecisionTreeRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.DecisionTreeRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreeRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DecisionTreeRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.DecisionTreeRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreeRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setCategoricalCols(self, val):
        return self._add_param('categoricalCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxLeaves(self, val):
        return self._add_param('maxLeaves', val)

    def setMinSampleRatioPerChild(self, val):
        return self._add_param('minSampleRatioPerChild', val)

    def setMinInfoGain(self, val):
        return self._add_param('minInfoGain', val)

    def setMaxDepth(self, val):
        return self._add_param('maxDepth', val)

    def setMinSamplesPerLeaf(self, val):
        return self._add_param('minSamplesPerLeaf', val)

    def setCreateTreeMode(self, val):
        return self._add_param('createTreeMode', val)

    def setMaxBins(self, val):
        return self._add_param('maxBins', val)

    def setMaxMemoryInMB(self, val):
        return self._add_param('maxMemoryInMB', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DecisionTreeTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.DecisionTreeTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreeTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setCategoricalCols(self, val):
        return self._add_param('categoricalCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxLeaves(self, val):
        return self._add_param('maxLeaves', val)

    def setMinSampleRatioPerChild(self, val):
        return self._add_param('minSampleRatioPerChild', val)

    def setMinInfoGain(self, val):
        return self._add_param('minInfoGain', val)

    def setMaxDepth(self, val):
        return self._add_param('maxDepth', val)

    def setMinSamplesPerLeaf(self, val):
        return self._add_param('minSamplesPerLeaf', val)

    def setCreateTreeMode(self, val):
        return self._add_param('createTreeMode', val)

    def setMaxBins(self, val):
        return self._add_param('maxBins', val)

    def setMaxMemoryInMB(self, val):
        return self._add_param('maxMemoryInMB', val)

    def setTreeType(self, val):
        return self._add_param('treeType', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DistinctBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.DistinctBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DistinctBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocCountVectorizerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.DocCountVectorizerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocCountVectorizerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocCountVectorizerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.DocCountVectorizerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocCountVectorizerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setMaxDF(self, val):
        return self._add_param('maxDF', val)

    def setMinDF(self, val):
        return self._add_param('minDF', val)

    def setFeatureType(self, val):
        return self._add_param('featureType', val)

    def setVocabSize(self, val):
        return self._add_param('vocabSize', val)

    def setMinTF(self, val):
        return self._add_param('minTF', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocHashCountVectorizerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.DocHashCountVectorizerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocHashCountVectorizerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocHashCountVectorizerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.nlp.DocHashCountVectorizerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocHashCountVectorizerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setNumFeatures(self, val):
        return self._add_param('numFeatures', val)

    def setMinDF(self, val):
        return self._add_param('minDF', val)

    def setFeatureType(self, val):
        return self._add_param('featureType', val)

    def setMinTF(self, val):
        return self._add_param('minTF', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _EvalBinaryClassBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.evaluation.EvalBinaryClassBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_EvalBinaryClassBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setPositiveLabelValueString(self, val):
        return self._add_param('positiveLabelValueString', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _EvalClusterBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.evaluation.EvalClusterBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_EvalClusterBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setDistanceType(self, val):
        return self._add_param('distanceType', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _EvalMultiClassBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.evaluation.EvalMultiClassBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_EvalMultiClassBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _EvalRegressionBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.evaluation.EvalRegressionBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_EvalRegressionBatchOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FeatureHasherBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.feature.FeatureHasherBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FeatureHasherBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setNumFeatures(self, val):
        return self._add_param('numFeatures', val)

    def setCategoricalCols(self, val):
        return self._add_param('categoricalCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FilterBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.FilterBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FilterBatchOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FirstNBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.FirstNBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FirstNBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSize(self, val):
        return self._add_param('size', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FpGrowthBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.associationrule.FpGrowthBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FpGrowthBatchOp, self).__init__(*args, **kwargs)
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

    def setMaxConsequentLength(self, val):
        return self._add_param('maxConsequentLength', val)

    def setMinLift(self, val):
        return self._add_param('minLift', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FullOuterJoinBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.FullOuterJoinBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FullOuterJoinBatchOp, self).__init__(*args, **kwargs)
        pass

    def setJoinPredicate(self, val):
        return self._add_param('joinPredicate', val)

    def setSelectClause(self, val):
        return self._add_param('selectClause', val)

    def setType(self, val):
        return self._add_param('type', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.GbdtPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtRegPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.GbdtRegPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtRegPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtRegTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.GbdtRegTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtRegTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setAlgoType(self, val):
        return self._add_param('algoType', val)

    def setLearningRate(self, val):
        return self._add_param('learningRate', val)

    def setMinSumHessianPerLeaf(self, val):
        return self._add_param('minSumHessianPerLeaf', val)

    def setCategoricalCols(self, val):
        return self._add_param('categoricalCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxLeaves(self, val):
        return self._add_param('maxLeaves', val)

    def setMinSampleRatioPerChild(self, val):
        return self._add_param('minSampleRatioPerChild', val)

    def setMinInfoGain(self, val):
        return self._add_param('minInfoGain', val)

    def setNumTrees(self, val):
        return self._add_param('numTrees', val)

    def setMinSamplesPerLeaf(self, val):
        return self._add_param('minSamplesPerLeaf', val)

    def setMaxDepth(self, val):
        return self._add_param('maxDepth', val)

    def setSubsamplingRatio(self, val):
        return self._add_param('subsamplingRatio', val)

    def setFeatureSubsamplingRatio(self, val):
        return self._add_param('featureSubsamplingRatio', val)

    def setGroupCol(self, val):
        return self._add_param('groupCol', val)

    def setMaxBins(self, val):
        return self._add_param('maxBins', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.classification.GbdtTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setAlgoType(self, val):
        return self._add_param('algoType', val)

    def setLearningRate(self, val):
        return self._add_param('learningRate', val)

    def setMinSumHessianPerLeaf(self, val):
        return self._add_param('minSumHessianPerLeaf', val)

    def setCategoricalCols(self, val):
        return self._add_param('categoricalCols', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxLeaves(self, val):
        return self._add_param('maxLeaves', val)

    def setMinSampleRatioPerChild(self, val):
        return self._add_param('minSampleRatioPerChild', val)

    def setMinInfoGain(self, val):
        return self._add_param('minInfoGain', val)

    def setNumTrees(self, val):
        return self._add_param('numTrees', val)

    def setMinSamplesPerLeaf(self, val):
        return self._add_param('minSamplesPerLeaf', val)

    def setMaxDepth(self, val):
        return self._add_param('maxDepth', val)

    def setSubsamplingRatio(self, val):
        return self._add_param('subsamplingRatio', val)

    def setFeatureSubsamplingRatio(self, val):
        return self._add_param('featureSubsamplingRatio', val)

    def setGroupCol(self, val):
        return self._add_param('groupCol', val)

    def setMaxBins(self, val):
        return self._add_param('maxBins', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GlmEvaluationBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.GlmEvaluationBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GlmEvaluationBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setFamily(self, val):
        return self._add_param('family', val)

    def setVariancePower(self, val):
        return self._add_param('variancePower', val)

    def setLink(self, val):
        return self._add_param('link', val)

    def setLinkPower(self, val):
        return self._add_param('linkPower', val)

    def setOffsetCol(self, val):
        return self._add_param('offsetCol', val)

    def setFitIntercept(self, val):
        return self._add_param('fitIntercept', val)

    def setRegParam(self, val):
        return self._add_param('regParam', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GlmPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.GlmPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GlmPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setLinkPredResultCol(self, val):
        return self._add_param('linkPredResultCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GlmTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.regression.GlmTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GlmTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setFamily(self, val):
        return self._add_param('family', val)

    def setVariancePower(self, val):
        return self._add_param('variancePower', val)

    def setLink(self, val):
        return self._add_param('link', val)

    def setLinkPower(self, val):
        return self._add_param('linkPower', val)

    def setOffsetCol(self, val):
        return self._add_param('offsetCol', val)

    def setFitIntercept(self, val):
        return self._add_param('fitIntercept', val)

    def setRegParam(self, val):
        return self._add_param('regParam', val)

    def setEpsilon(self, val):
        return self._add_param('epsilon', val)

    def setWeightCol(self, val):
        return self._add_param('weightCol', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GmmPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.GmmPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GmmPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GmmTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.clustering.GmmTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GmmTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setTol(self, val):
        return self._add_param('tol', val)

    def setK(self, val):
        return self._add_param('k', val)

    def setMaxIter(self, val):
        return self._add_param('maxIter', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GroupByBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.sql.GroupByBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GroupByBatchOp, self).__init__(*args, **kwargs)
        pass

    def setGroupByPredicate(self, val):
        return self._add_param('groupByPredicate', val)

    def setSelectClause(self, val):
        return self._add_param('selectClause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class ImputerPredictBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.ImputerPredictBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(ImputerPredictBatchOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class ImputerTrainBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.operator.batch.dataproc.ImputerTrainBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(ImputerTrainBatchOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setStrategy(self, val):
        return self._add_param('strategy', val)

    def setFillValue(self, val):
        return self._add_param('fillValue', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class InMemorySourceBatchOp(BatchOperator):
    CLS_NAME = 'com.alibaba.alink.executor.python.util.InMemorySourceBatchOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(InMemorySourceBatchOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)

