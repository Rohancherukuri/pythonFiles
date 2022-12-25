# Finding minimum and maximum element in an matrix
from time import time
import numpy as np
from numba import jit
def main():
    """ Main function """
    matrix = [[4,1,7],[9,6,2],[12,3,8]]
    arr_matrix = np.matrix(matrix)
    m1 = find_min(arr_matrix)
    m2 = find_max(arr_matrix)
    print("The minimum element present in the matrix is: "+str(m1))
    print("The maximum element present in the matrix is: "+str(m2))

@jit(nopython = True)
def find_min(matrix):
    """ Function to find minimum element from the matrix """
    minimum = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] < minimum:
                minimum = matrix[i][j]
    return minimum

@jit(nopython = True)
def find_max(matrix):
    """ Function to find maximum element from the matrix """
    maximum = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
    return maximum

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")