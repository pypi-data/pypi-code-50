#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..base import StreamOperator, BaseSinkStreamOp, BaseModelStreamOp


class PcaPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.PcaPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PcaPredictStreamOp, self).__init__(*args, **kwargs)
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


class PrintStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.utils.PrintStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(PrintStreamOp, self).__init__(*args, **kwargs)
        pass

    def setRefreshInterval(self, val):
        return self._add_param('refreshInterval', val)

    def setMaxLimit(self, val):
        return self._add_param('maxLimit', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class _PyBinaryScalarFunctionStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.executor.udf.python.PyBinaryScalarFunctionStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_PyBinaryScalarFunctionStreamOp, self).__init__(*args, **kwargs)
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


class _PyBinaryTableFunctionStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.executor.udf.python.PyBinaryTableFunctionStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(_PyBinaryTableFunctionStreamOp, self).__init__(*args, **kwargs)
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


class QuantileDiscretizerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.feature.QuantileDiscretizerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(QuantileDiscretizerPredictStreamOp, self).__init__(*args, **kwargs)
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


class RandomForestPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.RandomForestPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(RandomForestPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class RandomForestRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.RandomForestRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(RandomForestRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setPredictionDetailCol(self, val):
        return self._add_param('predictionDetailCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class RegexTokenizerStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.RegexTokenizerStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(RegexTokenizerStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setPattern(self, val):
        return self._add_param('pattern', val)

    def setGaps(self, val):
        return self._add_param('gaps', val)

    def setMinTokenLength(self, val):
        return self._add_param('minTokenLength', val)

    def setToLowerCase(self, val):
        return self._add_param('toLowerCase', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class RidgeRegPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.regression.RidgeRegPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(RidgeRegPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setPredictionCol(self, val):
        return self._add_param('predictionCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setVectorCol(self, val):
        return self._add_param('vectorCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SampleStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.SampleStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SampleStreamOp, self).__init__(*args, **kwargs)
        pass

    def setRatio(self, val):
        return self._add_param('ratio', val)

    def setWithReplacement(self, val):
        return self._add_param('withReplacement', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SegmentStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.SegmentStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SegmentStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setUserDefinedDict(self, val):
        return self._add_param('userDefinedDict', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SelectStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.SelectStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SelectStreamOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SideOutputStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.utils.SideOutputStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SideOutputStreamOp, self).__init__(*args, **kwargs)
        pass

    def setIndex(self, val):
        return self._add_param('index', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SocketSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.SocketSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SocketSinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setHost(self, val):
        return self._add_param('host', val)

    def setPort(self, val):
        return self._add_param('port', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SoftmaxPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.classification.SoftmaxPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SoftmaxPredictStreamOp, self).__init__(*args, **kwargs)
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


class SplitStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.SplitStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SplitStreamOp, self).__init__(*args, **kwargs)
        pass

    def setFraction(self, val):
        return self._add_param('fraction', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class SqlCmdStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.SqlCmdStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(SqlCmdStreamOp, self).__init__(*args, **kwargs)
        pass

    def setCommand(self, val):
        return self._add_param('command', val)

    def setAlias(self, val):
        return self._add_param('alias', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class StandardScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.StandardScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(StandardScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class StopWordsRemoverStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.StopWordsRemoverStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(StopWordsRemoverStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setCaseSensitive(self, val):
        return self._add_param('caseSensitive', val)

    def setStopWords(self, val):
        return self._add_param('stopWords', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class StringIndexerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.StringIndexerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(StringIndexerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class TextSinkStreamOp(BaseSinkStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sink.TextSinkStreamOp'
    OP_TYPE = 'SINK'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(TextSinkStreamOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setOverwriteSink(self, val):
        return self._add_param('overwriteSink', val)

    def setNumFiles(self, val):
        return self._add_param('numFiles', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class TextSourceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.source.TextSourceStreamOp'
    OP_TYPE = 'SOURCE'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(TextSourceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setFilePath(self, val):
        return self._add_param('filePath', val)

    def setIgnoreFirstLine(self, val):
        return self._add_param('ignoreFirstLine', val)

    def setTextCol(self, val):
        return self._add_param('textCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class TokenizerStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.TokenizerStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(TokenizerStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class UnionAllStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.UnionAllStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(UnionAllStreamOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorAssemblerStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorAssemblerStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorAssemblerStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorElementwiseProductStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorElementwiseProductStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorElementwiseProductStreamOp, self).__init__(*args, **kwargs)
        pass

    def setScalingVector(self, val):
        return self._add_param('scalingVector', val)

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorImputerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorImputerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorImputerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorInteractionStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorInteractionStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorInteractionStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorMaxAbsScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorMaxAbsScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorMaxAbsScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCols(self, val):
        return self._add_param('selectedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorMinMaxScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorMinMaxScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorMinMaxScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setMin(self, val):
        return self._add_param('min', val)

    def setMax(self, val):
        return self._add_param('max', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorNormalizeStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorNormalizeStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorNormalizeStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setP(self, val):
        return self._add_param('p', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorPolynomialExpandStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorPolynomialExpandStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorPolynomialExpandStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setDegree(self, val):
        return self._add_param('degree', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorSerializeStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.utils.VectorSerializeStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorSerializeStreamOp, self).__init__(*args, **kwargs)
        pass

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorSizeHintStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorSizeHintStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorSizeHintStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setSize(self, val):
        return self._add_param('size', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setHandleInvalid(self, val):
        return self._add_param('handleInvalid', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorSliceStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorSliceStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorSliceStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCol(self, val):
        return self._add_param('outputCol', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setIndices(self, val):
        return self._add_param('indices', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorStandardScalerPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorStandardScalerPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorStandardScalerPredictStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setWithMean(self, val):
        return self._add_param('withMean', val)

    def setWithStd(self, val):
        return self._add_param('withStd', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class VectorToColumnsStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.dataproc.vector.VectorToColumnsStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(VectorToColumnsStreamOp, self).__init__(*args, **kwargs)
        pass

    def setSelectedCol(self, val):
        return self._add_param('selectedCol', val)

    def setOutputCols(self, val):
        return self._add_param('outputCols', val)

    def setReservedCols(self, val):
        return self._add_param('reservedCols', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class WhereStreamOp(StreamOperator):
    CLS_NAME = 'com.alibaba.alink.operator.stream.sql.WhereStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(WhereStreamOp, self).__init__(*args, **kwargs)
        pass

    def setClause(self, val):
        return self._add_param('clause', val)

    def setMLEnvironmentId(self, val):
        return self._add_param('MLEnvironmentId', val)


class Word2VecPredictStreamOp(BaseModelStreamOp):
    CLS_NAME = 'com.alibaba.alink.operator.stream.nlp.Word2VecPredictStreamOp'
    OP_TYPE = 'FUNCTION'

    def __init__(self, *args, **kwargs):
        kwargs['CLS_NAME'] = self.CLS_NAME
        kwargs['OP_TYPE'] = self.OP_TYPE
        super(Word2VecPredictStreamOp, self).__init__(*args, **kwargs)
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

