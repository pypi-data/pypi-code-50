# VERSION 0.0.1

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoLarsCV
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import SGDRegressor

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.linear_model import BayesianRidge
from xgboost import XGBClassifier
from xgboost import XGBRegressor
from lightgbm import LGBMClassifier
from lightgbm import LGBMRegressor
from catboost import CatBoostClassifier
from catboost import CatBoostRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import VotingRegressor

from keras import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.layers import Dropout
from keras.optimizers import Adam
from keras import metrics

from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer
from sklearn.metrics import mean_squared_error

class Ghalat_Machine_Learning(object):
    
    def __init__(self,n_estimators=300):
        """
        n_estimators ; number of estimators in some models.
        """
        self.df = pd.DataFrame([])
        self.n_estimator = n_estimators
        self.classifiers = [
            'LogisticRegressionCV','LogisticRegression','SVC','DecisionTreeClassifier','KNeighborsClassifier',
            'SGDClassifier','RandomForestClassifier','AdaBoostClassifier','ExtraTreesClassifier',
            'XGBClassifier','LGBMClassifier','CatBoostClassifier','GradientBoostingClassifier','NaiveBayesGaussian'
        ]
        self.classifier_models = [
            LogisticRegressionCV(max_iter=1000),LogisticRegression(max_iter=1000),SVC(),
            DecisionTreeClassifier(),KNeighborsClassifier(),
            SGDClassifier(),RandomForestClassifier(n_estimators=n_estimators),
            AdaBoostClassifier(DecisionTreeClassifier(),n_estimators=n_estimators),
            ExtraTreesClassifier(n_estimators=n_estimators),XGBClassifier(n_estimators=n_estimators),
            LGBMClassifier(n_estimators=n_estimators),
            CatBoostClassifier(n_estimators=n_estimators,verbose=0),GradientBoostingClassifier(n_estimators=n_estimators),
            GaussianNB()
        ]
        
        self.regressors = [
            'LassoLarsCV','LinearRegression','SVR','DecisionTreeRegressor','KNeighborsRegressor','SGDRegressor',
            'RandomForestRegressor','AdaBoostRegressor','ExtraTreesRegressor','XGBRegressor',
            'LGBMRegressor','CatBoostRegressor','GradientBoostingRegressor','NaiveBayesianRidge'
        ]
        
        self.regressors_models = [
            LassoLarsCV(max_iter=1000),
            LinearRegression(),SVR(),DecisionTreeRegressor(),KNeighborsRegressor(),SGDRegressor(),
            RandomForestRegressor(n_estimators=n_estimators),
            AdaBoostRegressor(DecisionTreeRegressor(),n_estimators=n_estimators),
            ExtraTreesRegressor(n_estimators=n_estimators),XGBRegressor(n_estimators=n_estimators),
            LGBMRegressor(n_estimators=n_estimators),CatBoostRegressor(verbose=0,n_estimators=n_estimators),
            GradientBoostingRegressor(n_estimators=n_estimators),BayesianRidge()
        ]
        self.models_stack = []
        
        print("Welcome to Ghalat Machine Learning!\n\nAll models are set to train\n \
        Have a tea and leave everything on us ;-)")

    
    def GMLClassifier(self,X,y,metric = accuracy_score, test_Size = 0.3,folds = 5, shuffle = True, scaler = 'SS',models=None,
                     neural_net="No",epochs=10,verbose=True):
        """
        Necessary arguments - X and y

        Optional: 
        metric ; if you want to test some custom metric 
        test_Size ; size of validation split (default 70% training and 30% validation)
        folds ; for cross validation
        Scaler ;
        for Scaler:
            'SS' for StandardScalar
            'MM' for MinMaxScalar
            'log' for Log scalar
        models ; list of models you want to compete with our models
        neural_net ; either "No" or "Yes"
        if neural_net == "Yes":
            epochs
            verbose
            
        returns:
            best model with parameters (not trained on data)
        """
        best_model = None
        best_acc = 0
        if scaler == 'SS':
            X = StandardScaler().fit_transform(X)
        elif scaler == 'MM':
            X = MinMaxScaler().fit_transform(X)
        elif scaler == 'log':
            X = np.log(X+1)
            
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_Size,shuffle=shuffle)

        for name,model in zip(self.classifiers,self.classifier_models):
            try:
                tmodel = model
                model.fit(X_train,y_train)
                y_hat = model.predict(X_test)
                score = metric(y_test,y_hat)
                cv_score = np.mean(cross_val_score(model,X,y,cv=folds))
                if cv_score > best_acc:
                    best_acc = cv_score
                    best_model = tmodel
                print('Model ',name,' got validation accuracy of ',score)
                self.df = self.df.append([[name,score,cv_score]])
            except:
                print("Error occured while training ",name)
        if not (models == None):
            for model in models:
                try:
                    tmodel = model
                    model.fit(X_train,y_train)
                    y_hat = model.predict(X_test)
                    score = metric(y_test,y_hat)
                    cv_score = np.mean(cross_val_score(model,X,y,cv=folds))
                    if cv_score > best_acc:
                        best_acc = cv_score
                        best_model = tmodel
                    print('Model ',type(model).__name__,' got validation accuracy of ',score)
                    self.df = self.df.append([[type(model).__name__,score,cv_score]])
                except:
                    print("Error occured while training ",type(model).__name__)
                
        if neural_net == "Yes" or neural_net == "YES" or neural_net == "yes":
            loss_func = ""
            y_train = to_categorical(y_train)
            output_features = len(np.unique(y))
            if len(np.unique(y)) == 2:
                loss_func = 'binary_crossentropy'
            else:
                loss_func = 'categorical_crossentropy'
            print('\n','*'*40,'\nTraining Neural Network\n','*'*40)
            model = Sequential()
            model.add(Dense(256, input_dim=X_train.shape[1], activation="relu" ))
            model.add(Dropout(0.50))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.50))
            model.add(Dense(64,activation="relu"))
            model.add(Dense(output_features,activation='sigmoid'))
            model.compile(optimizer='adam',loss=loss_func,metrics=['accuracy'])
            tmodel = model
            model.fit(X_train,y_train,epochs=epochs,verbose=verbose,validation_data=(X_test,to_categorical(y_test)))
            y_hat = model.predict(X_test)
            y_hat = np.argmax(y_hat,axis=1)
            score = metric(y_test,y_hat)
            if score > best_acc:
                best_acc = score
                best_model = tmodel
            print('Neural Network got validation accuracy of ',score)
            self.df = self.df.append([['Neural Network',score,score]])
            print(model.summary())
            
        self.df.columns = 'Model','Val_Accuracy','CV on '+str(folds)+' folds'
        self.df.sort_values(self.df.columns[2],inplace=True,ascending=False)
        print(pd.DataFrame(self.df))
        
        print('\n\n','*'*40,'\nSuggested Models for Stacking\n','*'*40,'\n',self.df['Model'].iloc[0:5])
        
        print('*'*40,'\n','PLEASE NOTE: these results are calculated using ',metric)
        
        return best_model
        
    def GMLRegressor(self,X,y,metric = mean_squared_error, test_Size = 0.3,folds=5, shuffle = True, scaler = 'SS',models=None,
                     neural_net="No",epochs=10,verbose=True):
        """
        Necessary arguments - X and y

        Optional: 
        metric ; if you want to test some custom metric 
        test_Size ; size of validation split (default 70% training and 30% validation)
        Scaler ;
        for Scaler:
            'SS' for StandardScalar
            'MM' for MinMaxScalar
            'log' for Log scalar
        models ; list of models you want to compete with our models
        neural_net ; either "No" or "Yes"
        if neural_net == "Yes":
            epochs
            verbose
            
        returns:
            best model with parameters (not trained on data)
        """
        best_model = None
        best_acc = 1000
        if scaler == 'SS':
            X = StandardScaler().fit_transform(X)
        elif scaler == 'MM':
            X = MinMaxScaler().fit_transform(X)
        elif scaler == 'log':
            X = np.log(X+1)
            
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_Size,shuffle=shuffle)

        for name,model in zip(self.regressors,self.regressors_models):
            try:
                tmodel = model
                model.fit(X_train,y_train)
                y_hat = model.predict(X_test)
                score = metric(y_test,y_hat)
                if score < best_acc:
                    best_acc = score
                    best_model = tmodel
                print('Model ',name,' got validation loss of ',score)
                self.df = self.df.append([[name,score]])
            except:
                print("Error occured while training ",name)
        
        if not (models==None):
            for model in models:
                try:
                    tmodel = model
                    model.fit(X_train,y_train)
                    y_hat = model.predict(X_test)
                    score = metric(y_test,y_hat)
                    if score < best_acc:
                        best_acc = score
                        best_model = tmodel
                    print('Model ',type(model).__name__,' got validation accuracy of ',score)
                    self.df = self.df.append([[type(model).__name__,score]])
                except:
                    print("Error occured while training ",type(model).__name__)
        
        if neural_net == "Yes" or neural_net == "YES" or neural_net == "yes":
            loss_func = ""           
            print('\n','*'*40,'\nTraining Neural Network\n','*'*40)
            model = Sequential()
            model.add(Dense(256, input_dim=X_train.shape[1], activation="relu" ))
            model.add(Dropout(0.50))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.50))
            model.add(Dense(64,activation="relu"))
            model.add(Dense(1,activation='linear'))
            model.compile(optimizer='adam',loss='mean_squared_error',metrics=['mae'])
            tmodel = model
            model.fit(X_train,y_train,epochs=epochs,verbose=verbose,validation_data=(X_test,y_test))
            y_hat = model.predict(X_test)
            score = metric(y_test,y_hat)
            if score < best_acc:
                best_acc = score
                best_model = tmodel
            print('Neural Network got validation loss of ',score)
            self.df = self.df.append([['Neural Network',score]])
            print(model.summary())
        
        self.df.columns = 'Model','Validation_Loss'
        self.df.sort_values('Validation_Loss',inplace=True)
        print(pd.DataFrame(self.df))
        
        print('\n\n','*'*40,'\nSuggested Models for Stacking\n','*'*40,'\n',self.df['Model'].iloc[0:5])
        

        print('*'*40,'\n','PLEASE NOTE: these results are calculated using ',metric)
        return best_model
