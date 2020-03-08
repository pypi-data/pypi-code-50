Ans="""

'''
To do this, we find the values ofλwhich satisfy thecharacteristic equationof thematrixA, namely those values ofλfor whichdet(A−λI) = 0,whereIis the 3×3identity matrix
Once theeigenvaluesof a matrix (A) have been found, we can find theeigenvectorsby Gaussian Elimination.•STEP 1: For each eigenvalueλ, we have(A−λI)x=0,wherexis theeigenvectorassociated witheigenvalueλ.•STEP 2: Findxby Gaussian elimination. That is, convert the augmented matrix(A−λI...0)to row echelon form, and solve the resulting linear system byback substitution.We find theeigenvectorsassociated with each of theeigenvalues
row echeleon is upper triangular
'''

import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m) 
print( "Eigenvalues of the said matrix",w)
print( "Eigenvectors of the said matrix",v)

"""
