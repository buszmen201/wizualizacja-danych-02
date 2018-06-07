import numpy as np

a = np.arange(0, 10, 0.1)

print("Tabliza a: \n", a)
b = a
print("\n\nTablica b:\n", b)

print("\n\n", a.dtype)
c = a.astype('int64')
print("\n\nTablica c:\n", c)