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
class KNN(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaEstimator):
    """


    Args:

        featuresCol (str): The name of the features column (default: features)
        k (int): number of matches to return (default: 5)
        leafSize (int): max size of the leaves of the tree (default: 50)
        outputCol (str): The name of the output column (default: [self.uid]_output)
        valuesCol (str): column holding values for each feature (key) that will be returned when queried (default: values)
    """

    @keyword_only
    def __init__(self, featuresCol="features", k=5, leafSize=50, outputCol=None, valuesCol="values"):
        super(KNN, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.nn.KNN")
        self.featuresCol = Param(self, "featuresCol", "featuresCol: The name of the features column (default: features)")
        self._setDefault(featuresCol="features")
        self.k = Param(self, "k", "k: number of matches to return (default: 5)")
        self._setDefault(k=5)
        self.leafSize = Param(self, "leafSize", "leafSize: max size of the leaves of the tree (default: 50)")
        self._setDefault(leafSize=50)
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column (default: [self.uid]_output)")
        self._setDefault(outputCol=self.uid + "_output")
        self.valuesCol = Param(self, "valuesCol", "valuesCol: column holding values for each feature (key) that will be returned when queried (default: values)")
        self._setDefault(valuesCol="values")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, featuresCol="features", k=5, leafSize=50, outputCol=None, valuesCol="values"):
        """
        Set the (keyword only) parameters

        Args:

            featuresCol (str): The name of the features column (default: features)
            k (int): number of matches to return (default: 5)
            leafSize (int): max size of the leaves of the tree (default: 50)
            outputCol (str): The name of the output column (default: [self.uid]_output)
            valuesCol (str): column holding values for each feature (key) that will be returned when queried (default: values)
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setFeaturesCol(self, value):
        """

        Args:

            featuresCol (str): The name of the features column (default: features)

        """
        self._set(featuresCol=value)
        return self


    def getFeaturesCol(self):
        """

        Returns:

            str: The name of the features column (default: features)
        """
        return self.getOrDefault(self.featuresCol)


    def setK(self, value):
        """

        Args:

            k (int): number of matches to return (default: 5)

        """
        self._set(k=value)
        return self


    def getK(self):
        """

        Returns:

            int: number of matches to return (default: 5)
        """
        return self.getOrDefault(self.k)


    def setLeafSize(self, value):
        """

        Args:

            leafSize (int): max size of the leaves of the tree (default: 50)

        """
        self._set(leafSize=value)
        return self


    def getLeafSize(self):
        """

        Returns:

            int: max size of the leaves of the tree (default: 50)
        """
        return self.getOrDefault(self.leafSize)


    def setOutputCol(self, value):
        """

        Args:

            outputCol (str): The name of the output column (default: [self.uid]_output)

        """
        self._set(outputCol=value)
        return self


    def getOutputCol(self):
        """

        Returns:

            str: The name of the output column (default: [self.uid]_output)
        """
        return self.getOrDefault(self.outputCol)


    def setValuesCol(self, value):
        """

        Args:

            valuesCol (str): column holding values for each feature (key) that will be returned when queried (default: values)

        """
        self._set(valuesCol=value)
        return self


    def getValuesCol(self):
        """

        Returns:

            str: column holding values for each feature (key) that will be returned when queried (default: values)
        """
        return self.getOrDefault(self.valuesCol)





    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.nn.KNN"

    @staticmethod
    def _from_java(java_stage):
        module_name=KNN.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".KNN"
        return from_java(java_stage, module_name)

    def _create_model(self, java_model):
        return KNNModel(java_model)


class KNNModel(ComplexParamsMixin, JavaModel, JavaMLWritable, JavaMLReadable):
    """
    Model fitted by :class:`KNN`.

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
        return "com.microsoft.ml.spark.nn.KNNModel"

    @staticmethod
    def _from_java(java_stage):
        module_name=KNNModel.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".KNNModel"
        return from_java(java_stage, module_name)

