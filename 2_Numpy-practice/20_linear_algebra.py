#Linear Algebra

import numpy as np

#dot() --> return the dot product of the two array 
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print('Array a:\n',a,'\nb :\n',b)

print('\nDot product is :\n',np.dot(a,b))

#vdot() --> return dot product of two vectors
print('\nVector dot product of array :\n',np.vdot(a,b))

#inner() --> return inner product of two array
print('\nInner product of array :\n',np.inner(a,b))

#matmul() --> return matrix product of two arrays
import numpy.matlib
print("\narray is :")
a = [[1,0],[0,1]]
print(a)
b = [[4,1],[2,2]]
print(b)
print('\nmatrix product using matlib :\n',np.matmul(a,b))
print('\nmatrix product using dot :\n',np.dot(a,b))

#determinant() --> computes the determinant of an array
a = np.array([[1,2],[3,4]])
print('\narray is :\n',a)
print('\ndeterminant of array :\n',np.linalg.det(a))
b = np.array([[6,1,1],[4,-2,5],[2,8,7]])
print(np.linalg.det(b))

#inv() --> finds the inverse of the matrix
x = np.array([[1,2],[3,4]])
print('\narray is :\n',x)
print('\ninverse determinant of array is :\n',np.linalg.inv(x))


