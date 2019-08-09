#Acessing the element from the 2-D array

import numpy as np

arr = np.arange(9).reshape(3,3)
print("array is :")
print(arr)

#first way to access the element form the array
print('\nAccess the element from array like arr[0][2] -> 0 in row and 2 is col')
print(arr[0,2])

#second way to access the element from the array
print("\nAccess the element from array like arr[1,2] also in row and col.")
print(arr[1,2])

#third way access the element from the array
print("\nNow we access the complete row and there col using the slicing way. arr [1:3,1:]")
print(arr[1:3,1:])
