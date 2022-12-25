# Finding the minimum and maximum element present in the list
import time as tm
import sys
start_time = tm.time()

def find_min_element(l):
    min = sys.maxsize
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min

def find_max_element(l):
    max =  -sys.maxsize
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max
    
if __name__ == "__main__":
    try:
        mylist = [int(i) for i in input("Enter the elements into the list: ").split(",")]
        f1 = find_min_element(mylist)
        f2 = find_max_element(mylist)
        print("The minimum element present in the list is: {}".format(f1))
        print("The maximum element present in the list is: {}".format(f2))
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        finish_time = tm.time() - start_time
        print("Finished in: {} sec".format(finish_time))
        