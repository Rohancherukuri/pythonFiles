# Solving tiling problem using recurssion in python
from time import time

def tilingWays(n):
    """This function computes the total possible ways for filling the tiles"""
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return tilingWays(n-1) + tilingWays(n-2)

def main():
    """This is a main function"""
    col = int(input("Enter the columns of the tile: "))
    ans = tilingWays(col)
    print("The total possible ways to fill the tile is: "+str(ans))

if __name__ == "__main__":
    try:
        t1 = time()
        main()    
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error ni your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" milli sec]")