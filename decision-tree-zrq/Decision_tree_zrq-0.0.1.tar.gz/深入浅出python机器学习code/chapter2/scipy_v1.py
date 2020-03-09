import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix
#eye函数生成一个6行6列的对角矩阵
#矩阵对角线上的元素为1，其余为0
matrix=np.eye(6)
#np数组转化为csr格式的SciPy稀疏矩阵sparse_matrix
#sparse函数只会存储非0元素
sparse_matrix=sparse.csr_matrix(matrix)
print("对角矩阵：\n{}".format(matrix))
#打印对角矩阵
print("\nsparse存储的矩阵：\n{}".format(sparse_matrix))

