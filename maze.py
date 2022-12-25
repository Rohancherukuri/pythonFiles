# Finding out the total possible ways of maze of size n x n
from time import time

def countPathsInMaze(n,i,j):
    """Thi function returns the total possible paths for a given maze"""
    if i == n - 1 and j == n - 1: # base case 1
        return 1
    if i >= n or j >= n: # base case 2
        return 0
    
    return countPathsInMaze(n,i+1,j) + countPathsInMaze(n,i,j+1)

def main():
    """This is a main function"""
    size = int(input("Enter the size of the maze (n x n): "))
    i = j = 0
    result = countPathsInMaze(size,i,j)
    print("The total number of possible paths in maze of size "+str(size)+" is: "+str(result))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" milli sec]")


    