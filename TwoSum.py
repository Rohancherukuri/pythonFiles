# Implementing two sum problem in python
from time import time

def twoSum(num_list,target):
    """This is a method to find the elemental 
       pair whose sum is equal to the target 
    """
    num_dict = dict() # key is number and value is index in num
    
    for i, num in enumerate(num_list):
        comp = target - num
        if comp  in num_dict:
            return num_list[num_dict[comp]],num_list[i]
        
        
        num_dict[num] = i
        
    return None # no sum

def main():
    """This is a main method"""
    mylist = [int(i) for i in input("Enter the numbers: ").split(",")]
    target = int(input("Enter the target variable: "))
    result = twoSum(mylist,target)
    print("The numbers whose sum is "+str(target)+" are: "+str(result))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t2 = time() - t1
        print("[Finished in: "+str(round(t2,3))+" sec]")