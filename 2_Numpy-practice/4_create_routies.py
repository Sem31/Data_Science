# Numpy arrays can be created in different ways .

import numpy as np

# empty(shape_of_array, dtype)
print("Empty methods in numpy")
a = np.empty([2,2], dtype = int)
print(a)

# zeroshape, dtype)
print("\nZeros methods in numpy.")
b = np.zeros([2,2], dtype = int)
print(b)

# ones(shape,dtype)
print("\nOnes methods in numpy.")
c = np.ones([2,2], dtype = int)
print(c)

#arange(value,<start><stop><step>)
print("\narange method in numpy")
x = np.arange(10)
print(x)
y = np.arange(0,10)
print(y)
z = np.arange(0,10,2)
print(z)

# eye(N,M,K=0,dtype)
print("\nEye N = number,M = column,k=index of the diagonal,dtype =int")
d = np.eye(3,3,k=0,dtype = int)
print(d)

# identity(n,dtype)
print("\nIdentity (n,dtype) method use for diagonal.")
f = np.identity(4,dtype = int)
print(f)

# mat(data,dtype)
print("\nmat(data,dtype) method for create arrya.")
g = np.mat([(1,2,3),(4,5,6),(7,8,9)], dtype = int)
print(g)

# asmatrix(x)
print("\nprint matrix via a asmatrix method")
x = np.array([[1,2],[3,4],[5,6]])
y = np.asmatrix(x)
print(y)
print("\nthere type is normal array : ",type(x))
print("\nthere type is when we use asmatrix : ",type(y))

#full(shape,fill_value)
print("\nfull(shape,fill_value) method for full fill with same itme")
x = np.full(shape=(2,3), fill_value=7)
print(x)

#asarray(data,dtype)
print('\nasarray(data,dtype) use for create array but its works for all list,tuple,dict..')
x  = np.arange(12).reshape(3,4)
print(x)
print("\ncreate via a asarray() method...")
y  = np.asarray(x)
print(y)


#create a random array
print("\nprint the random array :")
a = np.random.rand(4,3)
print(a)
