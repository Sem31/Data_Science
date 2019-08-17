#series

import numpy as np
import pandas as pd

labels = ['a','b','c']
data = np.array([1,2,3])

#series
series = pd.Series(data,index = labels)
print(series)

d = {'a':1,'b':2,'c':3}
print(pd.Series(d))
print(d['b'])
