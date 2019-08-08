import numpy as np

list_data = [1,2,3,4]
arr = np.array(list_data)
print("print 1-D arry :\n ",arr)
arr = np.array(list_data).reshape(2,2)
print("NOw print reshape array :\n ",arr)
