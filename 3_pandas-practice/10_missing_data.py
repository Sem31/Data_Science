#missing Data

import numpy as np
import pandas as pd

d = {'one':pd.Series([1,2,3,4],['a','b','c','d']),'two':pd.Series([10,20,30],['a','b','d'])}
df = pd.DataFrame(d)
print(df)

#add the new column
print('added the new column third :')
df['Third'] = pd.Series([12,13,np.nan],['a','b','c'])
print(df)

#dropna() any missing value find
print("drop the NaN value rows :")
print(df.dropna())
print("drop the NaN value columns :")
print(df.dropna(axis = 1))

#thresh in the dropna()
print('thresh the 2 NaN value using dropna() rows : ')
print(df.dropna(thresh = 2))

#fill the missing value using fillna()
print('fillna() for fill the NaN values to 0 see : ')
print(df.fillna(0))
