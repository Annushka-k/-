import numpy as np
def fun(yi1, yi2):
    yi1 = np.array(yi1)
    yi2 = np.array(yi2)
    mse = np.mean((yi1 - yi2) ** 2)
    return mse
print(fun([5, 6, 7], [8, 9, 10]))
