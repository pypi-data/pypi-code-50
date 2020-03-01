# Copyright (C) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in project root for information.


import sys
if sys.version >= '3':
    basestring = str

from pyspark.ml.param.shared import *
from pyspark import keyword_only
from pyspark.ml.util import JavaMLReadable, JavaMLWritable
from mmlspark.core.serialize.java_params_patch import *
from pyspark.ml.wrapper import JavaTransformer, JavaEstimator, JavaModel
from pyspark.ml.common import inherit_doc
from mmlspark.core.schema.Utils import *

@inherit_doc
class _IsolationForest(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """


    Args:

        bootstrap (bool): If true, draw sample for each tree with replacement. If false, do not sample with replacement. (default: false)
        contamination (double): The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter. (default: 0.0)
        contaminationError (double): The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value. (default: 0.0)
        featuresCol (str): The feature vector. (default: features)
        maxFeatures (double): The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 1.0)
        maxSamples (double): The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 256.0)
        numEstimators (int): The number of trees in the ensemble. (default: 100)
        predictionCol (str): The predicted label. (default: predictedLabel)
        randomSeed (long): The seed used for the random number generator. (default: 1)
        scoreCol (str): The outlier score. (default: outlierScore)
    """

    @keyword_only
    def __init__(self, bootstrap=False, contamination=0.0, contaminationError=0.0, featuresCol="features", maxFeatures=1.0, maxSamples=256.0, numEstimators=100, predictionCol="predictedLabel", randomSeed=1, scoreCol="outlierScore"):
        super(_IsolationForest, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.isolationforest.IsolationForest")
        self.bootstrap = Param(self, "bootstrap", "bootstrap: If true, draw sample for each tree with replacement. If false, do not sample with replacement. (default: false)")
        self._setDefault(bootstrap=False)
        self.contamination = Param(self, "contamination", "contamination: The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter. (default: 0.0)")
        self._setDefault(contamination=0.0)
        self.contaminationError = Param(self, "contaminationError", "contaminationError: The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value. (default: 0.0)")
        self._setDefault(contaminationError=0.0)
        self.featuresCol = Param(self, "featuresCol", "featuresCol: The feature vector. (default: features)")
        self._setDefault(featuresCol="features")
        self.maxFeatures = Param(self, "maxFeatures", "maxFeatures: The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 1.0)")
        self._setDefault(maxFeatures=1.0)
        self.maxSamples = Param(self, "maxSamples", "maxSamples: The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 256.0)")
        self._setDefault(maxSamples=256.0)
        self.numEstimators = Param(self, "numEstimators", "numEstimators: The number of trees in the ensemble. (default: 100)")
        self._setDefault(numEstimators=100)
        self.predictionCol = Param(self, "predictionCol", "predictionCol: The predicted label. (default: predictedLabel)")
        self._setDefault(predictionCol="predictedLabel")
        self.randomSeed = Param(self, "randomSeed", "randomSeed: The seed used for the random number generator. (default: 1)")
        self._setDefault(randomSeed=1)
        self.scoreCol = Param(self, "scoreCol", "scoreCol: The outlier score. (default: outlierScore)")
        self._setDefault(scoreCol="outlierScore")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, bootstrap=False, contamination=0.0, contaminationError=0.0, featuresCol="features", maxFeatures=1.0, maxSamples=256.0, numEstimators=100, predictionCol="predictedLabel", randomSeed=1, scoreCol="outlierScore"):
        """
        Set the (keyword only) parameters

        Args:

            bootstrap (bool): If true, draw sample for each tree with replacement. If false, do not sample with replacement. (default: false)
            contamination (double): The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter. (default: 0.0)
            contaminationError (double): The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value. (default: 0.0)
            featuresCol (str): The feature vector. (default: features)
            maxFeatures (double): The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 1.0)
            maxSamples (double): The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 256.0)
            numEstimators (int): The number of trees in the ensemble. (default: 100)
            predictionCol (str): The predicted label. (default: predictedLabel)
            randomSeed (long): The seed used for the random number generator. (default: 1)
            scoreCol (str): The outlier score. (default: outlierScore)
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setBootstrap(self, value):
        """

        Args:

            bootstrap (bool): If true, draw sample for each tree with replacement. If false, do not sample with replacement. (default: false)

        """
        self._set(bootstrap=value)
        return self


    def getBootstrap(self):
        """

        Returns:

            bool: If true, draw sample for each tree with replacement. If false, do not sample with replacement. (default: false)
        """
        return self.getOrDefault(self.bootstrap)


    def setContamination(self, value):
        """

        Args:

            contamination (double): The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter. (default: 0.0)

        """
        self._set(contamination=value)
        return self


    def getContamination(self):
        """

        Returns:

            double: The fraction of outliers in the training data set. If this is set to 0.0, it speeds up the training and all predicted labels will be false. The model and outlier scores are otherwise unaffected by this parameter. (default: 0.0)
        """
        return self.getOrDefault(self.contamination)


    def setContaminationError(self, value):
        """

        Args:

            contaminationError (double): The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value. (default: 0.0)

        """
        self._set(contaminationError=value)
        return self


    def getContaminationError(self):
        """

        Returns:

            double: The error allowed when calculating the threshold required to achieve the specified contamination fraction. The default is 0.0, which forces an exact calculation of the threshold. The exact calculation is slow and can fail for large datasets. If there are issues with the exact calculation, a good choice for this parameter is often 1% of the specified contamination value. (default: 0.0)
        """
        return self.getOrDefault(self.contaminationError)


    def setFeaturesCol(self, value):
        """

        Args:

            featuresCol (str): The feature vector. (default: features)

        """
        self._set(featuresCol=value)
        return self


    def getFeaturesCol(self):
        """

        Returns:

            str: The feature vector. (default: features)
        """
        return self.getOrDefault(self.featuresCol)


    def setMaxFeatures(self, value):
        """

        Args:

            maxFeatures (double): The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 1.0)

        """
        self._set(maxFeatures=value)
        return self


    def getMaxFeatures(self):
        """

        Returns:

            double: The number of features used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 1.0)
        """
        return self.getOrDefault(self.maxFeatures)


    def setMaxSamples(self, value):
        """

        Args:

            maxSamples (double): The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 256.0)

        """
        self._set(maxSamples=value)
        return self


    def getMaxSamples(self):
        """

        Returns:

            double: The number of samples used to train each tree. If this value is between 0.0 and 1.0, then it is treated as a fraction. If it is >1.0, then it is treated as a count. (default: 256.0)
        """
        return self.getOrDefault(self.maxSamples)


    def setNumEstimators(self, value):
        """

        Args:

            numEstimators (int): The number of trees in the ensemble. (default: 100)

        """
        self._set(numEstimators=value)
        return self


    def getNumEstimators(self):
        """

        Returns:

            int: The number of trees in the ensemble. (default: 100)
        """
        return self.getOrDefault(self.numEstimators)


    def setPredictionCol(self, value):
        """

        Args:

            predictionCol (str): The predicted label. (default: predictedLabel)

        """
        self._set(predictionCol=value)
        return self


    def getPredictionCol(self):
        """

        Returns:

            str: The predicted label. (default: predictedLabel)
        """
        return self.getOrDefault(self.predictionCol)


    def setRandomSeed(self, value):
        """

        Args:

            randomSeed (long): The seed used for the random number generator. (default: 1)

        """
        self._set(randomSeed=value)
        return self


    def getRandomSeed(self):
        """

        Returns:

            long: The seed used for the random number generator. (default: 1)
        """
        return self.getOrDefault(self.randomSeed)


    def setScoreCol(self, value):
        """

        Args:

            scoreCol (str): The outlier score. (default: outlierScore)

        """
        self._set(scoreCol=value)
        return self


    def getScoreCol(self):
        """

        Returns:

            str: The outlier score. (default: outlierScore)
        """
        return self.getOrDefault(self.scoreCol)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.isolationforest.IsolationForest"

    @staticmethod
    def _from_java(java_stage):
        module_name=_IsolationForest.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".IsolationForest"
        return from_java(java_stage, module_name)

    def _create_model(self, java_model):
        return _IsolationForestModel(java_model)


class _IsolationForestModel(ComplexParamsMixin, JavaModel, JavaMLWritable, JavaMLReadable):
    """
    Model fitted by :class:`_IsolationForest`.

    This class is left empty on purpose.
    All necessary methods are exposed through inheritance.
    """

    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.isolationforest.IsolationForestModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=_IsolationForestModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".IsolationForestModel"
        return from_java(java_stage, module_name)

