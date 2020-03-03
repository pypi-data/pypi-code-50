from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def preprocessing(X):
    
    imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
    imputer=imputer.fit(X)
    X=imputer.transform(X)
    X=MinMaxScaler().fit_transform(X)
    
    return X
