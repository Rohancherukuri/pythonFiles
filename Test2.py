# File handling in python with Exception handling

def read_file():
    """This is a method which reads the file and displays it"""
    f = open("test.txt","r")
    print(f.read())


def main():
    """This is a main method"""
    try:
        with open("test.txt","w") as f:
            f.write("Hello my name is Rohan\n")
            f.write("And I am studying in engineering 3rd year\n")
        read_file()
            
    except Exception as e:
        print("Sorry an error occurred: "+str(e))
    
    else:
        print("Ths code has been executed successfully")
if __name__ == "__main__":
    try:
        main()
    
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))




