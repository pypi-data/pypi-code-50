import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree,datasets
from sklearn.model_selection import train_test_split
data = pd.read_csv('adult.csv',header=None,index_col=False,
                   names=['年龄','单位性质','权重','学历','年受教育时长','婚姻状况','职业'
                          ,'家庭情况','种族','性别','资产所得','资产损失','周工作时长','原籍','收入'])
data_lite =data[['年龄','单位性质','学历','性别','周工作时长','职业','收入']]

print(data_lite.head())

data_dummies =  pd.get_dummies(data_lite)
print("样本原始特征：\n",list(data_lite.columns),'\n')
print("虚拟变量特征：\n",list(data_dummies.columns))

features = data_dummies.ix[:,'职业_ Transport-moving']
X= features.values
y=data_dummies['收入_ >50K'].values
print('\n\n\n')
print('代码运行结果')
print('=======================')

print('特征形态：{}标签形态{}'.format(X.shape,y.shape))
print('========================')
print('\n\n\n')

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)
go_dating_tree = tree.DecisionTreeClassifier(max_depth=5)
go_dating_tree.fit(X_train,y_train)
print('\n\n\n')
print('代码运行结果')
print('=======================')

print('模型得分{.2f}'.format(go_dating_tree.score(X_test,y_test)))
print('========================')
print('\n\n\n')

Mr_Z=[[37,40,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,
       0,0,0,0,0,0,0,0,0,0,0,0,0]]
dating_dec= go_dating_tree.predict(Mr_Z)
print('\n\n\n')
print('代码运行结果')
print('=======================')
if dating_dec == 1:
    print("大胆去追求真爱吧，这哥们月薪过5万了")
else:
    print("不用缺，不满足你的要求")
print('特征形态：{}标签形态{}'.format(X.shape,y.shape))
print('========================')
print('\n\n\n')


