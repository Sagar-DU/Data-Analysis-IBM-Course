import numpy as np

a = np.array([0, 1, 3, 4, 5, 6])
print (type(a))

for index, count in enumerate(a):
    print("a[", count, "] = ", a[index])

print (np.__version__)