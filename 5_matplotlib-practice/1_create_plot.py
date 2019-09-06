#creating plots in matplotlib

import matplotlib.pyplot as plt

import numpy as np

x = np.arange(10)
y = x*2

#x for x-axis and y for y-axis and r is for color
plt.plot(x,y,'r')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.show()
