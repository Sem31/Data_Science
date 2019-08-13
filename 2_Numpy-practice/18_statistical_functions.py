#Statistical functions

import numpy as np

#np.amin() --> find the minimum
print('array : ')
x = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(x)
print('\nminimum value of array is :')
print(np.amin(x))
print('\namin() value along axis 1:')
print(np.amin(x,1))
print('\namin() value along axis 0:')
print(np.amin(x,0))

#np.amax() --> find the maximum
print('\nmaximum value of array is :')
print(np.amax(x))
print('\namax() value along axis 1:')
print(np.amax(x,1))
print('\namax() value along axis 0:')
print(np.amax(x,0))

#np.ptp() --> range[max-min]
print('\nptp value :')
print(np.ptp(x))

#np.percentile(array,p,axis)
#p --> percentile value between 0 to 100
print('\npercentile values :')
print("\n50th percentile : ",np.percentile(x,50)) #computer 50th percentile
print("\n100th percentile : ",np.percentile(x,100)) #computer 100th percentile

#np.average()
print('\naverage values are :')
print(np.average(x))
print('\nAverage of along axis 0 :',np.average(x,0))
print('\nAverage of along axis 1 :',np.average(x,1))

#np.std() --> standard values
print("\nstd values are :")
print(np.std(x))
print('\nstd of along axis 0 :',np.std(x,0))
print('\nstd of along axis 1 :',np.std(x,1))

#np.var()
print('\nvariance values are :')
print(np.var(x))
print('\nvariance of along are :',np.var(x,0))
print('\nvariance of along are :',np.var(x,1))


#np.mean()
print('\nmean values are : ')
print(np.mean(x))
print("\nmean of along axis 0 :",np.mean(x,axis = 0))
print("\nmean of along axis 1 :",np.mean(x,axis = 1))

#np.median()
print('\nmedian values are : ')
print(np.median(x))
print('\nmedian of along axis 0 :',np.median(x,0))
print('\nmedian of along axis 1 :',np.median(x,1))

