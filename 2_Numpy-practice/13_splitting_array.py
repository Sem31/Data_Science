#Splitting array

import numpy as np
a = np.arange(9)
print(a)
print("Splitting the array in 3 equal-sized subarrays.")
b = np.split(a,3)
print(b)

#  In this the subarray is start with the given split data
print("\nSplit the array at position indicated in 1-D array.")
c = np.split(a,[1,4,7])
print(c)

#hsplit --> horizontal splitting
a = np.arange(16).reshape(4,4)
print(a)
print('\nHorizontal splitting :')
b = np.hsplit(a,2)
print(b)

#vsplit --> vertical splitting
print('\nVertical splitting :')
b = np.vsplit(a,2)
print(b)


