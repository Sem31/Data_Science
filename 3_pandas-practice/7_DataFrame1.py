#data frame 1

import numpy as np
import pandas as pd

#create a data frame
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index = ['a','b','c'],columns = ['col1','col2','col3'])
print(df)
print('col1 : \n',df['col1'])
print('col1,col2 : \n',df[['col1','col2']])
print('create a new column : ')
df['col4'] = pd.Series([10,20,30],['a','b','c'])
print(df)
print('add new column :')
df['new'] = df['col1'] + df['col4']
print(df)
print('drop new column : ')
#drop, axis =1 is not work when we don't use a inplace = True
df.drop('new',axis = 1, inplace = True)
print(df)

#row operation
print('\n\n\nRow access using "loc" and "iloc : "')
print(df)
print('print "a" using loc :')
print(df.loc['a'])
print('print "b" using iloc :')
print(df.iloc[1])
