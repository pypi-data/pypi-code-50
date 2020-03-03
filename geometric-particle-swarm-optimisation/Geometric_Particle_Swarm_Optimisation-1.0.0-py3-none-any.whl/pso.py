import pandas as pd
import numpy as np
from pinitialise import population_initialisation
from preprocessing import preprocessing
from tpmbx import tpmbx
from mutate import mutate
from svc import svm_fitness

def pso(dm,population_size=40):

    df=dm.copy(deep=True)

    X=df.iloc[:,:-1]
    X=np.array(X,dtype=float)
    X_=preprocessing(X)
    X=X_.copy()
    y=df.iloc[:,len(df.columns)-1]
    y=np.array(y,dtype=int)

    population_size=40
    population=population_initialisation(len(df.columns)-1,population_size=40,no_population_slots=4)

    fitness=np.zeros(population_size,dtype=float)
    historical_fitness=np.zeros(population_size,dtype=float)
    historical_position=population.copy()
    global_fitness=999999
    global_position=np.zeros(len(df.columns)-1,dtype=int)
    for i in range(0,population_size):
    	historical_fitness[i]=999999

    k=0

    while(k!=100):
        
        print('\n',k+1,'th generation in process...')
        for i in range(0,population_size):
            fitness[i]=svm_fitness(X,y,population[i])
            if(str(fitness[i])!=str(historical_fitness[i])):
                f=[fitness[i],historical_fitness[i]]
                if(f.index(min(f))==0):
                    historical_fitness[i]=(fitness[i]).copy()
                    historical_position[i]=(population[i]).copy()
            
        
            if(str(historical_fitness[i])!=str(global_fitness)):
                f=[historical_fitness[i],global_fitness]
                if(f.index(min(f))==0):
                    global_fitness=(historical_fitness[i]).copy()
                    global_position=(population[i]).copy()
        
        for i in range(0,population_size):
            population[i]=(tpmbx(population[i],global_position,historical_position[i])).copy()
            population[i]=(mutate(population[i])).copy()
        k=k+1

    features_best=list(*(np.where(global_position==1)))
    acc=svm_fitness(X,y,global_position,1,1)

    return [features_best,acc]
