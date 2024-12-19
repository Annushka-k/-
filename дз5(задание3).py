import numpy as np
array = np.array(range(1, 101))
new = []
for i in array:
    if i % 2 == 0:
        new.append(i)
new = np.array(new)
sum = np.sum(new)
print(sum)