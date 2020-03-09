import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree,datasets
wine = datasets.load_wine()
X=wine.data[:,:2]
y=wine.target
X_train,X_test,y_train,y_test = train_test_split(X,y)

clf=tree.DecisionTreeClassifier(max_depth=1)
clf.fit(X_train,y_train)

from matplotlib.colors import  ListedColormap
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
cmap_light=ListedColormap(['#FFAAAF','#AAFFAD','#AAAAFD'])
cmap_bold=ListedColormap(['#FF0000','#00FF00','#0000FF'])
# cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
# cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
x_min,x_max=X_train[:,0].min()-1,X_train[:,0].max()+1
y_min,y_max=X_train[:,1].min()-1,X_train[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,.02),
                 np.arange(y_min,y_max,.02))
Z=clf.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
# plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

plt.scatter(X[:,0],X[:,1],c=y,cmap=cmap_bold,edgecolor="k")
plt.xlim(xx.min(),yy.max())
plt.ylim(yy.min(),yy.max())
plt.title("Classifier:{max_depth=1}")
plt.show()