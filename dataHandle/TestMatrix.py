import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

for i in range(a.shape[0]):
    print(a[i].sum())
