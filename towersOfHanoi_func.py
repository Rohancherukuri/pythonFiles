# Implementing towers of hanoi in python
from time import time

def towersOfHanoi(n,src,dest,helper):
    """This moves disc from source to destination"""
    if n == 0: # base case
        return
    towersOfHanoi(n-1,src,helper,dest)
    print("The disc is moved from "+str(src)+" to "+str(dest))
    towersOfHanoi(n-1,helper,dest,src)
    
def main():
    """This is main method"""
    n = int(input("Enter number of discs to be moved: "))
    towersOfHanoi(n,"A","C","B")
    print()
    
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