Ans="""
'''
Null Space:

The null space of any matrix A consists of all the vectors B such that AB = 0
and B is not zero. It can also be thought as the solution obtained from AB = 0
where A is known matrix of size m x n and B is matrix to be found of size n x k.
The size of the null space of the matrix provides us with the number
of linear relations among attributes.

'''
from sympy import Matrix 
  
# List A  
A = [[1, 2, 0], [2, 4, 0], [3, 6, 1]] 
  
# Matrix A 
A = Matrix(A) 
  
# Null Space of A 
NullSpace = A.nullspace()   # Here NullSpace is a list 
  
NullSpace = Matrix(NullSpace)   # Here NullSpace is a Matrix 
print("Null Space : ", NullSpace) 
  
# checking whether NullSpace satisfies the 
# given condition or not as A * NullSpace = 0 
# if NullSpace is null space of A 
print(A * NullSpace) 
"""
