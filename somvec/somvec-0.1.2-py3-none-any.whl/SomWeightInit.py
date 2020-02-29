import numpy as np

class SomWeightInit:

    def __init__(self, data, map, width, height, seed=10):
        self.data = data
        self.n_features = data.shape[1]
        self.n_rows = data.shape[0]
        self.map = map
        self.mapWidth = width
        self.mapHeight = height
        self.seed = seed

    def initialiseWeights(self, weightInitialisation='uniform'):
        print('Initialising Weights')

        if weightInitialisation == 'hypercube':
            self.initialiseHypercubeWeights()
        else:
            self.initialiseUniformWeights()

        return self.map

    def initialiseUniformWeights(self):
        low = self.data.min(axis=0)
        high = self.data.max(axis=0)
        np.random.seed(self.seed)
        self.map = np.random.uniform(low, high, self.map.shape)

    def initialiseHypercubeWeights(self):
        #Find the four most dis-similar input data points
        Zs1, Zs2 = self.calcZs1Zs2()
        Zs3 = self.calcZs3(Zs1, Zs2)
        Zs4 = self.calcZs4(Zs1, Zs2, Zs3)

        #create a local map with intuitive layout
        map = np.zeros((self.mapHeight, self.mapWidth, self.n_features))

        #initialise the four corners of the map
        map[self.mapHeight-1,0,:] = self.data[Zs1,:]
        map[0,self.mapWidth-1,:] = self.data[Zs2,:]
        map[0,0,:] = self.data[Zs3,:]
        map[self.mapHeight-1,self.mapWidth-1,:] = self.data[Zs4,:]

        for i in range(1, self.mapWidth-1):
            #interpolate the top and bottom rows
            map[0, i, :] = map[0,0,:] + (i - 1) * (map[0,self.mapWidth-1,:] - map[0,0,:]) / (self.mapWidth - 1)
            map[self.mapHeight-1, i, :] = map[self.mapHeight-1,0,:] + (i - 1) * (map[self.mapHeight-1,self.mapWidth-1,:] - map[self.mapHeight-1,0,:]) / (self.mapWidth - 1)

        for i in range(1, self.mapHeight-1):
            #interolate the first and last columns
            map[i, 0, :] = map[0,0,:] + (i - 1) * (map[self.mapHeight-1,0,:] - map[0,0,:]) / (self.mapHeight - 1)
            map[i, self.mapWidth-1, :] = map[0,self.mapWidth-1,:] + (i - 1) * (map[self.mapHeight-1,self.mapWidth-1,:] - map[0,self.mapWidth-1,:]) / (self.mapHeight - 1)

            for j in range(1, self.mapWidth-1):
                #interpolate all the central nodes
                map[i, j, :] = map[i, 0, :] + (j-1)*(map[i,self.mapWidth-1,:] - map[i,0,:])/(self.mapWidth-1)

        #initialise the real map
        self.map = map.reshape((self.mapHeight * self.mapWidth, self.n_features))

    def calcZs1Zs2(self):
        ''''''''''''''''''''''''''''''
        '''Calculate pair (Zs1, Zs2) st ||Zs1-Zs2||2 is maximal over Dt'''
        ''''''''''''''''''''''''''''''
        maximal = np.NINF#negative infinity
        Zs1 = 0 #indicies of records in data
        Zs2 = 1
        for n in range(self.n_rows):
            Zsn = self.data[n,:]
            compare = Zsn - self.data
            norms = np.linalg.norm(compare,axis=1)

            maxNorm = np.max(norms)
            if maxNorm > maximal:
                maximal = maxNorm
                Zs1 = n
                Zs2 = np.argmax(norms)
        print('Zs1: ', Zs1, ' Zs2: ', Zs2, ' maximal: ', maximal)
        return (Zs1, Zs2)

    def calcZs3(self, Zs1, Zs2):
        ''''''''''''''''''''''''''''''
        '''Calculate pair Zs3 st ||Zs1-Zs3||2 + ||Zs2-Zs3||2 is maximal over Dt'''
        ''''''''''''''''''''''''''''''
        #ensure that none of the previous observations are picked
        data = np.delete(self.data, [Zs1,Zs2], axis=0)

        normsZs1 = np.linalg.norm(Zs1 - data,axis=1)
        normsZs2 = np.linalg.norm(Zs2 - data,axis=1)
        Zs3 = np.argmax(normsZs1 + normsZs2)
        #for info's sake
        maximal = np.linalg.norm(data[Zs1,:] - data[Zs3,:])
        maximal += np.linalg.norm(data[Zs2,:] - data[Zs3,:])
        print('Zs3: ', Zs3, ' maximal: ', maximal)

        return Zs3

    def calcZs4(self, Zs1, Zs2, Zs3):
        ''''''''''''''''''''''''''''''
        '''Calculate pair Zs3 st ||Zs1-Zs4||2 + ||Zs2-Zs4||2 + ||Zs3-Zs4||2 is maximal over Dt'''
        ''''''''''''''''''''''''''''''
        #ensure that none of the previous observations are picked
        data = np.delete(self.data, [Zs1,Zs2,Zs3], axis=0)

        normsZs1 = np.linalg.norm(Zs1 - data,axis=1)
        normsZs2 = np.linalg.norm(Zs2 - data,axis=1)
        normsZs3 = np.linalg.norm(Zs3 - data,axis=1)
        Zs4 = np.argmax(normsZs1 + normsZs2 + normsZs3)
        #for info's sake
        maximal = np.linalg.norm(data[Zs1,:] - data[Zs4,:])
        maximal += np.linalg.norm(data[Zs2,:] - data[Zs4,:])
        maximal += np.linalg.norm(data[Zs3,:] - data[Zs4,:])
        print('Zs4: ', Zs4, ' maximal: ', maximal)

        return Zs4
