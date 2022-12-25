# Taking user input from the list until the user quits the program
import time as tm
start_time = tm.time()
if __name__ == "__main__":
    try:
        mylist = []
        while True:
            ch = input("Press 'q' to quit or 'c' to continue, from the program! ")
            if ch == 'q':
                break
            value = eval(input("Enter the elements into the list: "))
            mylist.append(value)
        print("The elements into the list are: {}".format(mylist))
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))
    finally:
        finish_time = tm.time() - start_time
        print("Finished in: {} sec".format(finish_time))