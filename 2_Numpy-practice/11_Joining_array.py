# Joining Array 

import numpy as np

a = np.array([[1,2],[3,4]])
print("Array a : \n",a)
b = np.array([[5,6],[7,8]])
print("Array b : \n",b)

c = np.concatenate((a,b))
print("concatenate the two array :\n",c)
c1 = np.concatenate((a,b),axis = 1)
print("concatenate the two array : \n",c1)

#stack(array,axis) --> joins sequece of array along a new axis

a = np.array([[1,2],[3,4]])
print("Array a : \n",a)
b = np.array([[5,6],[7,8]])
print("Array b : \n",b)

print("\nstacking two array along axis 0 :")
print(np.stack((a,b),0))
print("\nstacking two array along axis 1 :")
print(np.stack((a,b),1))

#hstack --> stacks array horizontally
a = np.array([[1,2],[3,4]])
print("Array a :\n",a)
b = np.array([[5,6],[7,8]])
print("Array b :\n",b)
c = np.hstack((a,b))
print("\nhstack(horizontal array) :\n",c)

#vstack --> stack array vertically
c = np.vstack((a,b))
print("\nvstack(vertical array :\n",c)

