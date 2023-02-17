import numpy as np

base_1 = np.zeros((2,2,2))
base_2 = np.ones((2,2,2))
x = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            x += 1
            base_1[i][j][k] += x
            base_2[i][j][k] += x

base_3 = base_1 * base_2

print(base_3)