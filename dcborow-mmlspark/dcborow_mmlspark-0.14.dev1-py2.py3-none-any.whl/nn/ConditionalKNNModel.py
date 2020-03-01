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
class ConditionalKNNModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        ballTree (object): the ballTree model used for perfoming queries
        conditionerCol (str): column holding identifiers for features that will be returned when queried
        featuresCol (str): The name of the features column
        k (int): number of matches to return
        labelCol (str): The name of the label column
        leafSize (int): max size of the leaves of the tree
        outputCol (str): The name of the output column
        valuesCol (str): column holding values for each feature (key) that will be returned when queried
    """

    @keyword_only
    def __init__(self, ballTree=None, conditionerCol=None, featuresCol=None, k=None, labelCol=None, leafSize=None, outputCol=None, valuesCol=None):
        super(ConditionalKNNModel, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.nn.ConditionalKNNModel")
        self.ballTree = Param(self, "ballTree", "ballTree: the ballTree model used for perfoming queries")
        self.conditionerCol = Param(self, "conditionerCol", "conditionerCol: column holding identifiers for features that will be returned when queried")
        self.featuresCol = Param(self, "featuresCol", "featuresCol: The name of the features column")
        self.k = Param(self, "k", "k: number of matches to return")
        self.labelCol = Param(self, "labelCol", "labelCol: The name of the label column")
        self.leafSize = Param(self, "leafSize", "leafSize: max size of the leaves of the tree")
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column")
        self.valuesCol = Param(self, "valuesCol", "valuesCol: column holding values for each feature (key) that will be returned when queried")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, ballTree=None, conditionerCol=None, featuresCol=None, k=None, labelCol=None, leafSize=None, outputCol=None, valuesCol=None):
        """
        Set the (keyword only) parameters

        Args:

            ballTree (object): the ballTree model used for perfoming queries
            conditionerCol (str): column holding identifiers for features that will be returned when queried
            featuresCol (str): The name of the features column
            k (int): number of matches to return
            labelCol (str): The name of the label column
            leafSize (int): max size of the leaves of the tree
            outputCol (str): The name of the output column
            valuesCol (str): column holding values for each feature (key) that will be returned when queried
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setBallTree(self, value):
        """

        Args:

            ballTree (object): the ballTree model used for perfoming queries

        """
        self._set(ballTree=value)
        return self


    def getBallTree(self):
        """

        Returns:

            object: the ballTree model used for perfoming queries
        """
        return self.getOrDefault(self.ballTree)


    def setConditionerCol(self, value):
        """

        Args:

            conditionerCol (str): column holding identifiers for features that will be returned when queried

        """
        self._set(conditionerCol=value)
        return self


    def getConditionerCol(self):
        """

        Returns:

            str: column holding identifiers for features that will be returned when queried
        """
        return self.getOrDefault(self.conditionerCol)


    def setFeaturesCol(self, value):
        """

        Args:

            featuresCol (str): The name of the features column

        """
        self._set(featuresCol=value)
        return self


    def getFeaturesCol(self):
        """

        Returns:

            str: The name of the features column
        """
        return self.getOrDefault(self.featuresCol)


    def setK(self, value):
        """

        Args:

            k (int): number of matches to return

        """
        self._set(k=value)
        return self


    def getK(self):
        """

        Returns:

            int: number of matches to return
        """
        return self.getOrDefault(self.k)


    def setLabelCol(self, value):
        """

        Args:

            labelCol (str): The name of the label column

        """
        self._set(labelCol=value)
        return self


    def getLabelCol(self):
        """

        Returns:

            str: The name of the label column
        """
        return self.getOrDefault(self.labelCol)


    def setLeafSize(self, value):
        """

        Args:

            leafSize (int): max size of the leaves of the tree

        """
        self._set(leafSize=value)
        return self


    def getLeafSize(self):
        """

        Returns:

            int: max size of the leaves of the tree
        """
        return self.getOrDefault(self.leafSize)


    def setOutputCol(self, value):
        """

        Args:

            outputCol (str): The name of the output column

        """
        self._set(outputCol=value)
        return self


    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column
        """
        return self.getOrDefault(self.outputCol)


    def setValuesCol(self, value):
        """

        Args:

            valuesCol (str): column holding values for each feature (key) that will be returned when queried

        """
        self._set(valuesCol=value)
        return self


    def getValuesCol(self):
        """

        Returns:

            str: column holding values for each feature (key) that will be returned when queried
        """
        return self.getOrDefault(self.valuesCol)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.nn.ConditionalKNNModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=ConditionalKNNModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".ConditionalKNNModel"
        return from_java(java_stage, module_name)
