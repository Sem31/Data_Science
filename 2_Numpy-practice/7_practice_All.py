# practice the all thing we do..

# import the module
import numpy as np

#create array
arr = np.arange(12).reshape(3,4)
print(arr)

#dimension
print(arr.ndim)

#type
print(type(arr))

#reshape
print(arr.reshape(4,3))

#all ones array
print(np.ones(12).reshape(3,4))

#all zeros array
print(np.zeros(12).reshape(3,4))

#empty array
print(np.empty(12).reshape(3,4))

#diagonal of 1 array
print(np.eye(3))

#random array
print(np.random.rand(12).reshape(3,4))

# Access the element from the 1-D array

arr1 = np.arange(10)
print(arr1)

#access the 5 element from the array
print(arr1[5])

#condition array print all grater value of the 5
print(arr1[arr1>5])

#Access the element from the 2-D array

arr2 = np.arange(12).reshape(3,4)
print(arr2)

#access the 5 no. from the array
print(arr2[1][1])

#access the element via different way
print(arr2[1,1])

#access the element 1st and 2nd row and 2nd and 3rd column data
print(arr2[:2,1:3])

