# String replacement using recussion in python
from time import time

def string_replacement(s):
    """This method replace the pi with 3.14"""
    if len(s) == 0: # base case
        return
    
    if s[0] == "p" and s[1] == "i":
        print("3.14",end = "")
        string_replacement(s[2:])
    
    else:
        print(s[0],end = "")
        string_replacement(s[1:])

def main():
    """This is main method"""
    s = input("Enter a string: ")
    string_replacement(s)
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
    
    