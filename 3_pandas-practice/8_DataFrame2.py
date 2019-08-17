#data frame 2

import numpy as np
import pandas as pd

#conditional selection
print('Conditional selection on the dataframe :')
print('\ndata frame :')
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index = ['a','b','c'],columns = ['col1','col2','col3'])
print(df)

print('grater than 3 from given data frame :')
print(df[df>3])

print('print the even no. from the given data frame : ')
print(df[df%2 == 0])

print('print the column1 is greater than 3 data :')
print(df[df['col1'] < 3])

print('\n\nReset the index : ')
print(df)
print('reset_index() : ')
print(df.reset_index())

print('set_index(column_name)')
print(df)
newid = "ind uk usa".split()
df['data'] = newid
print(df)
print('now set the index ,data into the index :')
print(df.set_index('data'))
