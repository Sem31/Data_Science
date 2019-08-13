#Create a series using pandas

#import the pandas library
import pandas as pd #pd is a alias name

print('create a Series using pandas : ')
#pd.Series(array,index)
a = pd.Series([1,2,3,4]) #by default index is 0,1,2... so on
print(a)

print('\ncreate a Series using own index : ')
b = pd.Series([1,2,3,4],index = ['a','b','e','d'])
print(b)
