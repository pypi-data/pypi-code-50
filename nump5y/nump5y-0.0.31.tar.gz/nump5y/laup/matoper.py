Ans="""

import numpy as np
m=np.array([1,1,2],[2,6,7],[3,6,7])
print(m)
for i in range(0,3):
    print("Row"+str(i))
a=5
print(a*m)
print(m.transpose())
def iden(n):
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                print("1",sep=" ",end=" ")
            else:
                print("0",sep=" ",end=" ")
        print()
iden(4)
def matsym(m,n):
    for i in range(0,n):
        for j in range(0,n):
            if m[i][j]!=m[j][i]:
                return False
    return True
matsym(m)

"""
