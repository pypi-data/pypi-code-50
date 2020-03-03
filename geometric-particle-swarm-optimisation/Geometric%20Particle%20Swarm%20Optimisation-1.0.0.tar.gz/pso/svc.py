import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def svmm(X,y,k=0):
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
    clf=svm.SVC(kernel='linear').fit(X_train,y_train)
    scores=cross_val_score(clf,X,y,cv=10)
    
    if(k==1):
        return(np.mean(scores)*100)
    
    return np.mean(scores)


def svm_fitness(X,y,l,b=1,k=0):
    
    if(sum(l)==0):
        return 99999

    features=list(*(np.where(l==1)))
    X=X[:,features]
    
    if(k==1):
        return(svmm(X,y,k))

    accuracy=svmm(X,y,k)
    fitness=(0.75*(100/accuracy))+(0.25*(sum(l)))
    #fitness=(accuracy/(b*sum(l)))-(100/(b*(len(l))))
    
    return fitness
