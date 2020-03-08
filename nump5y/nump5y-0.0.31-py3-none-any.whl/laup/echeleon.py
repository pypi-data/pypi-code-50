Ans="""
'''
A matrix is in reduced row echelon form (also called row canonical form) if it satisfies the following conditions:[3]

    It is in row echelon form.
    The leading entry in each nonzero row is a 1 (called a leading 1).
    Each column containing a leading 1 has zeros everywhere else.

'''
def row_mult(row,num):
return[x*num for x in row]
#subtract one row from another
def row_sub(row_left,row_right):
return[a-b for (a,b) in zip(row_left,row_right)]
#row_echelon ::Matrix->Matrix
def row_echelon(mtx):
temp_mtx=list(mtx)
def echelonify(rw,col):
for i,row in enumerate(temp_mtx[(col+1):]):
i+=1
if rw[col]==0:continue
temp_mtx[i+col]=row_sub(row,row_mult(rw,row[col]/r
w[col]))
for i in range(len(mtx)):
active_row=temp_mtx[i]
echelonify(active_row,i)
#flatten out values very close to zero
temp_mtx=[
[(0 if(0.0000000001>x>-0.0000000001)else x)
for x in row]
for row in temp_mtx
]
return temp_mtx
#accept input of square matrix
print('enter dimensions of matrix')
r=int(input('enter no of rows'))
c=int(input('enter no of columns'))
mtx=[]
mtx_result=[]
for i in range(r):
mtx.append([])
print('enter elements of row',i)
for j in range(c):
n=float(input('enter element'))
mtx[i].append(n)
print('entered matrix')
for row in mtx:
print(''.join(("{0:.2f}".format(x)for x in row)))
mtx_result=row_echelon(mtx)
print('Row Echelon form matrix')
for row in mtx_result:
print(''.join(("{0:.2f}".format(x)for x in row)))


"""
