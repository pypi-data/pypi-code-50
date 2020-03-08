Ans="""
'''
Nullity can be defined as the number of vectors present in the null space
of a given matrix. In other words, the dimension of the null space of the
matrix A is called the nullity of A. The number of linear relations among
the attributes is given by the size of the null space.
The null space vectors B can be used to identify these linear relationship.
'''

from sympy import Matrix 
  
A = [[1, 2, 0], [2, 4, 0], [3, 6, 1]] 
   
A = Matrix(A) 
  
# Number of Columns 
NoC = A.shape[1] 
  
# Rank of A 
rank = A.rank() 
  
# Nullity of the Matrix 
nullity = NoC - rank 
  
print("Nullity : ", nullity) 

"""
