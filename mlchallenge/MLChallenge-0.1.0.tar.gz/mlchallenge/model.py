import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import scipy.stats as stats
import pandas_profiling   #need to install using anaconda prompt (pip install pandas_profiling)

%matplotlib inline
plt.rcParams['figure.figsize'] = 10, 7.5
plt.rcParams['axes.grid'] = True

from matplotlib.backends.backend_pdf import PdfPages

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA   

# reading data into dataframe
data = pd.read_csv("C:/Users/Tushar/Documents/Eloy/Machine Learning Challenge.csv")

data.apply(lambda x: sum(x.isnull()))

data.loc[data['customer_age'] == 'o', 'customer_age'] = np.nan

data.fillna("o", inplace = True)

data.head()

data_new = pd.get_dummies(data, columns=['gender'], drop_first=True, prefix='gender')

data_new.loc[data_new['customer_age'] == 'o', 'customer_age'] = np.nan

data_new['customer_age'] = pd.to_numeric(data_new['customer_age'])

data_new.drop('consumer_id', axis=1, inplace=True)


#Handling missings - Method2
def Missing_imputation(x):
    x = x.fillna(x.median())
    return x

data_new=data_new.apply(lambda x: Missing_imputation(x))


data_new.drop('account_status', axis=1, inplace=True)


#PCA
sc = StandardScaler()
std_model = sc.fit(data_new)

data_scaled = std_model.transform(data_new)

data_scaled = pd.DataFrame(data_scaled, columns=data_new.columns)


data_scaled.describe()


#Using PCA to create to reduce the data to two important features
from sklearn import preprocessing
# reduce to 2 importants features
pca = PCA(n_components=2)
data_pca = pca.fit_transform(data_scaled)
# standardize these 2 new features
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data_pca)
data_pced = pd.DataFrame(np_scaled)


sse = []
list_k = list(range(1, 10))

for k in list_k:
    km = KMeans(n_clusters=k)
    km.fit(data_pced)
    sse.append(km.inertia_)

# Plot sse against k
plt.figure(figsize=(6, 6))
plt.plot(list_k, sse, '-o')
plt.xlabel(r'Number of clusters *k*')
plt.ylabel('Sum of squared distance');


#the curve seems to be  monotonically decreasing and does not show any elbow clealry. From the graph it does looks that value of k
#between 2 and 6 could be a good choice.


#Silhouette analysis can be used to determine the degree of separation between clusters.we want the coefficients to be as 
#big as possible and close to 1 to have a good clusters. Iterating it between 2 and 6



from sklearn.metrics import silhouette_samples, silhouette_score
for i, k in enumerate([2, 3, 4, 5,6,7,8]):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.set_size_inches(18, 7)
    
    # Run the Kmeans algorithm
    km = KMeans(n_clusters=k)
    labels = km.fit_predict(data_pced)
    centroids = km.cluster_centers_

    # Get silhouette samples
    silhouette_vals = silhouette_samples(data_pced, labels)

    # Silhouette plot
    y_ticks = []
    y_lower, y_upper = 0, 0
    for i, cluster in enumerate(np.unique(labels)):
        cluster_silhouette_vals = silhouette_vals[labels == cluster]
        cluster_silhouette_vals.sort()
        y_upper += len(cluster_silhouette_vals)
        ax1.barh(range(y_lower, y_upper), cluster_silhouette_vals, edgecolor='none', height=1)
        ax1.text(-0.03, (y_lower + y_upper) / 2, str(i + 1))
        y_lower += len(cluster_silhouette_vals)

    # Get the average silhouette score and plot it
    avg_score = np.mean(silhouette_vals)
    ax1.axvline(avg_score, linestyle='--', linewidth=2, color='green')
    ax1.set_yticks([])
    ax1.set_xlim([-0.1, 1])
    ax1.set_xlabel('Silhouette coefficient values')
    ax1.set_ylabel('Cluster labels')
    ax1.set_title('Silhouette plot for the various clusters', y=1.02);
    
    # Scatter plot of data colored with labels
    ax2.scatter(data_pced.iloc[:, 0], data_pced.iloc[:, 1], c=labels)
    ax2.scatter(centroids[:, 0], centroids[:, 1], marker='*', c='r', s=250)
    ax2.set_xlim([-2, 2])
    ax2.set_xlim([-2, 2])
    ax2.set_xlabel('Eruption time in mins')
    ax2.set_ylabel('Waiting time to next eruption')
    ax2.set_title('Visualization of clustered data', y=1.02)
    ax2.set_aspect('equal')
    plt.tight_layout()
    plt.suptitle(f'Silhouette analysis using k = {k}',
                 fontsize=16, fontweight='semibold', y=1.05);
				 
				 
				 
