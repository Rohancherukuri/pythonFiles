from MatrixRoatation import MatrixOperations
from time import time


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Enter the elements into the matrix: ")
    matrix = [[int(j) for j in input().split(",")] for i in range(rows)]
    print("The original matrix is: "+str(matrix))
    mo = MatrixOperations()
    mo.matrix_rotate(matrix, rows, cols)

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")