# Testing assert keyword in python
from keyword import kwlist
from time import time

def main():
    """This is a main function"""
    try:
        var = input("Enter a string: ")
        assert var == "Rohan"
        print("The value var contains is: "+var)
    
    except(AssertionError,KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Exception occured: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" milli sec]")    