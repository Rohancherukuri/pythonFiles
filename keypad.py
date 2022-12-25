# Solving a keypad problem in python using recurssion
from time import time

def keypad(s,ans,s_lst):
    """
        This function returns the combination 
        of characters parallel to keypad numbers
    """
    if(len(s)) == 0: # base case
        print(ans)
        return
    
    ch = s[0]
    code = s_lst[int(ch)]
    ros = s[1:]
    for i in range(len(code)):
        keypad(ros,ans + code[i],s_lst)
    

def main():
    """This is a main function"""
    st = input("Enter a number string: ")
    empty_string = ""
    keypad_list = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    print("The Character combinations for string of numbers "+st+" is: ")
    keypad(st,empty_string,keypad_list)


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
    