#Using n=3 and performing clustering


km_3 = KMeans(n_clusters=3, random_state=123)
km_3 = km_3.fit(data_pced)

#Using n=4 and performing clustering

km_4 = KMeans(n_clusters=4, random_state=123)
km_4 = km_4.fit(data_pced)


data_new['cluster_3'] = km_3.labels_

data_new['cluster_4'] = km_4.labels_


#Visualising clusters with n=3
#plot the different clusters with the 2 main features
fig, ax = plt.subplots()
colors = {0:'red', 1:'blue', 2:'green', 3:'pink'}
ax.scatter(data_new['principal_feature1'], data_new['principal_feature2'], c=data_new["cluster_3"].apply(lambda x: colors[x]))
plt.show()


#Visualising the clusters with n=4
#plot the different clusters with the 2 main features
fig, ax = plt.subplots()
colors = {0:'red', 1:'blue', 2:'green', 3:'pink', 4:'pink'}
ax.scatter(data_new['principal_feature1'], data_new['principal_feature2'], c=data_new["cluster_4"].apply(lambda x: colors[x]))
plt.show()


data_new['principal_feature1'] = data_pced[0]
data_new['principal_feature2'] = data_pced[1]


# Function to return Series of distance between each point and his distance with the closest centroid
def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        distance.set_value(i, np.linalg.norm(Xa-Xb))
    return distance
	
	
#Findning out the anomalies based on the distance using 3 clusters
outliers_fraction = 0.01
distance = getDistanceByPoint(data_pced, km_3)
number_of_outliers = int(outliers_fraction*len(distance))
threshold = distance.nlargest(number_of_outliers).min()
# anomaly25 contain the anomaly result of method 2.1 Cluster (0:normal, 1:anomaly) 
data_new['anomaly25'] = (distance >= threshold).astype(int)


#Finding the number of anomalies identified
data_new.anomaly25.value_counts()


#Visualisin the anomalies
fig, ax = plt.subplots()
colors = {0:'blue', 1:'red'}
ax.scatter(data_new['principal_feature1'], data_new['principal_feature2'], c=data_new["anomaly25"].apply(lambda x: colors[x]))
plt.show()


#Finding the anomalies using 4 clusters
outliers_fraction = 0.01
distance = getDistanceByPoint(data_pced, km_4)
number_of_outliers = int(outliers_fraction*len(distance))
threshold = distance.nlargest(number_of_outliers).min()
# anomaly21 contain the anomaly result of method 2.1 Cluster (0:normal, 1:anomaly) 
data_new['anomaly26'] = (distance >= threshold).astype(int)


#Visualising the anomalies
fig, ax = plt.subplots()
colors = {0:'blue', 1:'red'}
ax.scatter(data_new['principal_feature1'], data_new['principal_feature2'], c=data_new["anomaly26"].apply(lambda x: colors[x]))
plt.show()


#Calculating the number of anomalies found 
data_new.anomaly26.value_counts()

#Again the number of anomalies found is 100.

#Which model to choose can be based on the silhoute score of both the models

print("Silhoute Score for three cluster: " + (silhouette_score(data_pced, data_new.cluster_3)).astype(str))
print("Silhoute Score for four cluster: " + (silhouette_score(data_pced, data_new.cluster_4)).astype(str))

#As stated the model with the score closest to 1 is a better model. Hence the model with 4 cluster is better and more accurate

import pickle

pickle.dump(km_4, open('model.pkl', 'wb'))