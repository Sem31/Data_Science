#operations

import numpy as np
import pandas as pd

print('Data Frame : ')
df = pd.DataFrame({'col1' : [1,2,3,4],
		'col2' : [444,555,666,444],
		'col3' : ['abc','def','ghi','jkl']})
print(df)

#return the unique values
print('return the unique value from the col2 : ',df['col2'].unique()) 
print('return the number of unique value from the col2 : ',df['col2'].nunique()) 

print('count the value repeated in col2 : \n',df['col2'].value_counts())

print('\n\nCondition : ')
print('find the data which greater than 2 in col1 and equal to 444 in col2 : ')
print(df[(df['col1'] > 2) & (df['col2'] == 444)])

#apply(func) method

print('\n\n use of the apply method : ')
def times(x):
	return x*10

print('Now the apply method to print col1*10 :')
print(df['col1'].apply(times))

print('\nNow use the lambda function : ')
print(df['col1'].apply(lambda x : x*10))

print('\nremove the col1 : use drop')
print(df.drop('col1',axis = 1))

print('\nprint columns : ')
print(df.columns)
print('\nprint index : ',df.index)

print('sort_value in col2 : \n',df.sort_values('col2'))

#pivot_table(values,index,column)
print('\n\npivot_table : ')
print('\nData Frame : ')
df = pd.DataFrame({'A' : ['foo','foo','foo','bar','bar','bar'],
		'B' : ['one','one','two','two','one','one'],
		'C' : ['x','y','x','y','x','y'],
		'D' : [1,2,3,5,6,1]})
print(df)

print('\nNow perfrom the pivot_table(value,index,column) : ')
print(df.pivot_table(values = 'D',index = ['A','B'],columns =['C']))

