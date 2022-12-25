# Converting a list into dictionary in python
from time import time

def main():
    """This is a main function"""
    lst = [eval(i) for i in input("Enter the elements into the list: ").split(",")]
    # Creating an empty dictionary
    d = {}
    # Iterating over the list
    for i in range(len(lst)):
        d[i+1] = lst[i]
    print("The dictionary obtained is: "+str(d))

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
