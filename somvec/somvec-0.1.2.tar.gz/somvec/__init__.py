import pandas as pd
import numpy as np
import os
import pickle
from datetime import datetime

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#plot processing
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
import matplotlib as mpl

#custom classes
from .SomWeightInit import SomWeightInit as WI

class SOM:

    def __init__(self, df=None, mapWidth=20, mapHeight=20, classificationAttributes=np.array([])
        , weightInitialisation='uniform', PBC=True, epochs=500
        , initialLearnRate=0.01, initialKernelWidth=10, decayLearnRate=20, decayKernelWidth=10
        , errType='Topological', errThreshold=1e-7, errWindow = 30, seed=20
        , scenarioName='SOM_scenario1', save=True, savePath='SavedModels/', load=False
        , loadPath='SavedModels/', saveImages=True, imagePath='Images/', saveClusters=True, clusterPath='Clusters/'):

        self.scenarioName = scenarioName
        print('SOM Scenario: ', scenarioName)

        #Data inputs
        self.features = list(df)
        self.data = df.values
        self.n_features = df.shape[1]
        self.n_rows = df.shape[0]

        #map dimensions
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.map = np.zeros((self.mapHeight * self.mapWidth, self.n_features)) #just create the map so not null (will intialise later)

        #semi-supervised
        self.isSemiSupervised = False
        if classificationAttributes.size > 0:
            self.classificationAttributes = classificationAttributes.astype(np.int32)
            self.isSemiSupervised = True

        #training parameters
        self.weightInitialisation = weightInitialisation
        self.PBC = bool(PBC)
        self.epochs = epochs
        self.initialLearnRate = initialLearnRate
        self.lr = initialLearnRate
        self.decayLearnRate = decayLearnRate
        self.initialKernelWidth = initialKernelWidth
        self.sigma = self.initialKernelWidth
        self.decayKernelWidth = decayKernelWidth
        self.minTrainEpochs = 5 #have a hard-coded minimum just in case
        self.seed = seed

        #topological/quantisation error
        self.errType = errType
        self.errWindow = errWindow
        self.errThreshold = errThreshold

        #File paths
        self.save = save
        self.savePath = savePath
        if savePath == 'SavedModels/':
            self.savePath += 'Model_' + scenarioName + '.pkl'
        self.load = load
        self.loadPath = loadPath
        if loadPath == 'SavedModels/':
            self.loadPath += 'Model_' + scenarioName + '.pkl'
        self.saveImages = saveImages
        self.imagePath = imagePath
        if imagePath == 'Images/':
            self.imagePath += scenarioName + '/'
        self.saveClusters = saveClusters
        self.clusterPath = clusterPath
        if clusterPath == 'Clusters/':
            self.clusterPath += scenarioName +'.pkl'

        if not os.path.exists(self.imagePath):
            os.makedirs(self.imagePath)

    def initMapCoords(self):
        #initialise map hexagonal co-ordinates (for plotting purposes)
        self.mapCoords = np.zeros((2,self.mapHeight, self.mapWidth))
        self.mapCoords[1,:,:] = np.arange(self.mapHeight).reshape((self.mapHeight,1)) #y
        self.mapCoords[1,:,:] = self.mapCoords[1,:,:] * 2/np.sqrt(3)*3/4#transform to co-ordinates
        self.mapCoords[0,:,:] = np.arange(self.mapWidth).reshape((1,self.mapWidth)) #x
        self.mapCoords[0,::2,:] = self.mapCoords[0,::2,:] + 0.5 #transformation: add 0.5 to every second row
        self.mapCoords = self.mapCoords.reshape((2,self.mapHeight * self.mapWidth))#flatten for efficiency!

        #calculate each coord's closest neighbour for topological error calc (note that some will have multiple that are just as close)
        diff = self.mapCoords.transpose() - self.mapCoords.transpose()[:,None]#couldn't figure it out without using transpose function
        norm = np.linalg.norm(diff, axis=2)#calc euclidean distance
        np.fill_diagonal(norm, np.inf)#otherwise argmin will choose its own position (since euclidean distance to itself is zero)
        self.NearestCoords = norm.argmin(axis=0).reshape(self.mapHeight * self.mapWidth)

        #Calculate each the distance from each coord to every other coord on the grid
        self.calcWeightDistances()

    def updateLearningRate(self, t):
        self.lr = self.initialLearnRate * np.exp(-t/self.decayLearnRate)

    def updateSigma(self, t):
        self.sigma = self.initialKernelWidth * np.exp(-t/self.decayKernelWidth)

    def findBMU(self, obs):
        compare = obs - self.map
        #for semi-supervised learning
        if self.isSemiSupervised:
            compare = np.delete(compare, self.classificationAttributes, axis=1)
        norms = np.linalg.norm(compare,axis=1)
        bmu = np.argmin(norms)
        return bmu

    def calcWeightDistances(self):
        #https://arxiv.org/pdf/1312.5753.pdf would suggest that periodic boundary conditions outperform non-PBC topologies.

        self.weightDistances = {}#a dictionary of the distances from the key weight to every other weight
        if self.PBC == False:
            #For each potential BMU calculate the distance between it and every other weight in the grid
            for i in range(self.mapWidth * self.mapHeight):
                #Calc ||Cba - Cyx||2 - where ab is the co-ordinate of the BMU and xy are all the map co-ordinates
                compare = self.mapCoords - self.mapCoords[:,i].reshape((2,1))
                self.weightDistances[i] = np.square(np.linalg.norm(compare, axis=0))
        else:
            '''Hexagonal Periodic Boundary Conditions''' #adapted from package SimpSOM (https://pypi.org/project/SimpSOM/)
            if self.mapHeight%2==0:
                offset=0
            else:
                offset=0.5
            offset2 = self.mapHeight*2/np.sqrt(3)*3/4
            for i in range(self.mapWidth * self.mapHeight):
                #shape of mapcoords: (2,self.mapHeight * self.mapWidth)
                normsAll = np.zeros(shape=(9,self.mapHeight * self.mapWidth))
                compare = self.mapCoords[:,i].reshape((2,1)) - self.mapCoords
                #TODO: Try and eliminate the norm and then square operation (should be possible with np.dot or something?)
                #normal
                normsAll[0,:] = np.square(np.linalg.norm(compare, axis=0))
                #right
                adj = compare + np.array([self.mapWidth,0]).reshape((2,1))
                normsAll[1,:] = np.square(np.linalg.norm(adj, axis=0))
                #left
                adj = compare - np.array([self.mapWidth,0]).reshape((2,1))
                normsAll[2,:] = np.square(np.linalg.norm(adj, axis=0))
                #bottom
                adj = compare + np.array([offset, offset2]).reshape((2,1))
                normsAll[3,:] = np.square(np.linalg.norm(adj, axis=0))
                #top
                adj = compare - np.array([offset, offset2]).reshape((2,1))
                normsAll[4,:] = np.square(np.linalg.norm(adj, axis=0))
                #bottom right
                adj = compare + np.array([self.mapWidth + offset, offset2]).reshape((2,1))
                normsAll[5,:] = np.square(np.linalg.norm(adj, axis=0))
                #bottom left
                adj = compare + np.array([-self.mapWidth + offset, offset2]).reshape((2,1))
                normsAll[6,:] = np.square(np.linalg.norm(adj, axis=0))
                #top right
                adj = compare + np.array([self.mapWidth - offset, -offset2]).reshape((2,1))
                normsAll[7,:] = np.square(np.linalg.norm(adj, axis=0))
                #top left
                adj = compare + np.array([-self.mapWidth - offset, -offset2]).reshape((2,1))
                normsAll[8,:] = np.square(np.linalg.norm(adj, axis=0))

                self.weightDistances[i] = np.min(normsAll, axis=0)

    def updateWeights(self, obs, bmu):

        norms = self.weightDistances[bmu]
        #calc the Gaussian Kernel: lr * exp(-||Cba - Cyx||2)
        divisor = 2*self.sigma**2
        if divisor > 0:
            kernel = self.lr * np.exp(-(norms)/divisor).reshape((self.mapHeight * self.mapWidth,1))
            deltaWeight = (obs - self.map) * kernel
            self.map += deltaWeight

    def calcQuantisationError(self, BMUs):
        compare = self.data - self.map[BMUs]
        return np.mean(np.linalg.norm(compare, axis=1))

    def calcTopologicalErrror(self, show_error=False):
        #calculate the closest weight in weight space
        diff = self.map - self.map[:,None]
        norm = np.linalg.norm(diff, axis=2)#calc euclidean distance
        np.fill_diagonal(norm, np.inf)#otherwise argmin will choose its own position (since euclidean distance to itself is zero)
        nearestWeights = norm.argmin(axis=0).reshape(self.mapHeight * self.mapWidth)

        # average calc ratio of distance from weight to nearest weight by co-ordinate to distance from weight to nearest weight in weight space
        ratios = np.linalg.norm(self.map - self.map[self.NearestCoords,:], axis=1) / np.linalg.norm(self.map - self.map[nearestWeights,:], axis=1)
        if show_error:
            print('Topological error: ', ratios.reshape(self.mapHeight, self.mapWidth))
        return np.mean(ratios)

    def fit(self, show_plot=True, verbose=True):
        #initialise map hexagonal co-ordinates
        self.initMapCoords()
        #initialise weights
        wi = WI(self.data, self.map, self.mapWidth, self.mapHeight, self.seed)
        self.map = wi.initialiseWeights(self.weightInitialisation)

        err = np.zeros(self.errWindow)
        avgErr = np.inf#arbitraty large number
        errHistory = np.zeros(self.epochs - self.errWindow)
        np.random.seed(self.seed)#set seed for reproducibility
        for t in range(self.epochs):
            #shuffle dataset
            np.random.shuffle(self.data)
            BMUs = np.zeros(self.n_rows, np.int32)
            for n in range(self.n_rows):
                bmu = self.findBMU(self.data[n,:])
                BMUs[n] = bmu
                self.updateWeights(self.data[n,:], bmu)

            self.updateLearningRate(t)
            self.updateSigma(t)

            '''calculate the quanitzation error: as a stopping criterion'''
            err[1:] = err[:-1]#slide the window on self.errWindow
            if self.errType == 'Topological':
                err[0] = self.calcTopologicalErrror()
            else:
                err[0] = self.calcQuantisationError(BMUs)

            if t >= self.errWindow:
                prevAvgErr = avgErr
                avgErr = np.mean(err)
                errHistory[t-self.errWindow] = avgErr
                if (prevAvgErr - avgErr) < self.errThreshold and t > self.minTrainEpochs: #AvgErr and prevAvgErr should be the other way around
                    print('Map has converged according to '+ self.errType +' error method after ', t, ' iterations')
                    plt.plot(errHistory[:t-self.errWindow], label="Moving Average of "+ self.errType +" Error")
                    plt.title(self.errType + ' error moving average history.')
                    plt.ylabel(self.errType + ' Error')
                    plt.xlabel('Epochs above ' + str(self.errWindow))
                    plt.legend(loc="upper right")
                    if self.saveImages:
                        plt.savefig(self.imagePath + self.errType + 'ErrorMovingAvergage.png')
                    if show_plot:
                        plt.show()
                    else:
                        plt.close()
                    break#break out of loop

            #plot the map every so often to see how it changes
            if t % 250 == 0 and t > 0 and show_plot and verbose:
                self.plotMap(0)
            #Plot training progress to monitor the improvement over time
            if t % 5 == 0 and verbose:
                print('Training progress: %.2f%%. %s error %.4f' % (float(t)/self.epochs*100, self.errType, err[0]))
        BMUs = self.predict(self.data)
        self.BMUcounts = np.bincount(BMUs, minlength = self.mapWidth*self.mapHeight)
        #print('BMU Counts: \n', self.BMUcounts.reshape((self.mapHeight, self.mapWidth)))
        top_error = self.calcTopologicalErrror(False)
        print('Topological error (near 1 is good):', top_error)
        quant_error = self.calcQuantisationError(BMUs)
        print('Quantisation error (near 0 is good):', quant_error)
        self.writeToTrainingLogs(top_error, quant_error, t)

        #save the model
        if self.save:
            self.saveModel()
        self.plotMap(toPlot=self.BMUcounts, FeatureName='Map BMU Counts', show_plot=show_plot)

        #plot feature maps
        for f in range(self.n_features):
            self.plotMap(f, 'viridis', show_plot=show_plot)

    def predict(self, data):
        #returns an array of BMUs for each observation
        BMUs = np.zeros(data.shape[0], dtype=np.int32)
        for i in range(data.shape[0]):
            BMUs[i] = self.findBMU(data[i,:])
        return BMUs

    def plotMap(self, feature_ind=0, cscheme='viridis', toPlot=None, FeatureName='',show_plot=True):
        #adapted from package SimpSOM (https://pypi.org/project/SimpSOM/)

        widthP=100
        dpi=72
        xInch = self.mapWidth*widthP/dpi
        yInch = self.mapHeight*widthP/dpi
        fig=plt.figure(figsize=(xInch, yInch), dpi=dpi)

        #center = mapcoords
        #weights = map
        ax = fig.add_subplot(111, aspect='equal')
        #cmap = plt.get_cmap(cscheme)
        cmap = cm.get_cmap(cscheme)
        mpl.rc('image', cmap=cscheme)#change the default matplotlib colourmap (just for this session)
        if toPlot is None:
            plotMap = np.vstack((self.mapCoords.reshape(2,self.mapHeight,self.mapWidth), self.map[:,feature_ind].reshape(1,self.mapHeight,self.mapWidth)))
        else:
            plotMap = np.vstack((self.mapCoords.reshape(2,self.mapHeight,self.mapWidth), toPlot.reshape(1,self.mapHeight,self.mapWidth)))
        plotMap = plotMap.reshape((3, self.mapHeight * self.mapWidth))
        #print('plotmap shape: ', plotMap.shape)

        patches=[]
        for i in np.arange(self.mapHeight * self.mapWidth):
            hexagon = RegularPolygon((plotMap[0,i],plotMap[1,i]), numVertices=6, radius=.95/np.sqrt(3) ,
								 orientation=np.radians(0),
								 facecolor=cmap(plotMap[2,i]))
            patches.append(hexagon)

        p = PatchCollection(patches)
        #p.set_array(np.flip(plotMap[2,:].reshape(self.mapHeight,self.mapWidth),0).flatten())
        p.set_array(plotMap[2,:].flatten())
        ax.add_collection(p)

        ax.axis('off')
        ax.autoscale_view()

        if toPlot is None:
            featureName = str(self.features[feature_ind])
        else:
            featureName = FeatureName
        ax.set_title('Node Grid w Feature ' +  featureName, size=40)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.0)
        cbar=plt.colorbar(ax.collections[0], cax=cax)
        cbar.set_label('Feature ' +  featureName +' value', size=40, labelpad=30)
        cbar.ax.tick_params(labelsize=25)
        plt.sca(ax)
        #printName='nodesFeature_'+str(colnum)+'.png'

        if self.saveImages:
            plt.savefig(self.imagePath + featureName +'.png')
        #print('Figures saved to: '+self.imagePath + featureName +'.png')
        if show_plot:
            plt.show()
        else:
            plt.close()
        #plt.clf()

    def cluster(self, K=2, show_plot=True):
        self.K = K
        self.kmeans = KMeans(n_clusters=K, random_state=self.seed).fit(self.map)

        #create an empty dataframe in which to store the BMU and Clusters info for each observation
        labels = pd.DataFrame(index=np.arange(self.n_rows), columns=['BMU','Cluster'])

        bmuList = []
        clusterList = []
        for i in range(self.n_rows):
            bmu = self.findBMU(self.data[i,:])
            bmuList.append(bmu)
            clusterList.append(self.kmeans.labels_[bmu])
        series = pd.Series(bmuList)
        labels["BMU"] = series.copy()
        series = pd.Series(clusterList)
        labels["Cluster"] = series.copy()

        #save a copy of the SOM grid with its associated cluster label
        self.mapClusters = self.kmeans.labels_

        #save a copy of the clusters
        if self.saveClusters:
            self.saveClusterLabels()

        #plot clusters after the probabilities have been printed
        self.plotMap(toPlot=self.kmeans.labels_, FeatureName='Clusters', show_plot=show_plot)

        return labels

    def optimiseCluster(self, minK=2, maxK=11):
        print('\nSilhouette score: \n\t-Best value: 1; \n\t-Worst value: -1 (neg values generally indicate incorrect cluster assignment); \n\t-Values near 0 inidcate overlapping clusters')
        for K in range(minK, maxK):
            kmeans = KMeans(n_clusters=K, random_state=self.seed).fit(self.map)
            silhouetteScore = silhouette_score(self.map, kmeans.labels_, metric='euclidean')
            print('K:', K, '. silhouetteScore:', silhouetteScore)

    def assignClusterLabels(self):

        #create an empty dataframe in which to store the BMU and Clusters info for each observation
        labels = pd.DataFrame(index=np.arange(self.n_rows), columns=['BMU','Cluster'])

        #add BMU and Cluster labels
        bmuList = []
        clusterList = []
        for i in range(self.n_rows):
            bmu = self.findBMU(self.data[i,:])
            bmuList.append(bmu)
            clusterList.append(self.mapClusters[bmu])
        series = pd.Series(bmuList)
        labels["BMU"] = series.copy()
        series = pd.Series(clusterList)
        labels["Cluster"] = series.copy()

        return labels

    def plotLabels(self, labels):

        features = list(labels)
        features.remove('BMU')#need this for the group by but won't want to plot it
        map = np.zeros((self.mapHeight * self.mapWidth, len(features)))
        groupby = labels.groupby('BMU').mean()
        for i in range(len(features)):
            map[groupby.index.values, i] = groupby[features[i]].values
            self.plotMap(toPlot=map[:, i], FeatureName=features[i])

    def saveModel(self):
        model = {'map': self.map, 'mapWidth': self.mapWidth, 'mapHeight': self.mapHeight
        , 'mapCoords': self.mapCoords, 'BMUcounts' : self.BMUcounts}
        try:
            outfile = open(self.savePath, 'wb')
        except (FileNotFoundError) as e:
            os.makedirs(os.path.dirname(self.savePath))
            outfile = open(self.savePath, 'wb')
        pickle.dump(model, outfile)
        outfile.close()

    def loadModel(self):
        infile = open(self.loadPath, 'rb')
        model = pickle.load(infile)
        infile.close()
        #load variables
        self.map = model['map']
        self.mapHeight = model['mapHeight']
        self.mapWidth = model['mapWidth']
        self.mapCoords = model['mapCoords']
        self.BMUcounts = model['BMUcounts']

    def saveClusterLabels(self):
        labels = {'clusters': self.mapClusters}
        try:
            outfile = open(self.clusterPath, 'wb')
        except (FileNotFoundError) as e:
            os.makedirs(os.path.dirname(self.clusterPath))
            outfile = open(self.clusterPath, 'wb')
        pickle.dump(labels, outfile)
        outfile.close()

    def loadClusterLabels(self):
        infile = open(self.clusterPath, 'rb')
        labels = pickle.load(infile)
        infile.close()
        #load variables
        self.mapClusters = labels['clusters']

    def writeToTrainingLogs(self, top_error, quant_error, epoch, fname='SOMlog.csv'):
        #check if file exists. Create it if it does not
        if os.path.exists(fname):
            log = pd.read_csv(fname)
        else:
            #create empty dataframe with appropriate column headings
            log = pd.DataFrame(columns=['scenarioName','PBC','errWindow','errThreshold'
            ,'isSemiSupervised','weightInitialisation','initialLearnRate','initialKernelWidth'
            ,'decayLearnRate','decayKernelWidth','mapWidth','mapHeight','n_rows'
            ,'maxEpochs','actualEpochs','timeStamp','topologicalError','quantisationError'])

        l = [self.scenarioName, self.PBC, self.errWindow, self.errThreshold \
            , self.isSemiSupervised, self.weightInitialisation, self.initialLearnRate, self.initialKernelWidth \
            , self.decayLearnRate, self.decayKernelWidth, self.mapWidth, self.mapHeight, self.n_rows \
            , self.epochs, epoch, datetime.now(), str(top_error), str(quant_error)]
        log.loc[log.shape[0]] = l
        log.to_csv(fname, index=False)
