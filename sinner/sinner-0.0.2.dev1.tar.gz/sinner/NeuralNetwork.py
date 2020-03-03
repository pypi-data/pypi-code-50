#!/usr/bin/python3

from random import random
from math import exp
from os import linesep

class NeuralNetwork:
    def __init__(self, layersSize, learningRate=0.5):
        self.__inputNeurons = layersSize[0]
        self.__outputNeurons = layersSize[-1]
        self.__learningRate = learningRate
        self.network = list()
        for prev, cur in zip(layersSize, layersSize[1:]):
            self.network.append([{'weights':[random() for i in range(prev+1)]} for i in range(cur)])
             
    def __str__(self):
        return str(self.network)

    def __activate(self, weights, inputs):
        activation = weights[-1]
        for i in range(len(weights)-1):
            activation += weights[i]*inputs[i]
        return activation

    def __transfer(self, activation):
        return 1.0/(1.0 + exp(-activation))

    def eval(self, inputs):
        if(len(inputs) != self.__inputNeurons):
            raise ValueError("All input should consider "+str(self.__inputNeurons)+" input neuron nodes")
        currentInputs = inputs+[None]
        for layer in self.network:
            newInputs = []
            for neuron in layer:
                activation = self.__activate(neuron['weights'],currentInputs)
                neuron['output'] = self.__transfer(activation)
                newInputs.append(neuron['output'])
            currentInputs = newInputs
        return currentInputs

    def __transferDerivative(self, output):
        return output * (1.0 - output)

    def __backwardPropagateError(self, expected):
        if(len(expected) != self.__outputNeurons):
            raise ValueError("All expected output should consider "+str(self.__outputNeurons)+" output neuron nodes")
        #output layer first
        for i in range(len(self.network[-1])):
            neuron = self.network[-1][i]
            neuron['delta'] = (expected[i] - neuron['output'])*self.__transferDerivative(neuron['output'])

        #now the hidden layers
        for i in reversed(range(len(self.network)-1)):
            layer = self.network[i]
            errors = list()
            for j in range(len(layer)):
                error = 0.0
                for neuron in self.network[i+1]:
                    error += (neuron['weights'][j]*neuron['delta'])
                neuron = layer[j]
                neuron['delta'] = error*self.__transferDerivative(neuron['output'])

    def __updateWeights(self, inputs):
        for i in range(len(self.network)):
            currentInputs = (inputs[:-1] if i == 0 else [neuron['output'] for neuron in self.network[i-1]])
            for neuron in self.network[i]:
                for j in range(len(currentInputs)):
                    neuron['weights'][j] += self.__learningRate * neuron['delta'] * currentInputs[j]

                #weighting bias
                neuron['weights'][-1] += self.__learningRate * neuron['delta']

    def train(self, trainingInputs, trainingOutputs, epochs=1):
        if(len(trainingInputs) != len(trainingOutputs)):
            raise ValueError("Training inputs and outputs should have the same number of tests (rows)")

        log = ""
        for epoch in range(epochs):
            SSE = 0
            for i in range(len(trainingInputs)):
                outputs = self.eval(trainingInputs[i])
                self.__backwardPropagateError(trainingOutputs[i])
                self.__updateWeights(trainingOutputs[i])
                SSE += sum([(trainingOutputs[i][j] - outputs[j])**2 for j in range(len(trainingOutputs[i]))])
            log+=("epoch: %d, MSE: %.6f" % (epoch+1, (SSE / len(trainingInputs))))+linesep
        return log

#if __name__ == "__main__":
#    nn = NeuralNetwork(layersSize=[2,4,5,1],learningRate=1)
#    inputs = [[0,0],
#            [0,1],
#            [1,0],
#            [1,1]]
#    outputs = [[1],[0],[0],[1]]
#    print(nn.train(inputs,outputs,epochs=10000))
#    for inputRow in inputs:
#        print(str(inputRow)+" "+str(nn.eval(inputRow)))
#    print(nn)
#
