import numpy as np
import math as mt
from random import *


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
