#part-2 Data Frame operations

import pandas as pd
import numpy as np

print('Create a dataFrame : ')
df = pd.DataFrame([[1,2],[3,4],[5,6]],index = ['x','y','z'],columns = ['a','b'])
print(df)

#pipe(functions,series)
#adding a value 2 to all the elements in the dataframe

def adder(ele1,ele2) :
	return ele1 + ele2

def multi(ele1,ele2):
	return ele1 * ele2

print('\nAdding a value 2 to all elements in given dataframes : ')
print(df)
df2 = df.pipe(adder,2)
print('\nAdded dataFrame : ')
print(df2)
print('\nMulti dataframe : ')
df3 = df.pipe(multi,10)
print(df3)


#apply() 
#displaying the mean value column wise using apply()
print('\nGiven DataFrame find mean value column wise using apply() : ')
print(df)
print('\napply() : ')
df2 = df.apply(np.mean)
print(df2)

print('\nGiven DataFrame find mean value row wise using apply() : ')
print(df)
print('\napply() : ')
df2 = df.apply(np.mean,axis = 1)
print(df2)

print('\nGiven DataFrame find max and min columns using apply() : ')
print(df)
print('\napply() : ')
df2 = df.apply(lambda x : x.max() - x.min()) #column wise
print(df2)

print('\nGiven DataFrame find max and min row using apply() : ')
print(df)
print('\napply() : ')
df2 = df.apply(lambda x : x.max() - x.min(),axis = 1) #row wise
print(df2)


#applymap()
print('\nGiven DataFrame : ')
print(df)
print('\nMap() function : ')
df2 = df['a'].map(lambda p : p*10)
df3 = df['a'].map(lambda p : p*10)
print(df2)
print(df3)

print('\napplymap() function :')
df4 = df.applymap(lambda p :p*10)
print(df4)

#multiply
print('\nMultiply each row of the dataframe bt different no. :')
df2 = df.mul([10,100])
print(df2)

#add
print('\nGiven data Frame :')
print(df)
print('add the column with [10,20] axis 1:')
print(df.add([10,20],axis=1))
print('add the row with [10,20] axis 0:')
print(df.add([10,20,30],axis =0))

#multiple the two data frame
print('\nmultiply two dataframes :')
df1 = pd.DataFrame([[1,2],[3,4]],index = ['a','b'],columns = ['col1','col2'])
print('first data frame is :')
print(df1)
df2 = pd.DataFrame([[1,2],[3,4]],index = ['a','b'],columns = ['col1','col2'])
print('second data frame is :')
print(df2)
print('multiply the first and second data frame is : ')
print(pd.np.multiply(df1,df2))


#create the dataframe
print('\n\ncreate the dataframe : ')
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns = ['col1','col2','col3'])
print(df)
print('shape : ',df.shape)
print('size : ',df.size)
print('length : ',len(df.index))
print('display the columns name : ',df.columns.values)
print('display the row name : ',df.index.values)

#indexing
print('iloc (integer location to track data) [0][1] :',df.iloc[0][1])
print('loc (direct location we give it) [0][1] :',df.loc[0][1])
print('loc[1]["col2"] in this first one is row and second one is column name to access the data : ',df.loc[1]['col2'])
print('at[1,"col2"] in this first one is row and second one is column name to access the data : ',df.at[1,'col2'])

#selection the particular row 
print('\nselecting the particular row : ')
print('2nd row to print :')
print(df.iloc[2])
print('\nselecting the particular column :')
print('col2 column to print :')
print(df.loc[:,'col2'])



#set_index() to our column to index
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns = ['col1','col2','col3'])
print('\n\nDataFrame is :')
print(df)
print('Now we make the col3 to our index :')
df1 = df.set_index('col3')
print(df1)

#add the column in the dataframe
print('\n Now we add the column in this data frame :')
print(df1)
print('added the column is "col4" : ')
df1['col4'] = np.array([5,3,1])
print(df1)

#reset the index
print('\nNow we reset the index of this data frame :')
print(df1)
print('reset the index see : ')
df2 = df1.reset_index(level = 0,drop = True)
print(df2)
