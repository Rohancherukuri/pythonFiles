# Testing simple python code
from time import time

def main():
    """This is main function"""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print("The numbers are a match!" if num1 == num2 else "The numbers are not a match!")

if __name__  == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" milli sec]")