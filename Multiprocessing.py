# Multiprocessing in python

import time
from multiprocessing import Pool

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * 1
    return s

if __name__ == "__main__":
    p = Pool()
    numbers = range(5)
    result = p.map(sum_square,numbers)
    print(result)
    p.close()
    p.join()