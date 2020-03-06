Ans='''"""
"""
m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
m2=[[10,11,12,13],
    [14,15,16,17],
    [18,19,20,21]]
rmatrix=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            rmatrix[i][j]+=m1[i][k]*m2[k][j]
for r in rmatrix:
    print(r)
"""
def matmul():
    print("Enter Details For Matrix 1")
    m1=[]
    nrow=int(input("Enter no of rows"))
    ncol=int(input("Enter no of columns"))
    for i in range(nrow):
        m1.insert(i,[])
        for j in range(ncol):
            temp=int(input("Enter Element["+str(i)+"]["+str(j)+"]"))
            m1[i].append(temp)
    print("Enter Details For Matrix 2")
    m2=[]
    nrow=int(input("Enter no of rows"))
    ncol=int(input("Enter no of columns"))
    for i in range(nrow):
        m2.insert(i,[])
        for j in range(ncol):
            temp=int(input("Enter Element["+str(i)+"]["+str(j)+"]"))
            m2[i].append(temp)
    nrow=len(m1)
    ncol=len(m2[0])
    l1=[]
    for i in range(nrow):
        l1.append([])
        for j in range(ncol):
            l1[i].append(0)
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                l1[i][j]+=m1[i][k]*m2[k][j]
    for i in l1:
        print(i)
matmul()
"""
'''
