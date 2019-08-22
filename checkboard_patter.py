#checkboard pattern using numpy array

import numpy as np

arr = np.zeros((8,8),dtype = int)

arr[1::2,::2] = 1
arr[::2,1::2] = 1

print('Array is :')
print(arr)

print('\n checkboard form : ')
for i in range(8):
	for j in range(8):
		print(arr[i][j], end = " ")
	print()	

