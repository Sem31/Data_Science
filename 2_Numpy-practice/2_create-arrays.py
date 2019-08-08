# creating 1-D array using Numpy

import numpy as np
print("1-D Array...\n")
	# arange use for range
print("using arange method")
arr = np.arange(10)
print(arr)
print('there dimension : ',arr.ndim)
print('there type : ',arr.dtype)			
	#also create by using array method
print("\nusing array method.")
arr1 = np.array([1,2,3,4])
print(arr1)

#creating 2-D array using Numpy
print("\n\n2-D array...")
	#it contains rows and cols
print("\nthere are row = 3 and col = 4")
arr2 = np.arange(12).reshape(3,4)
print(arr2)
print('there dimension : ',arr2.ndim)
print('there type : ',arr2.dtype)			


	#we also write like this in case row is 4 and cols is 3
print("\nthere are row = 4 and col = 3")
arr3 = np.arange(12).reshape(4,3)
print(arr3)

#creating 3-D array using Numpy
print("\n\n3-D array")

print("\nthere are row = 3, col = 4")
arr4 = np.arange(24).reshape(3,4,2)
print(arr4)
print('there dimension : ',arr4.ndim)
print('there type : ',arr4.dtype)			
