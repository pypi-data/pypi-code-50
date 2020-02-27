import os
import numpy as np
import shutil
from utils import *
from config import *

from pickle import load,dump
from sklearn import svm
from sklearn.preprocessing import normalize
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc,accuracy_score

import warnings

warnings.filterwarnings("ignore")



def features():

    file_paths = []
    labels = []
    features = []
    rootdir = "./data"
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.wav'):
                fp = subdir+'/'+file
                features.append(extract_features(fp))
                file_paths.append(fp)
                labels.append(fp.split('/')[-2])

    # convert feature into array
    feat = np.array(features)

    return file_paths,labels,feat


def create_df():

    file_paths,labels,feat = features()

    # creating the dataframe
    df = pd.DataFrame({"filepath":file_paths,"label":labels})
    df["mfccs"] = feat[:,0]
    df["chroma"] = feat[:,1]
    df["mel"] = feat[:,2]
    df["contrast"] = feat[:,3]
    df["tonnetz"] = feat[:,4]
    df["Final_label"] = feat[:,5]

    return df


def get_features():

    df = create_df()
    # stacking all samples to create a matrix
    mfccs = np.vstack((df["mfccs"].values))
    chroma = np.vstack((df["chroma"].values))
    mel = np.vstack((df["mel"].values))
    tonnetz = np.vstack((df["tonnetz"].values))
    contrast = np.vstack((df["contrast"].values))

    labels = df["label"].values

    print("Features extracted successfully...")


    # normalizing the features
    mfccs = normalize(mfccs,axis=0)
    chroma = normalize(chroma,axis=0)
    mel = normalize(mel,axis=0)
    contrast = normalize(contrast,axis=0)
    tonnetz = normalize(tonnetz,axis=0)

    return mfccs,chroma,mel,contrast,tonnetz,labels


def train(samples):

    print("Making data set ready for classifier...")
    
    voiceSamples(samples)

    mfccs,contrast,mel,chroma,tonnetz,labels = get_features()

    svm_x = np.hstack((mfccs,contrast,mel,chroma,tonnetz))
    svm_y = labels

    # printing the necessary information
    print("*"*60)
    print(mfccs.shape)
    print(chroma.shape)
    print(mel.shape)
    print(tonnetz.shape)
    print(contrast.shape)
    print(svm_x.shape)
    print(svm_y.shape)


    ############## Training ###########
    X_train, X_test, y_train, y_test = train_test_split(svm_x,svm_y, test_size=0.25, random_state=42)

    for i in c:
        clf = svm.SVC(C = i,kernel='rbf', class_weight='balanced',probability=True)
        clf.fit(X_train,y_train)
        print("*"*60)
        print("For C = ",i)
        print("Accuracy for train ",accuracy_score(y_train,clf.predict(X_train)))
        print("Accuracy for test ",accuracy_score(y_test,clf.predict(X_test)))



    print(clf.classes_)
    c_ = eval(input("Please provide value of c for final..\n"))
    clf = svm.SVC(C = c_,kernel='rbf',class_weight="balanced",probability=True)
    clf.fit(X_train,y_train)

    # saving the model
    os.mkdir("model")
    with open("./model/clf.pkl","wb") as f:
        dump(clf,f)
        print("Model saved successfully...")



if __name__ == "__main__":

    samples = eval(input("Please provide a list of voice samples\n"))
    assert type(samples) == list , "please provide list of paths"

    try:

        train(samples)
        
        if os.path.exists("./data/"):
            shutil.rmtree("./data/")    
    except Exception as e:

        if os.path.exists("./data/"):
            shutil.rmtree("./data/")    

        print(e)
        print("Cleaning done...")

         

