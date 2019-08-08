import numpy as np
a = []

n = int(input("Enter the no. you want the matrix : "))

for i in range(n):
	k = int(input("enter the no. :"))
	a.append(k)

if (len(a) == 12):
	arr = np.array(a).reshape(3,4)
	print(arr)
elif(len(a) == 24):
	arr = np.array(a).reshape(3,4,2)
	print(arr)

