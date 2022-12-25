# Implementing list rotation in python
import time as tm
start_time = tm.time()       
def list_left_rotation(l):
    size = len(l)
    temp =  l[0]
    for  i in range(size - 1):
        l[i] = l[i+1]
    l[size -1] = temp

def list_right_rotation(l):
    size = len(l)
    temp = l[size - 1]
    for i in range(size -1,-1,-1):
        l[i] = l[i-1]
    l[0] = temp

def d_left(l,d):
    for i in range(d):
        list_left_rotation(l)

def d_right(l,d):
    for i in range(d):
        list_right_rotation(l)
if __name__ == "__main__":
    try:
        mylist = [eval(i) for i in input("Enter the elements into the list: ").split(",")]
        print("Before rotation: {}".format(mylist))
        d = int(input("Enter the number of rotations: "))
        d_left(mylist,d)
        print("After Left rotation: {}".format(mylist))
        d_right(mylist,d)
        print("After right rotation: {}".format(mylist))
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        finish_time = tm.time() - start_time
        print("Finished in: {} sec".format(finish_time))
