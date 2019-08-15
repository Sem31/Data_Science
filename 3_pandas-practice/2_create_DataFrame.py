#Now we understand with the DataFrame of pandas

#import pandas
import pandas as pd
import numpy as np

#syntax of the pandas 
print('Syntax : \n',pd.DataFrame())

#create DataFrame data with default index and column name
print('\nData frame : ')
arr = np.array([[1,2,3],[9,8,7]])
data = pd.DataFrame(arr)
print(data)

#create DataFrame with own index and own column name
print('\nData Frame with own index and column name : ')
arr = np.array([[1,2,3],[4,5,6]])
data = pd.DataFrame(arr,index=['a','b'],columns =['col1','col2','col3'])
print(data)

#create employee table see using list
print('\ncreate a list of emp :')
emp = [['sem',21],['kamlesh',19],['jaadu',21]]
data = pd.DataFrame(emp,index = ['emp1','emp2','emp3'],columns = ['name','age'])
print(data)

#create data frame using dictionary
print('\ncreate a data using dictionary : ')
dict1 = {'Name':['sem','kamlesh','vishal','shiv'],'Age':[21,22,19,24]}
print('dict is :',dict1)
print('DataFrame : ')
data = pd.DataFrame(dict1)
print(data)

#now in data any null value then
print('\ncreate a dictionary with null or nan value : ')
dict1 = {'Name':['sem',np.nan,'vishal',None],'Age':[21,22,np.nan,24]}
print('dict is :',dict1)
print('DataFrame : ')
data = pd.DataFrame(dict1)
print(data)

#create data frame using list on dict
print('\ncreate the data frame using list on dict :')
arr = [{'a':1,'b':2},{'a':3,'b':4,'c':5}]
print('list : ',arr)
print('data frame : ')
data = pd.DataFrame(arr)
print(data)

#create DataFrame using series
print('\nCreate a data frames using Series : ')
arr = {'one':pd.Series([1,2,3],index=['a','b','c']),'two' : pd.Series([6,4,3],['a','b','d'])}
print('dict data is  :',arr)
print('Data Frame is :')
data = pd.DataFrame(arr)
print(data)
