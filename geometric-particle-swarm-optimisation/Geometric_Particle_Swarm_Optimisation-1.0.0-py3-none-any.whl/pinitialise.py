import numpy as np
import math as mt

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
