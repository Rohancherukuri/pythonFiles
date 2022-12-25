# Searching the element linearly

from time import time
import numpy as np
import random

def search(l,key):
    isFound = False
    for i in l:
        if i == key:
            print("Found")
            isFound = True
            break
    if isFound == False:
        print("Not found")

def main():
    l = list(range(100))
    random.shuffle(l)
    key = int(input("Enter the key to be searched: "))
    search(l,key)

if __name__ == "__main__":
    try:
        t1 = time()
        main()

    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))

    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")


