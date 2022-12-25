# Adding two matrices
import numpy as np

m1 = np.matrix([[1,2,3],
               [4,5,6],
               [7,8,9]])

m2 = np.matrix([[10,12,13],
               [14,15,16],
               [17,18,19]])

result = m1+m2

print("The resultant matrix is: ")
print(result)
