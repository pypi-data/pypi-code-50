# 使用 K 最近邻算法来拟合这些数据

#导入数据集生成器
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
#导入数据集生成器
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
# %matplotlib inline
data = make_blobs(n_samples=200,centers=2,random_state=8)
X,y=data
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolor='k')
plt.show()
clf = KNeighborsClassifier()
clf.fit(X,y)
x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,0].min()-1,X[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,.02),
                 np.arange(y_min,y_max,.02))
Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)

plt.pcolormesh(xx,yy,Z)
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolor="k")
plt.xlim(xx.min(),yy.max())
plt.ylim(yy.min(),yy.max())
plt.title("Classifier:KNN")
plt.show()

data2 = make_blobs(n_samples=200,centers=5,random_state=8)
X2,y2=data2
#使用散点图将数据集可视化
plt.scatter(X2[:,0],X2[:,1],c=y2,cmap=plt.cm.spring,edgecolor="k")
plt.show()