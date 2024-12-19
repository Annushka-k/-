import numpy as np
def fun(matrix1, matrix2):
    return matrix1.dot(matrix2)
print(fun(np.array([4, 4, 4]), np.array([[8], [3], [1]])))