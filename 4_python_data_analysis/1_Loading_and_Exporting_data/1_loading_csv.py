#loading the csv and shows the data

#import pandas
import pandas as pd
#assign the location of csv file
location = 'data_sets/smallgradesh.csv'
print('read csv without header : ')
#read the file without headers
df = pd.read_csv(location,header = None)
print(df[0:5])

print('\n\nRead csv with header : ')
#read with header
df = pd.read_csv(location)
print(df.head()[0:5])


#try to import data from the file all_040_in_36.p1.csv into python
print('\n\nQ : try to import data from the file all_040_in_36.p1.csv into python ')

import pandas as pd
location = 'data_sets/all_040_in_36.P1.csv'
df = pd.read_csv(location)
print('\n')
print(df.head()[0:5])

