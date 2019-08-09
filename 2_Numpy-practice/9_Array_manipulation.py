#Array Manipulation

import numpy as np

arr = np.arange(12).reshape(3,4)
print(arr)

# ravel(array,order) --> returns a flat array
print("\nBefore using ravel function")
print(arr)
print("\nafter applying ravel")
print(arr.ravel())

#Transpose(array, axes)

print("\nArray after transpose :")
print(arr)
print("\nArray before transpose :")
print(np.transpose(arr))
print("\nTranspose by second way :")
print(arr.T)

#axis --> axis to roll backward,rolls axis 2 to 0,start --> zero by default

y = np.arange(12).reshape(2,3,2)
print('\nBefore array : ')
print(y)
print("\nArray arr after applying rollaxis :")
print(np.rollaxis(y,2)) 
print(np.rollaxis(y,2,1))

#swapaxes(array, axis1,axis2) --> interchange the axes of an array
print('\nSwapaxes(array, axis1, axis2) :')
a = np.arange(8).reshape(2,2,2)
print(a)
print("\narray after swapping the axes : ")
print(np.swapaxes(a,2,0))

