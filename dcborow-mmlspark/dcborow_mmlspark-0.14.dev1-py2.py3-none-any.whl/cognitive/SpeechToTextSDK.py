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
class SpeechToTextSDK(ComplexParamsMixin, JavaMLReadable, JavaMLWritable, JavaTransformer):
    """


    Args:

        audioData (object): The data sent to the service must be a .wav files
        format (object): Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))
        language (object): Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))
        outputCol (str): The name of the output column
        profanity (object): Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))
        subscriptionKey (object): the API key to use
        url (str): Url of the service
    """

    @keyword_only
    def __init__(self, audioData=None, format=None, language=None, outputCol=None, profanity=None, subscriptionKey=None, url=None):
        super(SpeechToTextSDK, self).__init__()
        self._java_obj = self._new_java_obj("com.microsoft.ml.spark.cognitive.SpeechToTextSDK")
        self.audioData = Param(self, "audioData", "audioData:  The data sent to the service must be a .wav files")
        self.format = Param(self, "format", "format:  Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))")
        self.language = Param(self, "language", "language:  Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))")
        self.outputCol = Param(self, "outputCol", "outputCol: The name of the output column")
        self.profanity = Param(self, "profanity", "profanity:  Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))")
        self.subscriptionKey = Param(self, "subscriptionKey", "subscriptionKey: the API key to use")
        self.url = Param(self, "url", "url: Url of the service")
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        self.setParams(**kwargs)

    @keyword_only
    def setParams(self, audioData=None, format=None, language=None, outputCol=None, profanity=None, subscriptionKey=None, url=None):
        """
        Set the (keyword only) parameters

        Args:

            audioData (object): The data sent to the service must be a .wav files
            format (object): Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))
            language (object): Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))
            outputCol (str): The name of the output column
            profanity (object): Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))
            subscriptionKey (object): the API key to use
            url (str): Url of the service
        """
        if hasattr(self, "_input_kwargs"):
            kwargs = self._input_kwargs
        else:
            kwargs = self.__init__._input_kwargs
        return self._set(**kwargs)

    def setAudioData(self, value):
        """

        Args:

            audioData (object): The data sent to the service must be a .wav files

        """
        self._java_obj = self._java_obj.setAudioData(value)
        return self


    def setAudioDataCol(self, value):
        """

        Args:

            audioData (object): The data sent to the service must be a .wav files

        """
        self._java_obj = self._java_obj.setAudioDataCol(value)
        return self




    def getAudioData(self):
        """

        Returns:

            object: The data sent to the service must be a .wav files
        """
        return self._cache.get("audioData", None)


    def setFormat(self, value):
        """

        Args:

            format (object): Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))

        """
        self._java_obj = self._java_obj.setFormat(value)
        return self


    def setFormatCol(self, value):
        """

        Args:

            format (object): Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))

        """
        self._java_obj = self._java_obj.setFormatCol(value)
        return self




    def getFormat(self):
        """

        Returns:

            object: Specifies the result format. Accepted values are simple and detailed. Default is simple.      (default: ServiceParamData(None,Some(Simple)))
        """
        return self._cache.get("format", None)


    def setLanguage(self, value):
        """

        Args:

            language (object): Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))

        """
        self._java_obj = self._java_obj.setLanguage(value)
        return self


    def setLanguageCol(self, value):
        """

        Args:

            language (object): Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))

        """
        self._java_obj = self._java_obj.setLanguageCol(value)
        return self




    def getLanguage(self):
        """

        Returns:

            object: Identifies the spoken language that is being recognized.      (default: ServiceParamData(None,Some(en-us)))
        """
        return self._cache.get("language", None)


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


    def setProfanity(self, value):
        """

        Args:

            profanity (object): Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))

        """
        self._java_obj = self._java_obj.setProfanity(value)
        return self


    def setProfanityCol(self, value):
        """

        Args:

            profanity (object): Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))

        """
        self._java_obj = self._java_obj.setProfanityCol(value)
        return self




    def getProfanity(self):
        """

        Returns:

            object: Specifies how to handle profanity in recognition results. Accepted values are masked, which replaces profanity with asterisks, removed, which remove all profanity from the result, or raw, which includes the profanity in the result. The default setting is masked.      (default: ServiceParamData(None,Some(Masked)))
        """
        return self._cache.get("profanity", None)


    def setSubscriptionKey(self, value):
        """

        Args:

            subscriptionKey (object): the API key to use

        """
        self._java_obj = self._java_obj.setSubscriptionKey(value)
        return self


    def setSubscriptionKeyCol(self, value):
        """

        Args:

            subscriptionKey (object): the API key to use

        """
        self._java_obj = self._java_obj.setSubscriptionKeyCol(value)
        return self




    def getSubscriptionKey(self):
        """

        Returns:

            object: the API key to use
        """
        return self._cache.get("subscriptionKey", None)


    def setUrl(self, value):
        """

        Args:

            url (str): Url of the service

        """
        self._set(url=value)
        return self


    def getUrl(self):
        """

        Returns:

            str: Url of the service
        """
        return self.getOrDefault(self.url)




    def setLocation(self, value):
        self._java_obj = self._java_obj.setLocation(value)
        return self


    @classmethod
    def read(cls):
        """ Returns an MLReader instance for this class. """
        return JavaMMLReader(cls)

    @staticmethod
    def getJavaPackage():
        """ Returns package name String. """
        return "com.microsoft.ml.spark.cognitive.SpeechToTextSDK"

    @staticmethod
    def _from_java(java_stage):
        module_name=SpeechToTextSDK.__module__
        module_name=module_name.rsplit(".", 1)[0] + ".SpeechToTextSDK"
        return from_java(java_stage, module_name)
