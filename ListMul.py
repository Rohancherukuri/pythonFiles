# Multiplying two lists
import numpy as np

def var(x,f):
    i=0
    l3 = []
    for i in range(0,len(x)):
        l3.append(x[i]*f[i])
    return l3
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5]
    f = [0.09, 0.15, 0.40, 0.25, 0.10, 0.01]
    v = var(x,f)
    print("The multiplication of two lists is: {}".format(v))
    print("The mean of x and f(x) is: {}".format(np.sum(v)))