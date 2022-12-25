# Making a clever program using python
import time as tm
start_time = tm.time()
if __name__ == "__main__":
    try:
        print("ODD" if int(input("Enter a number: "))%2 else "EVEN ")
        print("Your program got executed in: {} sec".format(tm.time() - start_time))
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    finally:
        print("Code executed with exit status: 1")
