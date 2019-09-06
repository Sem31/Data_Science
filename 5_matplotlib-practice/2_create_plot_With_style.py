#using -- and *to create a plot line

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6)
y = x*2

a = plt.subplot(1,2,1) 
a.plot(x,y,'r--')
plt.show()

b = plt.subplot(1,2,2)
b.plot(y,x,'b*-')
plt.show()
