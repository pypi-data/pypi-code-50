import pandas as pd
import numpy as np
import math as mt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from random import *
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

def tpmbx(parent_1,parent_2,parent_3):
    
    child=np.zeros(len(parent_1),dtype=int)
    for i in range(0,len(parent_1)):
        if(parent_1[i]!=parent_2[i]):
            child[i]=parent_3[i]
        else:
            child[i]=parent_1[i]

    return child


def svmm(X,y,k=0):
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
    clf=svm.SVC(kernel='linear').fit(X_train,y_train)
    scores=cross_val_score(clf,X,y,cv=10)
    
    if(k==1):
        return(np.mean(scores)*100)
    
    return np.mean(scores)


def svm_fitness(X,y,l,b=1,k=0):
    
    if(sum(l)==0):
        return 99999

    features=list(*(np.where(l==1)))
    X=X[:,features]
    
    if(k==1):
        return(svmm(X,y,k))

    accuracy=svmm(X,y,k)
    fitness=(0.75*(100/accuracy))+(0.25*(sum(l)))
    #fitness=(accuracy/(b*sum(l)))-(100/(b*(len(l))))
    
    return fitness

def mutate(a,m_probability=0.1):

    no_of_mutations=mt.ceil(m_probability*len(a))
    positions=[]
    a_c=np.zeros(len(a),dtype=int)
    while(sum(a_c)==0):
        a_c=a.copy()
        for i in range(0,no_of_mutations):
            r=randint(0,(len(a)-1))
            while(r in positions):
                r=randint(0,(len(a)-1))
            positions.append(r)
            if(a_c[r]==1):
                a_c[r]=0
            else:
                a_c[r]=1
    a=a_c.copy()

    return a

def population_initialisation(n,population_size=40,no_population_slots=4):
    
    population=[]
    population_slots=np.zeros(no_population_slots,dtype=int)
    population_slots_size=np.zeros(no_population_slots,dtype=int)
    pop_prob=np.zeros(no_population_slots,dtype=float)
    k=10
    N=4
    if(n<15):
        N=2
    for i in range(0,no_population_slots):
        population_slots[i]=(population_size/100)*k
        population_slots_size[i]=N
        pop_prob[i]=N/n
        k=k+10
        if(n<15):
            N=N+2
        else:
            N=N+4
    population_slots_size[-1]=n//2
    pop_prob[-1]=(n//2)/n
    
    for i in range(0,no_population_slots):
        for j in range(0,population_slots[i]):
            a=np.random.choice([1,0],size=(n,),p=[pop_prob[i],(1-pop_prob[i])])
            while(sum(a)!=population_slots_size[i]):
                a=np.random.choice([1,0],size=(n,),p=[pop_prob[i],(1-pop_prob[i])])
            population.append(a)

    population=np.array(population,dtype=int)

    print('\nPopulation Initialised\n')

    return population

def preprocessing(X):
    
    imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
    imputer=imputer.fit(X)
    X=imputer.transform(X)
    X=MinMaxScaler().fit_transform(X)
    
    return X

def klp_pso(dm,population_size=40):

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
