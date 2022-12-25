# Rotating a matrix by 90
from time import time

class MatrixOperations:
    """This is MatrixOperations class"""
    def matrix_rotate(self,m,rows,cols):
        """This is a matrix rotation function"""
        print("After Matrix rotation is: ")
        for i in range(rows-1,-1,-1):
            for j in range(cols):
                print(str(m[i][j])+"\t",end = " ")
            print()
            
    def minmax(self,m,rows,cols):
        """
            This is a function to find minimum and 
            maximum elements from the given matrix
        """
        minimum,maximum  = m[0][0],m[0][0]
        for i in range(rows):
            for j in range(cols):
                if m[i][j] < minimum:
                    minimum = m[i][j]
        
        for i in range(rows):
            for j in range(cols):
                if m[i][j] > maximum:
                    maximum = m[i][j]
        
        return minimum,maximum
    
    def matmul(self,m1,m2,rows,cols):
        """
            This method is to multiply two matrices 
            with same dimensions or shape
        """
        c = [[0,0,0],[0,0,0],[0,0,0]]
        if rows == cols:
            for i in range(rows):
                for j in range(cols):
                    for k in range(rows):
                        c[i][j] += m1[i][k] * m2[k][j]
            
            print("The resultant matrix is:")
            for i in range(len(c)):
                for j in range(len(c)):
                    print(str(c[i][j])+"\t",end = " ")
                print()
            
        else:
            print("Sorry could not perform multiplication operation!")
                    
        
    
    def matrix_shape(self,rows,cols):
        """This method returns the shape of the matrix"""
        shape = (rows,cols)
        print("The shape of the matrix is: "+str(shape))
        
        

def main():
    """This is a main function"""
    mo = MatrixOperations()
    print(mo.__doc__)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))
    print("Enter the elements into the first matrix: ")
    matrix = [[int(j) for j in input().split(",")] for i in range(rows)]
    print("Enter the elements into the second matrix: ")
    matrix2 = [[int(j) for j in input().split(",")] for i in range(rows)]
    print("Before Matrix rotation is: ")
    for i in range(rows):
        for j in range(cols):
            print(str(matrix[i][j])+"\t",end = " ")
        print()
    print("-"*25)    
    mo.matrix_rotate(matrix,rows,cols)
    m1,m2 = mo.minmax(matrix,rows,cols)
    print("\nThe minimum and maximum element from Matrix is: "+str(m1)+", "+str(m2)+"\n")
    mo.matrix_shape(rows,cols)
    print("\n")
    mo.matmul(matrix,matrix2,rows,cols)
    print()

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")
