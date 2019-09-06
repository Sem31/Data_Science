#data input and output

import pandas as pd
import numpy as np

#now read the file
print('read the file "Example" : ')
io = pd.read_csv('example')
print(io)
print('\nNOw save above data into the "data_put.csv" file and then read it : ')
#now the io data is put into another file
io.to_csv('data_put.csv',index=False)
df = pd.read_csv('data_put.csv')
print(df)


#now read the Excel file
excel = pd.read_excel('Excel_Sample.xlsx', sheet_name = 'Sheet1')
print(excel)
