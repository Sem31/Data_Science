#some exercises

#import numpy as np
import numpy as np

#create an array of 10 zeros
zero = np.zeros(10)
print(zero)

#create an array of 10 ones
one = np.ones(10)
print(one)

#create an array of 10 fives
five = np.ones(10)*5
print(five)

#create an array of the integers from 10 to 50 
arr = np.arange(10,51)
print(arr)

#create an array of the all even no. from 10 to 50
arr = np.arange(10,51,2)
print(arr)

#create an 3x3 matrix with values ranging from 0 to 8
arr = np.arange(9).reshape(3,3)
print(arr)

#create a 3x3 identity matrix
arr = np.identity(3)
print(arr)

#use NumPy to generte a random number between 0 to 1
arr = np.random.rand(1)
print(arr)

#use NumPy to generate an array of 25 random no. sampled from a standard normal distribution
arr = np.random.randn(25) #randn() return the standard normal numbers
print(arr)

#create a matrix to print all no. between 0 to 1,decimal values also
arr = np.arange(1,101).reshape(10,10)/100 #first way
print(arr)
arr = np.linspace(0.01,1,100).reshape(10,10)
print(arr)

#create an array of 20 linearly spaced points between 0 and 1
arr = np.linspace(0,1,20)
print(arr)

#NumPy Indexing and Selection

#given matrix
mat = np.arange(1,26).reshape(5,5)
print(mat)

#indexing
print(mat[2:,1:])

#print 20
print(mat[3,4])

print(mat[:3,1:2])

print(mat[4,0:])

print(mat[3:,0:])


#print the sum of all values in mat
print(mat.sum())

#get the standard deviation of the values in mat
print(mat.std())

#get the sum of all the columns in mat
print(mat.sum(axis = 0))





