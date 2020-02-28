#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..base import StreamOperator, BaseSinkStreamOp, BaseModelStreamOp


class AftSurvivalRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.AftSurvivalRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AftSurvivalRegPredictStreamOp, self).__init__(*args, **kwargs)
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


class AlsPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.recommendation.AlsPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AlsPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setUserCol(self, val):
        return self._add_param('userCol', val)

    def setItemCol(self, val):
        return self._add_param('itemCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class AsStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.AsStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(AsStreamOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BinarizerStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.BinarizerStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BinarizerStreamOp, self).__init__(*args, **kwargs)
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


class BisectingKMeansPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.clustering.BisectingKMeansPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BisectingKMeansPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class BucketizerStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.BucketizerStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(BucketizerStreamOp, self).__init__(*args, **kwargs)
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


class CsvSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.CsvSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(CsvSinkStreamOp, self).__init__(*args, **kwargs)
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


class CsvSourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.CsvSourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(CsvSourceStreamOp, self).__init__(*args, **kwargs)
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


class DCTStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.DCTStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DCTStreamOp, self).__init__(*args, **kwargs)
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


class DecisionTreePredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.DecisionTreePredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreePredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DecisionTreeRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.DecisionTreeRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DecisionTreeRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocCountVectorizerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.DocCountVectorizerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocCountVectorizerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class DocHashCountVectorizerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.DocHashCountVectorizerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(DocHashCountVectorizerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class EvalBinaryClassStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.evaluation.EvalBinaryClassStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(EvalBinaryClassStreamOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setTimeInterval(self, val):
        return self._add_param('timeInterval', val)

    def setPositiveLabelValueString(self, val):
        return self._add_param('positiveLabelValueString', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class EvalMultiClassStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.evaluation.EvalMultiClassStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(EvalMultiClassStreamOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setTimeInterval(self, val):
        return self._add_param('timeInterval', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class FeatureHasherStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.FeatureHasherStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FeatureHasherStreamOp, self).__init__(*args, **kwargs)
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


class FilterStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.FilterStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(FilterStreamOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _FtrlPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.onlinelearning.FtrlPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_FtrlPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _FtrlTrainStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.onlinelearning.FtrlTrainStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_FtrlTrainStreamOp, self).__init__(*args, **kwargs)
        pass

    def setLabelCol(self, val):
        return self._add_param('labelCol', val)

    def setVectorSize(self, val):
        return self._add_param('vectorSize', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setFeatureCols(self, val):
        return self._add_param('featureCols', val)

    def setWithIntercept(self, val):
        return self._add_param('withIntercept', val)

    def setTimeInterval(self, val):
        return self._add_param('timeInterval', val)

    def setL1(self, val):
        return self._add_param('l1', val)

    def setL2(self, val):
        return self._add_param('l2', val)

    def setAlpha(self, val):
        return self._add_param('alpha', val)

    def setBeta(self, val):
        return self._add_param('beta', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.GbdtPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GbdtRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.GbdtRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GbdtRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GlmPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.GlmPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GlmPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setLinkPredResultCol(self, val):
        return self._add_param('linkPredResultCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class GmmPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.clustering.GmmPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(GmmPredictStreamOp, self).__init__(*args, **kwargs)
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


class ImputerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.ImputerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(ImputerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class IndexToStringPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.IndexToStringPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IndexToStringPredictStreamOp, self).__init__(*args, **kwargs)
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


class IsotonicRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.IsotonicRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(IsotonicRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class JdbcRetractSinkStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.JdbcRetractSinkStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(JdbcRetractSinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class JsonValueStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.JsonValueStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(JsonValueStreamOp, self).__init__(*args, **kwargs)
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


class KMeansPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.clustering.KMeansPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(KMeansPredictStreamOp, self).__init__(*args, **kwargs)
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


class Kafka010SinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.Kafka010SinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Kafka010SinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setDataFormat(self, val):
        return self._add_param('dataFormat', val)

    def setFieldDelimiter(self, val):
        return self._add_param('fieldDelimiter', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class Kafka010SourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.Kafka010SourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Kafka010SourceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setGroupId(self, val):
        return self._add_param('groupId', val)

    def setStartupMode(self, val):
        return self._add_param('startupMode', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setTopicPattern(self, val):
        return self._add_param('topicPattern', val)

    def setStartTime(self, val):
        return self._add_param('startTime', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class Kafka011SinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.Kafka011SinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Kafka011SinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setDataFormat(self, val):
        return self._add_param('dataFormat', val)

    def setFieldDelimiter(self, val):
        return self._add_param('fieldDelimiter', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class Kafka011SourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.Kafka011SourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Kafka011SourceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setGroupId(self, val):
        return self._add_param('groupId', val)

    def setStartupMode(self, val):
        return self._add_param('startupMode', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setTopicPattern(self, val):
        return self._add_param('topicPattern', val)

    def setStartTime(self, val):
        return self._add_param('startTime', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class KafkaSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.KafkaSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(KafkaSinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setDataFormat(self, val):
        return self._add_param('dataFormat', val)

    def setFieldDelimiter(self, val):
        return self._add_param('fieldDelimiter', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class KafkaSourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.KafkaSourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(KafkaSourceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setBootstrapServers(self, val):
        return self._add_param('bootstrapServers', val)

    def setGroupId(self, val):
        return self._add_param('groupId', val)

    def setStartupMode(self, val):
        return self._add_param('startupMode', val)

    def setTopic(self, val):
        return self._add_param('topic', val)

    def setTopicPattern(self, val):
        return self._add_param('topicPattern', val)

    def setStartTime(self, val):
        return self._add_param('startTime', val)

    def setProperties(self, val):
        return self._add_param('properties', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LassoRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.LassoRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LassoRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LibSvmSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.LibSvmSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LibSvmSinkStreamOp, self).__init__(*args, **kwargs)
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


class LibSvmSourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.LibSvmSourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LibSvmSourceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.LinearRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class LinearSvmPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.LinearSvmPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LinearSvmPredictStreamOp, self).__init__(*args, **kwargs)
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


class LogisticRegressionPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.LogisticRegressionPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(LogisticRegressionPredictStreamOp, self).__init__(*args, **kwargs)
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


class MaxAbsScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.MaxAbsScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MaxAbsScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MinMaxScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.MinMaxScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MinMaxScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMin(self, val):
        return self._add_param('min', val)

    def setMax(self, val):
        return self._add_param('max', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class MultiStringIndexerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.MultiStringIndexerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultiStringIndexerPredictStreamOp, self).__init__(*args, **kwargs)
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


class MultilayerPerceptronPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.MultilayerPerceptronPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MultilayerPerceptronPredictStreamOp, self).__init__(*args, **kwargs)
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


class MySqlSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.MySqlSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MySqlSinkStreamOp, self).__init__(*args, **kwargs)
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


class MySqlSourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.MySqlSourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(MySqlSourceStreamOp, self).__init__(*args, **kwargs)
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


class NGramStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.NGramStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NGramStreamOp, self).__init__(*args, **kwargs)
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


class NaiveBayesTextPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.NaiveBayesTextPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(NaiveBayesTextPredictStreamOp, self).__init__(*args, **kwargs)
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


class OneHotPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.OneHotPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(OneHotPredictStreamOp, self).__init__(*args, **kwargs)
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

