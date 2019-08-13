# Mathematical Functions

import numpy as np #np is a alias name

#rounding function
#np.around(array,decimal)
print("Round function in numpy : ")
a = np.array([1.0,5.55,123,0.567,25.234])
print(a)

print('\nArray after rounding : ')
print(np.around(a))
print(np.around(a, decimals = 1))
print(np.around(a, decimals = -1))


#floor() --> return the floor value
print('\nGiven values are : ')
x = np.array([-1.7,1.5,-0.2,0.6,10])
print(x)
print('\nAfter floor function :')
print(np.floor(x))

#np.ceil() --> return the ceiling value
print('\nGiven values are :')
x = np.array([-1.7,1.5,-0.2,0.6,10])
print(x)
print('\nAfter ceil function :')
print(np.ceil(x))


