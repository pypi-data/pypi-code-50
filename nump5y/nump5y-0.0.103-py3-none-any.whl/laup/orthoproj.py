Ans="""

'''

Orthogonal projection is a cornerstone of vector space methods, with many diverse applications. These include, but are not limited to, Least squares projection, also known as linear regression. Conditional expectations for multivariate normal (Gaussian) distributions.
'''

import numpy as np 
  
# vector u  
u = np.array([2, 5, 8])        
  
# vector n: n is orthogonal vector to Plane P 
n = np.array([1, 1, 7])        
   
# Task: Project vector u on Plane P 
  
# finding norm of the vector n  
n_norm = np.sqrt(sum(n**2))     
   
# Apply the formula as mentioned above 
# for projecting a vector onto the orthogonal vector n 
# find dot product using np.dot() 
proj_of_u_on_n = (np.dot(u, n)/n_norm**2)*n 
  
# subtract proj_of_u_on_n from u:  
# this is the projection of u on Plane P 
print("Projection of Vector u on Plane P is: ", u - proj_of_u_on_n)

"""
