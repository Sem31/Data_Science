#Create a series using pandas

#import the pandas library
import pandas as pd #pd is a alias name

#what the syntax of the series see..
print("Series syntax :\n",pd.Series())

print('create a Series using pandas : ')
#pd.Series(array,index)
a = pd.Series([1,2,3,4]) #by default index is 0,1,2... so on
print(a)

print('\ncreate a Series using own index : ')
b = pd.Series([1,2,3,4],index = ['a','b','e','d'])
print(b)

print('\nCreate a Series using the Dictionary object : ')
dict1 = {'a':1,'b':2,'c':3,'d':4}
print("\nDictionary : ",dict1)
data = pd.Series(dict1)
print('Series :')
print(data)

print('\nAny one nan value then all data convert into float see ..:')
dict1 = {'a':1,'b':2,'c':3,'d':4}
print(dict1)
print('Series :')
print(pd.Series(dict1,index = ['e','f','a','b','c','d']))

#access the series data using slicing
print('\nSeries')
a = pd.Series([1,2,3,4]) #by default index is 0,1,2... so on
print(a)
print('first[0] values : ',a[0])
