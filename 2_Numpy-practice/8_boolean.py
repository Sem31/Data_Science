#Boolean

import numpy as np

a = np.arange(12).reshape(3,4)
print(a)
print("even : ",a[a%2==0])
print("odd  : ",a[a%2!=0])
print("boolean : \n",a>5)



