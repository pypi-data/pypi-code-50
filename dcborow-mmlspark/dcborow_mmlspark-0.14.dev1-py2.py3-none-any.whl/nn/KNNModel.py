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
class KNNModel(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        ballTree (object): the ballTree model used for perfoming queries
        featuresCol (str): The name of the features column
        k (int): number of matches to return
        leafSize (int): max size of the leaves of the tree
        outputCol (str): The name of the output column
        valuesCol (str): column holding values for each feature (key) that will be returned when queried
    """

    @keyword_only
    def __init__(self, ballTree=None, featuresCol=None, k=None, leafSize=None, outputCol=None, valuesCol=None):
        super(KNNModel, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.nn.KNNModel")
        self.ballTree = Param(self, "ballTree", "ballTree: the ballTree model used for perfoming queries")
        self.featuresCol = Param(self, "featuresCol", "featuresCol: The name of the features column")
        self.k = Param(self, "k", "k: number of matches to return")
        self.leafSize = Param(self, "leafSize", "leafSize: max size of the leaves of the tree")
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column")
        self.valuesCol = Param(self, "valuesCol", "valuesCol: column holding values for each feature (key) that will be returned when queried")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, ballTree=None, featuresCol=None, k=None, leafSize=None, outputCol=None, valuesCol=None):
        """
        Set the (keyword only) parameters

        Args:

            ballTree (object): the ballTree model used for perfoming queries
            featuresCol (str): The name of the features column
            k (int): number of matches to return
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
        return "com.microsoft.ml.spark.nn.KNNModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=KNNModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".KNNModel"
        return from_java(java_stage, module_name)
