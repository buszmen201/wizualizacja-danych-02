import numpy as np

zero = np.zeros((5, 5))
print(zero)

diagonalna = np.diag([1, 2, 3, 3, 4])
diagonalna2 = np.diag([1, 2, 3, 3], k=-1)
diagonalna3 = np.diag([2, 3, 4, 5], k=1)
print(zero + diagonalna2+diagonalna+diagonalna3)

