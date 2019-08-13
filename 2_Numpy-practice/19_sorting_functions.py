#Sorting Functions

import numpy as np

#np.sort() --> return sorted values of the input array
#np.sort(array,axis,order)
print('Array :')
a = np.array([[3,7],[9,1]])
print(a)
print('\nafter applying sort function : ')
print(np.sort(a))
print('\nSorting along axis 0:')
print(np.sort(a,0))

#order parameter in sort function
dt = np.dtype([('name','S10'),('age',int)])
x  = np.array([('Ram',23),('Robert',25),('Rahim',27)], dtype = dt)
print('\nArray :')
print(x)
print('dtype : ',dt)
print('Order by name : ')
print(np.sort(x, order = 'name'))

#np.nonzero() --> returns the indices of the non-zero elements
b = np.array([[30,40,0],[0,20,10],[50,0,60]])
print('\narray b is :\n',b)
print('\nafter applying nonzero() function :')
print(np.nonzero(b))

#np.Where() --> returns the indices of elements when the condition is satisfied
x = np.arange(12).reshape(3,4)
print('\nArray is  :')
print(x)
print('Indices of elements >3 :')
y = np.where(x>3) #its just work like a sql query
print(y)

print('Use these indices to get elements statisfying the condition :')
print(x[y])

#np.extract() --> returns the elements satisfying any condition
x = np.arange(9).reshape(3,3)
print('\nArray : ')
print(x)

#define conditions
condition = np.mod(x,2) == 0
print('\nelement-wise value of condition :\n',condition)
print('\nextract elements using condition :\n',np.extract(condition, x))

