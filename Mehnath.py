import numpy as np
s = {i for i in range(101) if i % 2 == 0}
#print(s)
print(type(s))
arr = np.array(s)
print(arr)
print(type(arr))