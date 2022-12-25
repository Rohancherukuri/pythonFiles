# Finding the min andmax elements of an array
from  numpy import array

arr = array([1,2,3,4,5,6,7,8])

def min_max(array):
    min = max = array[0]
    for i in range(len(array)):
        if min > array[i]:
            min = array[i]

    for i in range(len(array)):
        if max < array[i]:
            max = array[i]

    return min,max

output1,output2 = min_max(arr)
print(output1,output2)
m1 = min(arr)
m2 = max(arr)
print(m1,m2)
