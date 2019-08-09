#indexing 1-D array

import numpy as np

a = np.arange(1,11)
print(a)

print("\nAccess first 5 element")
print(a[0:5])
print(a[:5])
print("\nAccess last 5 element")
print(a[5:10])
print(a[5:])
print("\nAccess 3 to 8 element")
print(a[3:8])

#broadcast the value see
print("\nBroadcast means we change the value from all the way from array is created")
print('\nBefore the Broadcast this array see.')
b = np.arange(1,11)
c = b[0:5]
print("this is array b :\n",b)
print("this is array c :\n",c)
print('\nAfter the Broadcast array of C')
c[:] = 100
print("this is broadcasted array c :\n",c)
print("array b is automatically broadcast via c : \n",b)
