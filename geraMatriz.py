import numpy as np
from scipy.sparse import csc_matrix


  
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 2, col = 3
array = np.random.randint(10, size=(3, 3))
print(array)

sparseMatrix = csc_matrix((array), shape = (3, 3)).toarray() 
print(sparseMatrix)