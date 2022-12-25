# Splitting a given string into substrings in python
from time import time

def sub_split(s,ans):
    """This function recursively splits the given string into the  substrings"""
    if len(s) == 0: # base case
        print(ans)
        return
    
    ch = s[0]
    rest_of_the_string = s[1:]
    sub_split(rest_of_the_string,ans)
    sub_split(rest_of_the_string,ans+ch)

def main():
    """This is main function"""
    s = input("Enter a string: ")
    empty_str = ""
    print("The substrings for the given string "+s+" are: ")
    sub_split(s,empty_str)

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