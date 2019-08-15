#DataFrame operations part-1

import pandas as pd
import numpy as np

#column operations

#1- selection column
print('Selection of column in this Data frame:')
x = {'one':pd.Series([1,2,3],index = ['a','b','c']),'two' : pd.Series([9,8,7,6],index = ['a','b','c','d'])}
df = pd.DataFrame(x)
print('Data Frame :')
print(df)
print('Select one column : ')
print(df['one'])

#2- Adding column
print('\nAdding column in this dataframe : ')
print(df)
df['three'] = pd.Series([5,6,7,8],index = ['a','b','c','d'])
print('added the third column : ')
print(df)
print('\nadd fourth column is that sum of the one and three :')
print(df)
df['four'] = df['one']+df['three']
print('added the four column is [one+three] :')
print(df)

#3- Deleting column
print('\nDeleting the column from the Data Frame :')
df1 = df
print(df1)
print('del() for delete the thrid column : ')
del(df1['three'])
print(df1)
print('also use the pop() for delete the two column :')
df1.pop('two')
print(df1)



#row operations

print('\n\n Row operations :')

#1- selecting rows
print('selecting the rows from the Data frame :')
arr = {'one':pd.Series([1,2,3,4],index=['a','b','c','d']),
	'two':pd.Series([9,8,7],index=['a','b','c'])}
print('Data frame is :')
df = pd.DataFrame(arr)
print(df)
print('Selecting row using loc function ..print the data of row "b" : ')
print(df.loc['b'])
print('Selecting row using iloc(interger location) function ..print the data of row 3rd using indexting : ')
print(df.iloc[2])

#2- Adding Row
print('\nAdded the new row  in this data frame:')
print(df)
newRow = pd.DataFrame([[6,5]],index = ['e'],columns = ['one','two'])
df = df.append(newRow)
print('Added the row "e" :')
print(df)

#3- slicing rows
print('\nSlicing the rows in the Data frame for see there data : ')
print(df)
print('print the rows b,c,d : ')
print(df[1:4])

#4- Deleting the rows
print('\nDeleting the rows in given data frame :')
print(df)
print('delete the "d" row from the data frame using the drop() : ')
print(df.drop('d'))

