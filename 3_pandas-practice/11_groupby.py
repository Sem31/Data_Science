#GroupBy in the data frame

import numpy as np
import pandas as pd

data = {'company' : ['Google','Google','Insta','Insta','FB','FB'],
	'person' : ['sem','vishal','kamlesh','Amy','Rohit','Aman'],
	'Sales' : [200,120,400,600,100,220]}
df = pd.DataFrame(data)
print('Data Frame : ')
print(df)

print('\n\n GroupBy the column of company and find the mean :')
groups = df.groupby('company')
print(groups.mean())
print('\nfind sum : ')
print(groups.sum())

print('find the particular company sum like FB : See')
print(df.groupby('company').sum().loc['FB'])

print('count the instances : ')
print(groups.count())
print('print the max :')
print(groups.max())
print('print the min :')
print(groups.min())

print(df.groupby('company').describe().transpose()['FB'])
