#shapes and reshapes

import numpy as np

print("create a array :")
x = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(x)
print('\nthere dimensions :',x.ndim)


print('\nsahpe the matrix')
x.shape = [3,4]
print(x)

print('\nreshape the matrix')
y = x.reshape(2,6)
z = x.reshape(6,2)
print(y)
print(z)
print('there dimensions :',y.ndim)

print('\nsingle array create and check there dimension')
a = np.arange(10)
print(a)
print('there dimensions :',a.ndim)


