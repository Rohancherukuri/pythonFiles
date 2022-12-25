import numpy as np
from timeit import Timer
from sys import getsizeof

n_elements = 100000
mylist = [i for i in range(n_elements)]
print("The memory size taken by the list is: {} bytes".format(getsizeof(mylist)))

arr = np.array(mylist)
print("The memory size taken by the array is: {} bytes".format(getsizeof(arr)))

result = getsizeof(mylist) - getsizeof(arr)
print("The array takes {} bytes lesser than list".format(result))