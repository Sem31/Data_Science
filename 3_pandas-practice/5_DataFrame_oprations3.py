#part-3 DataFrame Operations

#removing and deleting duplicates indexs in dataframes

import pandas as pd
import numpy as np

print('Removing and deleting the duplicates indexes : ')
#drop_duplicates(subset = None,keep = 'first','last',False) 
print('Data frame : ')
df = pd.DataFrame({'userid':[1,1,1,2,3,3],'itemid' :[1,1,3,4,1,2]})
print(df)
print('Drop the duplicates in itemid : ')
print(df.drop_duplicates(subset = 'itemid'))
print('Drop the duplicates in userid : ')
print(df.drop_duplicates(subset = 'userid'))
print('drop the duplicates from complete data set : ')
print(df.drop_duplicates(subset = None))

#resetting the indexes
print('\n\nResetting the indexes :')
print('Given data set : ')
df1 = pd.DataFrame(data = np.array([[1,2,3],[4,5,6],[22,33,44],[12,13,14],[23,24,25]]),index = [2,3,4,2,5],columns = ['col1','col2','col3'])
print(df1)
print('reset the index : ')
df2 = df1.reset_index(level = 0)
print(df2)

#rename the column name
print('\nGiven data frame is that : ')
print(df1)
print('now we change the column name "col1" to "A" : ')
print(df1.rename(columns = {'col1':'A'}))
print('rename the multiple column : ')
print(df1.rename(columns = {'col1':'A','col2':'B','col3':'C'}))


#rename the rows name
print('\nGiven data frame is that : ')
print(df1)
print('now we change the row name 2 to "row1" : ')
print(df1.rename(index = {2:'row1'}))
print('rename the multiple rows : ')
print(df1.rename(index = {2:'row1',3:'row2',4 : 'row3',5:'row4'}))
