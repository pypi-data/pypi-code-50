import os
import shutil
import numpy as np
from utils import *
from pickle import load,dump
from sklearn.preprocessing import normalize


class VoiceClassify():

    """ The class for classifying voice samples. """

    def __init__(self):

        # loading the model
        with open("./model/clf.pkl","rb") as f:
            self.clf = load(f)
        
    @staticmethod
    def _process(fp):

        """ 
        This method is called internally to process the auido file.
        :type fp: file_path of sample file
        :param fp: file_path

        :raises: Raises an excetion if something went wrong.

        :rtype: Returns the numpy array fo features extracted from voice.
        """
        fname = fp.split("/")[-1].split(".")[0]
        print(fname)

        try:

            if not os.path.exists("./temp"):
                os.mkdir("temp") 

            # convert audio file to .wav format
            os.system("ffmpeg -i {} -b:a 320000 ./temp/{}.wav".format(fp,fname))
            # trim the silence present in the file
            os.system("sox ./temp/{}.wav ./temp/{}_sl.wav silence -l 1 0.1 1% -1 2.0 1%".format(fname,fname))

            print("Audio preprocessed..")

            path = os.path.realpath("./temp/{}.wav".format(fname))
            mfccs, chroma, mel, contrast, tonnetz,_ = extract_features(path)

            # remmooving the unnecessary files
            shutil.rmtree("./temp/")
            return np.hstack((normalize(mfccs),normalize(contrast),normalize(mel),normalize(chroma),normalize(tonnetz)))

        except Exception as e:

            # remmooving the unnecessary files
            shutil.rmtree("./temp/")
            print("Cleaning done...")
            print(e)
            
    def classes_(self):

        """ 
        Returns the classes of the model
        :type self:
        :param self:
    
        :raises: None
    
        :rtype: classes_ object
        """    
        return self.clf.classes_

    def predict(self,fp):

        """ Description
        :type self: 
        :param self:

        :type fp: absolute path of sample audio file
        :param fp: file path to be classified

        :raises: NA

        :rtype: predicted class and their probabilities and classes
        """
        dp = self._process(fp)

        prediction,prob,classes = self.clf.predict(dp),self.clf.predict_proba(dp),self.clf.classes_

        return prediction,prob,classes



    