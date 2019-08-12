#Adding and removing elements

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)

b = np.resize(a,(3,2))
print(b)
print(b.shape)

#observe that the first row of a is repeated in b since the size is bigger
print('\nResizing the second array : ')
b = np.resize(a,(3,3))
print(b)
print('\nResize the array : ')
c = np.array([[1,2,3]])
print(c)
w = np.resize(c,(3,3))
print(w)

# append(array,values/elements,axis) --> append the values to the end of array
a = np.array([[1,2,3],[4,5,6]])
print(a)
print('\nAppend elements to array : ')
print(np.append(a,[7,8,9]))
print('\nAppend elements along axis 0 :')
print(np.append(a,[[7,8,9]],axis = 0))
print('\nAppend elements along axis 1 :')
print(np.append(a,[[5,5,5],[7,8,9]],axis = 1))

#Insert(array,obj,values,axis) --> insert the values along a given axis
#obj --> The index before which insertion is to be made

a = np.array([[1,2],[3,4],[5,6]])
print(a)

print('\nAxis parameter not passed so the input array is flattened before insertion : ')
print(np.insert(a,3,[11,12]))

print('\nAxis parameter passed. the values array is broadcast to match input array : ')
print('\nBroadcast along axis 0 :')
print(np.insert(a,1,[11],axis = 0))

print('\nBroadcast along axis = 1 :')
print(np.insert(a,1,11,axis = 1))

#  np.delete(array,obj,axis)
# obj --> can be a slice, integer or array of integers

print('\nUnique values of array a : ')
a = np.arange(12).reshape(3,4)
print(a)


print(np.delete(a,5))

print('\nColumn 2 deleted : ')
print(np.delete(a,1,axis = 1))

#np.unique(arr, reture_index, return_inverse, return_counts)
a = np.array([5,4,3,2,3,11,4,2,5])
print(a)
print('\nUnique values of array a : ')
u = np.unique(a, return_index = True)
print(u)

print('\nUnique array and Indices array : ')
u,indices = np.unique(a,return_index = True)
print(indices)

print('\nIndices of unique array : ')
u,indices = np.unique(a,return_inverse = True)
print(u)
print('\nIndices are : ')
print(indices)

print('\nreconstructing the original array using indices : ')
print(u[indices])
print('\nreturn the count of repetition of unique element : ')
u,indices = np.unique(a,return_counts = True)
print(u)
print(indices)
