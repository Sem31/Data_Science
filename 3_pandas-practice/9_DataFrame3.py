#data frame 3

import numpy as np
import pandas as pd

#zip uses and shows the index Hierarchical
print('zip uses : ')
groups = ['G1','G1','G1','G2','G2','G2']
level = [1,2,3,1,2,3]
zip_data = list(zip(groups,level))
zip_data = pd.MultiIndex.from_tuples(zip_data)
print('column data :',groups)
print('index : ',level)
print("column and index into zip : \n",zip_data)

#create a dataframe in the form of index hierarchical
df = pd.DataFrame([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]],zip_data,['A','B'])
print(df)
df.index.names = ['Groupes','num']
print(df)
print('print the value 10 from the given dataframe :')
print(df.loc['G2']['B'][2])
print('print the G1 data using cross section(xs) method :')
print(df.xs('G1'))
