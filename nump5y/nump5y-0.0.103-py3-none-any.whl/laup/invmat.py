Ans="""

import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
test =  np.linalg.det(m)
if test>=0:
    result =  np.linalg.inv(m)
    print("Inverse of the said matrix:")
    print(result)
else:
    print("Inverse of the said matrix not possible!")

"""
