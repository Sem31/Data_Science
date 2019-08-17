#merging joining and Concatenating

import numpy as np
import pandas as pd

df = pd.DataFrame({'A' : ['A0','A1','A2','A3'],
		'B' : ['B0','B1','B2','B3'],
		'C' : ['C0','C1','C2','C3'],
		'D' : ['D0','D1','D2','D3']},index = [0,1,2,3])
df1 = pd.DataFrame({'A' : ['A4','A5','A6','A7'],
		'B' : ['B4','B5','B6','B7'],
		'C' : ['C4','C5','C6','C7'],
		'D' : ['D4','D5','D6','D7']},index = [4,5,6,7])
df2 = pd.DataFrame({'A' : ['A8','A9','A10','A11'],
		'B' : ['B8','B9','B10','B11'],
		'C' : ['C8','C9','C10','C11'],
		'D' : ['D8','D9','D10','D11']},index = [8,9,10,11])
print(df)
print(df1)
print(df2)

print('\n\nConcate the Df,df1,df2 : ')
print(pd.concat([df,df1,df2]))
print(pd.concat([df,df1,df2],axis = 1))

left = pd.DataFrame({'key' : ['k0','k1','k2','k3'],
		'A' : ['A0','A1','A2','A3'],
		'B' : ['B0','B1','B2','B3']})

right = pd.DataFrame({'key' : ['k0','k1','k2','k3'],
		'C' : ['C0','C1','C2','C3'],
		'D' : ['D0','D1','D2','D3']})
print('\n\nleft and right : ')
print(left)
print(right)

print('\n\nmerge left and right :')
print('\ninner merge :')
print(pd.merge(left,right,how = 'inner', on = 'key'))
#print('\nouter merge :')
#print(pd.merge(left,right,how = 'outer', on = ['key1','key2']))
#print('\nright merge : ')
#print(pd.merge(left,right,how = 'right', on = ['key1','key2']))

#joining two data frame

print('\n\n\nJoining : ')
print('left data frame :')
left = pd.DataFrame({'A' : ['A0','A1','A2'],
		'B' : ['B0','B1','B2']},index = ['k0','k1','k2'])
print(left)
print('\nRight data frame : ')
right = pd.DataFrame({'C' : ['C0','C2','C3'],
		'D' : ['D0','D2','D3']},index = ['k0','k2','k3'])
print(right)
print('\nJoin the left and right using inner join : ')
print(left.join(right))
