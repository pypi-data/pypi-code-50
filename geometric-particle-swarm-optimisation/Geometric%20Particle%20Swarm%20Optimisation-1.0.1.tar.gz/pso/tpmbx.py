import numpy as np

def tpmbx(parent_1,parent_2,parent_3):
    
    child=np.zeros(len(parent_1),dtype=int)
    for i in range(0,len(parent_1)):
        if(parent_1[i]!=parent_2[i]):
            child[i]=parent_3[i]
        else:
            child[i]=parent_1[i]

    return child
