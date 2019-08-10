# Broadcast the array

import numpy as np
x = np.array([[1],[2],[3]])
y = np.array([4,5,6])
b = np.broadcast(x,y)
print(b)
print(b.shape)

#np.braodcast to (array,shape) -> broadcasts an array to a new shape

a = np.arange(4).reshape(1,4)
print('\nArray :')
print(a)
print("\nBroadcast the array : ")
print(np.broadcast_to(a,(4,4)))


#squeeze ---> remove one-dimensional entry from the shape of the given array

x = np.arange(9).reshape(1,3,3)
print("\nX Array :")
print(x)
y = np.squeeze(x)
print("\nsqueeze Y Array : ")
print(y)

print("\nX Array : ")
print(x.shape)
print('\nY Array : ')
print(y.shape)
