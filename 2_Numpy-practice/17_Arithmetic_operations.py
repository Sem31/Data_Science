#Arithmetic Operations

import numpy as np

#np.add()
print("Add the two array : ")
a = np.arange(9).reshape(3,3)
print('\nfirst array : ')
print(a)
b = np.array([10,20,30])
print('\nsecond array : ')
print(b)
print("\narray after adding : ")
print(np.add(a,b))

#np.subtract()
print("\nAfter array subtracting :")
print(np.subtract(b,a))

#np.multiply()
print('\narray after multiplying :')
print(np.multiply(a,b))

#np.divide()
print('\narray after dividing :')
print(np.divide(a,b))

#np.power()
print('\nPower : ')
a = np.array([10,100,1000])
print(a)
print('\narray after applying power function :')
print(np.power(a,2))

#np.mod()
a = np.array([10,20,30])
b = np.array([3,5,7])
print('\narray a : ')
print(a)
print('\narray b : ')
print(b)
print('\narray after applying mod function : ')
print(np.mod(a,b))
