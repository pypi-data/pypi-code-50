#导入数据集生成器
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
data = make_blobs(n_samples=200,centers=2,random_state=8)
X,y=data
plt.scatter(X[:,0],X[:,1],c=y,cmap=plt.cm.spring,edgecolor='k')
plt.show()