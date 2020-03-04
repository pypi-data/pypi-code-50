# VERSION 0.0.1

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from category_encoders import TargetEncoder
from autofeat import AutoFeatClassifier
from autofeat import AutoFeatRegressor

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
            LogisticRegressionCV(max_iter=1000,n_jobs=-1),LogisticRegression(max_iter=1000,n_jobs=-1),SVC(),
            DecisionTreeClassifier(),KNeighborsClassifier(n_jobs=-1),
            SGDClassifier(n_jobs=-1),RandomForestClassifier(n_estimators=n_estimators,n_jobs=-1),
            AdaBoostClassifier(DecisionTreeClassifier(),n_estimators=n_estimators),
            ExtraTreesClassifier(n_estimators=n_estimators,n_jobs=-1),XGBClassifier(n_estimators=n_estimators,n_jobs=-1),
            LGBMClassifier(n_estimators=n_estimators,n_jobs=-1),
            CatBoostClassifier(n_estimators=n_estimators,verbose=0),
            GradientBoostingClassifier(n_estimators=n_estimators),
            GaussianNB()
        ]
        
        self.regressors = [
            'LassoLarsCV','LinearRegression','SVR','DecisionTreeRegressor','KNeighborsRegressor','SGDRegressor',
            'RandomForestRegressor','AdaBoostRegressor','ExtraTreesRegressor','XGBRegressor',
            'LGBMRegressor','CatBoostRegressor','GradientBoostingRegressor','NaiveBayesianRidge'
        ]
        
        self.regressors_models = [
            LassoLarsCV(max_iter=1000),
            LinearRegression(n_jobs=-1),SVR(),DecisionTreeRegressor(),KNeighborsRegressor(n_jobs=-1),
            SGDRegressor(),
            RandomForestRegressor(n_estimators=n_estimators,n_jobs=-1),
            AdaBoostRegressor(DecisionTreeRegressor(),n_estimators=n_estimators,),
            ExtraTreesRegressor(n_estimators=n_estimators,n_jobs=-1),XGBRegressor(n_estimators=n_estimators,n_jobs=-1),
            LGBMRegressor(n_estimators=n_estimators,n_jobs=-1),
            CatBoostRegressor(verbose=0,n_estimators=n_estimators),
            GradientBoostingRegressor(n_estimators=n_estimators),BayesianRidge()
        ]
        self.models_stack = []
        
        print("Welcome to Ghalat Machine Learning!\n\nAll models are set to train\n \
        Have a tea and leave everything on us ;-)")

    def Auto_Feature_Engineering(self,X,y,type_of_task=None,test_data=None,splits=5,fill_na_='median',ratio_drop=0.2,
                               generate_features=False,feateng_steps=2,max_gb=None):
        """
        * X
          Data columns excluding target column
        * y
          target column
        * type_of_task
          Either 'Regression' or 'Classification' (default = None)
          Optional, but in the case of feature generation, compulsory.
        * test_data
          test data if any. (default = None)
        * splits
          splits for stratified k folds when encoding features with target encoding (default = 5)
        * fill_na_
          fill missing values in the columns, either 'Mean' , 'Median' , 'Mode'. for string/character data = Mode. by default = Median 
        * ratio_drop
          if there are so many missing values in column, so its better to drop them. default = 0.2
        * generate_features
          generate new features and select the important ones only (default = False)
        * feateng_steps
          the more step = the more features and more computational power required (default = 2)
        * max_gb 
          limit of gbs
          
         Returns:
         new X and Y
         if you gave the test_data then test_data will be returned too. .e.g. new_X,y,test_data

        """
        X = pd.DataFrame(X)
        y = np.array(y)
        test_data = pd.DataFrame(test_data)
        encode_y = False
        for b in y:
            if type(b) == np.str_:
                encode_y = True
                break
        LE_encoder = LabelEncoder()
        y = LE_encoder.fit_transform(y)

        # filling nans
        for col in X.columns:
            if X[col].isnull().any():
                a = X[col].isnull().value_counts()
                a = pd.DataFrame(a)
                a.reset_index(inplace=True)
                ratio = a.loc[1,1] / a.loc[0,1]
                if ratio > ratio_drop or a.loc[0,0] == 0:
                    X.drop([col],axis=1,inplace=True)
                else:
                    if fill_na_ == 'mode' or X[col].dtype == 'O':
                        X[col].fillna(X[col].mode()[0],inplace=True)
                    elif fill_na_ == 'median':
                        X[col].fillna(X[col].median(),inplace=True)
                    elif fill_na_ == 'mean':
                        X[col].fillna(X[col].mean(),inplace=True)
        if not test_data.empty:
            for col in test_data.columns:
                if test_data[col].isnull().any():
                    a = test_data[col].isnull().value_counts()
                    a = pd.DataFrame(a)
                    a.reset_index(inplace=True)
                    ratio = a.loc[1,1] / a.loc[0,1]
                    if ratio > ratio_drop:
                        test_data.drop([col],axis=1,inplace=True)
                    else:
                        if fill_na_ == 'mode' or test_data[col].dtype == 'O':
                            test_data[col].fillna(test_data[col].mode()[0],inplace=True)
                        elif fill_na_ == 'median':
                            test_data[col].fillna(test_data[col].median(),inplace=True)
                        elif fill_na_ == 'mean':
                            test_data[col].fillna(test_data[col].mean(),inplace=True)

        print('*'*60,"\nSuccessfully dealt with missing data!\n\nX:\n\n",X,'\nTest Data:\n\n',test_data,'\n\n','*'*60)
        # target mean encoding with Stratified KFolds technique to avoid overfitting

        cols = list(X.columns[X.dtypes=='object'])
        encoded = pd.DataFrame([])
        for tr_in,val_in in StratifiedKFold(n_splits=splits,shuffle=True).split(X,y):
            encoder = TargetEncoder(cols=cols,smoothing=0.2)
            encoder.fit(X[cols].iloc[tr_in],y[tr_in])
            encoded = encoded.append(encoder.transform(X[cols].iloc[val_in]),ignore_index=False)
        encoded.sort_index(inplace=True)
        if not test_data.empty:
            encoder = TargetEncoder(cols=cols,smoothing=0.2)
            encoder.fit(X[cols],y)
            test_data[cols] = encoder.transform(test_data[cols])
        X[cols] = encoded
        print('\n','*'*60,"\nSuccessfully encoded categorical data with Target Mean Encoding using Stratified KFolds technique!\n\n",'X:\n\n',X,'\n\nTest Data:\n\n',test_data,'\n\n','*'*60)
        if generate_features == True:
            print('\n','*'*60,"\n Generating new features !\n",'*'*60)
            if type_of_task == 'Regression':
                afr = AutoFeatRegressor(verbose=1,n_jobs=-1,feateng_steps=feateng_steps,max_gb=max_gb)
                X = afr.fit_transform(X,y)
                if not test_data.empty:
                    test_data = afr.transform(test_data)
            elif type_of_task == 'Classification':
                afc = AutoFeatClassifier(verbose=1,n_jobs=-1,feateng_steps=feateng_steps,max_gb=max_gb)
                X = afc.fit_transform(X,y)
                if not test_data.empty:
                    test_data = afc.transform(test_data)
            else:
                print("Please specify type_of_task for feature generation")
            print('\n','*'*60,"\nSuccessfully generated new features! and selected the best features\n\n",'X:\n\n',X,'\n\nTest Data:\n\n',test_data,'\n\n','*'*60)

        if not test_data.empty:
            return X,LE_encoder.inverse_transform(y),test_data
        else:
            return X,LE_encoder.inverse_transform(y)
    
    def nn_classification(self,nn,X_train,output_features,loss_func):
        if nn == "simple":
            model = Sequential()
            model.add(Dense(256, input_dim=X_train.shape[1], activation="relu" ))
            model.add(Dropout(0.50))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.50))
            model.add(Dense(64,activation="relu"))
            model.add(Dense(output_features,activation='sigmoid'))
            model.compile(optimizer='adam',loss=loss_func,metrics=['accuracy'])
            return model
        
        
    def nn_regression(self,nn,X_train):
        if nn == "simple":
            model = Sequential()
            model.add(Dense(256, input_dim=X_train.shape[1], activation="relu" ))
            model.add(Dropout(0.50))
            model.add(Dense(128,activation="relu"))
            model.add(Dropout(0.50))
            model.add(Dense(64,activation="relu"))
            model.add(Dense(1,activation='linear'))
            model.compile(optimizer='adam',loss='mean_squared_error',metrics=['mae'])
            return model
    
    
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
                if folds > 0:
                    cv_score = np.mean(cross_val_score(model,X,y,cv=folds))
                    if cv_score > best_acc:
                        best_acc = cv_score
                        best_model = tmodel
                else:
                    if score > best_acc:
                        best_acc = score
                        best_model = tmodel
                print('Model ',name,' got validation accuracy of ',score)
                if folds > 0:
                    self.df = self.df.append([[name,score,cv_score]])
                else:
                    self.df = self.df.append([[name,score,0]])
            except:
                print("Error occured while training ",name)
        if not (models == None):
            for model in models:
                try:
                    tmodel = model
                    model.fit(X_train,y_train)
                    y_hat = model.predict(X_test)
                    score = metric(y_test,y_hat)
                    if folds > 0:
                        cv_score = np.mean(cross_val_score(model,X,y,cv=folds))
                        if cv_score > best_acc:
                            best_acc = cv_score
                            best_model = tmodel
                    else:
                        if score > best_acc:
                            best_acc = score
                            best_model = tmodel
                            
                    print('Model ',type(model).__name__,' got validation accuracy of ',score)
                    if folds > 0:
                        self.df = self.df.append([[type(model).__name__,score,cv_score]])
                    else:
                        self.df = self.df.append([[type(model).__name__,score,0]])
                except:
                    print("Error occured while training ",type(model).__name__)
        nn_simple = None 
        if neural_net == "Yes" or neural_net == "YES" or neural_net == "yes":
            loss_func = ""
            y_train = to_categorical(y_train)
            output_features = len(np.unique(y))
            if len(np.unique(y)) == 2:
                loss_func = 'binary_crossentropy'
            else:
                loss_func = 'categorical_crossentropy'
            print('\n','*'*40,'\nTraining Neural Network\n','*'*40)
            
            model = self.nn_classification('simple',X_train,output_features,loss_func)
            tmodel = model
            nn_simple = tmodel
            model.fit(X_train,y_train,epochs=epochs,verbose=verbose,validation_data=(X_test,to_categorical(y_test)))
            y_hat = model.predict(X_test)
            y_hat = np.argmax(y_hat,axis=1)
            score = metric(y_test,y_hat)
            if score > best_acc:
                best_acc = score
                best_model = tmodel
            print('Neural Network got validation accuracy of ',score)
            if folds > 0:
                self.df = self.df.append([['Neural Network',score,score]])
            else:
                self.df = self.df.append([['Neural Network',score,0]])
            print(model.summary())
            
        self.df.columns = 'Model','Val_Accuracy','CV on '+str(folds)+' folds'

        if folds > 0:
            self.df.sort_values(self.df.columns[2],inplace=True,ascending=False)
        else:
            self.df.sort_values(self.df.columns[1],inplace=True,ascending=False)
        
        best_model = None
        best_acc = 0
        
        print('\n','*'*60,'\nRound One Results\n','*'*60,'\n',pd.DataFrame(self.df),'\n','*'*60)
        
        models_R2 = []
        names_R2 = []
        all_added = False
        for name in self.df.iloc[:,0].values[0:5]:
            found = False
            for i,n in enumerate(self.classifiers):
                if n == name:
                    found = True
                    names_R2.append(name)
                    models_R2.append(self.classifier_models[i])
            if found == False:
                if name == "Neural Network":
                    names_R2.append('Neural Network')
                    models_R2.append(nn_simple)
                else:
                    if not models == None and all_added == False:
                        all_added = True
                        for m in models:
                            names_R2.append(type(model).__name__,)
                            models_R2.append(m)
        df_2 = pd.DataFrame([])
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_Size,shuffle=shuffle)
        for name,model in zip(names_R2,models_R2):
            try:
                nn = False
                tmodel = model
                if name == 'Neural Network':
                    ty_train = y_train
                    nn = True
                    y_train = to_categorical(y_train)
                    model.fit(X_train,y_train,epochs=epochs,verbose=verbose,validation_data=(X_test,to_categorical(y_test)))
                else:
                    model.fit(X_train,y_train)
                y_hat = model.predict(X_test)
                if name == 'Neural Network':
                    y_hat = np.argmax(y_hat,axis=1)
                score = metric(y_test,y_hat)
                if folds > 0 :
                    if name == 'Neural Network':
                        cv_score = score
                    else:
                        cv_score = np.mean(cross_val_score(model,X,y,cv=folds))
                    if cv_score > best_acc:
                        best_acc = cv_score
                        best_model = tmodel
                else:
                    if score > best_acc:
                        best_acc = score
                        best_model = tmodel
                print('Model ',name,' got validation accuracy of ',score)
                if folds > 0:
                    df_2 = df_2.append([[name,score,cv_score]])
                else:
                    df_2 = df_2.append([[name,score,0]])
                if nn == True:
                    y_train = ty_train
            except:
                print("Error occured while training ",name)
                
        df_2.columns = 'Model','Val_Accuracy','CV on '+str(folds)+' folds'
        if folds > 0:
            df_2.sort_values(df_2.columns[2],inplace=True,ascending=False)
        else:
            df_2.sort_values(df_2.columns[1],inplace=True,ascending=False)
        print('\n','*'*60,'\nRound Two Results\n','*'*60,'\n',pd.DataFrame(df_2),'\n','*'*60)
                    
        
        print('\n\n','*'*40,'\nSuggested Models for Stacking\n','*'*40,'\n',df_2['Model'].iloc[0:3])
        
        print('*'*40,'\n','PLEASE NOTE: these results are calculated using ',metric)
        
        self.df = pd.DataFrame([])
        return best_model
        
    def GMLRegressor(self,X,y,metric = mean_squared_error, test_Size = 0.3, shuffle = True, scaler = 'SS',models=None,
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
        nn_simple = None
        if neural_net == "Yes" or neural_net == "YES" or neural_net == "yes":
            loss_func = ""           
            print('\n','*'*40,'\nTraining Neural Network\n','*'*40)
            model = self.nn_regression('simple',X_train)
            tmodel = model
            nn_simple = tmodel
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
        
        print('\n','*'*60,'\nRound One Results\n','*'*60,'\n',pd.DataFrame(self.df),'\n','*'*60)
        best_model = None
        best_acc = 1000
        
        models_R2 = []
        names_R2 = []
        all_added = False
        for name in self.df.iloc[:,0].values[0:5]:
            found = False
            for i,n in enumerate(self.regressors):
                if n == name:
                    found = True
                    names_R2.append(name)
                    models_R2.append(self.regressors_models[i])
            if found == False:
                if name == "Neural Network":
                    names_R2.append('Neural Network')
                    models_R2.append(nn_simple)
                else:
                    if not models == None and all_added == False:
                        all_added = True
                        for m in models:
                            names_R2.append(type(model).__name__,)
                            models_R2.append(m)
        df_2 = pd.DataFrame([])
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_Size,shuffle=shuffle)
        for name,model in zip(names_R2,models_R2):
            try:
                tmodel = model
                model.fit(X_train,y_train)
                y_hat = model.predict(X_test)
                score = metric(y_test,y_hat)
                if score < best_acc:
                    best_acc = score
                    best_model = tmodel
                print('Model ',name,' got validation accuracy of ',score)
                df_2 = df_2.append([[name,score]])
            except:
                print("Error occured while training ",name)
                
        df_2.columns = 'Model','Val_Accuracy'
        df_2.sort_values(df_2.columns[1],inplace=True)
        print('\n','*'*60,'\nRound Two Results\n','*'*60,'\n',pd.DataFrame(df_2),'\n','*'*60)
                    
        
        print('\n\n','*'*40,'\nSuggested Models for Stacking\n','*'*40,'\n',df_2['Model'].iloc[0:3])
        

        print('*'*40,'\n','PLEASE NOTE: these results are calculated using ',metric)
        self.df = pd.DataFrame([])
        return best_model
