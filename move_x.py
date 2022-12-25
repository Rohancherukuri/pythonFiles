# Moving 'X' character from any postion to last position
from time import time

def move_all_x_to_end(st):
    """
        This function appends the character 'x' at the end of 
        the string if prersent in the given string inputted by the user
    """
    if len(st) == 0: # base case 
        return ""
    
    ch = st[0]
    ans = move_all_x_to_end(st[1:])
    if ch == "x":
        return (ans + ch)
    return (ch + ans)


def main():
    """This is main function"""
    s = input("Enter a string: ")
    result = move_all_x_to_end(s)
    print("The string is: "+result)

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: ")
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" milli sec]")


    